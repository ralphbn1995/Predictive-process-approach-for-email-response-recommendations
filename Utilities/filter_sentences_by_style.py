# Function to filter sentences by writing style
def filter_sentences_by_style(stylometric_clusters, sentences, target_cluster):
    # Placeholder for storing filtered sentences
    filtered_sentences = []

    # Iterate through each sentence and its corresponding cluster
    for sentence, cluster_label in zip(sentences, stylometric_clusters):
        # Check if the cluster label matches the target cluster
        if cluster_label == target_cluster:
            # Keep the sentence if it belongs to the target cluster
            filtered_sentences.append(sentence)

    return filtered_sentences

# Example Usage
sentences = ["This is a sentence with style 1.", "Another sentence with style 2.", "Different style in this sentence."]
target_cluster = 1  # Replace with the cluster label you want to filter

filtered_sentences = filter_sentences_by_style(stylometric_clusters, sentences, target_cluster)
print("Original Sentences:", sentences)
print(f"Filtered Sentences for Cluster {target_cluster}:", filtered_sentences)
