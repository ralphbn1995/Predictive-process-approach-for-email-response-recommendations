import stanza
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Function to perform stylometric analysis using K-Means Clustering
def perform_stylometric_analysis(email, chunk_size=100, num_clusters=3):
    # Load Stanza pipeline for English
    nlp = stanza.Pipeline(lang='en', processors='tokenize')

    # Split the email into chunks
    chunks = [email[i:i+chunk_size] for i in range(0, len(email), chunk_size)]

    # Extract stylometric features for each chunk
    stylometric_features = []
    for chunk in chunks:
        doc = nlp(chunk)
        # Extract features (e.g., sentence length, vocabulary diversity, etc.)
        features = [len(sent.words) for sent in doc.sentences]
        stylometric_features.append(features)

    # Flatten the list of features for clustering
    flat_features = [item for sublist in stylometric_features for item in sublist]

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(flat_features)

    return cluster_labels

# Example Usage
received_email = "This is a sample email with different writing styles in each chunk. ..."

# Assuming you have identified the optimal chunk size and number of clusters for your dataset
stylometric_clusters = perform_stylometric_analysis(received_email, chunk_size=100, num_clusters=3)
print("Stylometric Clusters:", stylometric_clusters)
