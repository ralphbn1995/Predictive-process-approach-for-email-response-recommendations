import yake
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import stanza

# Function to identify business context using Yake
def identify_business_context(sentences):
    custom_kwextractor = yake.KeywordExtractor()
    keywords = [kw[0] for kw in custom_kwextractor.extract_keywords_from_text(sentences)]
    return " ".join(keywords)

# Function to compute cosine similarity between vectors A and B
def compute_cosine_similarity(A, B):
    similarity = cosine_similarity(A, B)
    return similarity[0][0]

# Function to recommend email template
def recommend_email_template(predicted_events, received_email, threshold=0.5):
    for event in predicted_events:
        # Step 1: Retrieve email sentences containing predicted BP knowledge
        retrieved_sentences = retrieve_email_sentences(received_email, event)

        # Step 2: Identify business context using Yake
        received_business_context = identify_business_context(received_email)
        retrieved_business_contexts = [identify_business_context(sentence) for sentence in retrieved_sentences]

        # Step 3: Filter retrieved sentences based on business context similarity
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([received_business_context] + retrieved_business_contexts)
        cosine_similarities = [
            compute_cosine_similarity(tfidf_matrix[0], tfidf_matrix[i]) for i in range(1, len(retrieved_business_contexts) + 1)
        ]
        similar_sentences = [retrieved_sentences[i - 1] for i, similarity in enumerate(cosine_similarities) if similarity > threshold]

        # Step 4: Keep sentences with the same writing style
        stylometric_clusters = perform_stylometric_analysis(received_email)
        stylometric_features = perform_stylometric_analysis(similar_sentences)
        selected_sentences = filter_sentences_by_style(stylometric_clusters, stylometric_features)

        # Step 5: Replace named entities with tags using Stanza
        modified_sentences = replace_entities_with_tags(selected_sentences)

        # Step 6: Concatenate sentences in the relative order of appearance
        concatenated_template = "\n".join(modified_sentences)

        print(f"Recommended Email Template for Event {event}:\n{concatenated_template}\n")

# Example Usage
predicted_events = [1, 2, 3]  # Replace with your actual list of predicted events
received_email = "This is a sample received email with business context and writing style."

recommend_email_template(predicted_events, received_email)
