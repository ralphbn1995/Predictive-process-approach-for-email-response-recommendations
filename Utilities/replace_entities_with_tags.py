import stanza

# Function to replace named entities with tags using Stanza
def replace_entities_with_tags(sentences):
    # Load Stanza pipeline for English
    nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')

    # Placeholder for storing modified sentences
    modified_sentences = []

    # Iterate through each sentence
    for sentence in sentences:
        # Process the sentence using Stanza
        doc = nlp(sentence)

        # Placeholder for storing modified words in the sentence
        modified_words = []

        # Iterate through each word in the sentence
        for word in doc.sentences[0].words:
            # Check if the word is a named entity
            if word.ner != 'O':
                # Replace the named entity with a tag (e.g., {date}, {person})
                modified_words.append(f'{{{word.ner.lower()}}}')
            else:
                # Keep non-entity words as they are
                modified_words.append(word.text)

        # Concatenate modified words to form the modified sentence
        modified_sentence = ' '.join(modified_words)
        modified_sentences.append(modified_sentence)

    return modified_sentences

# Example Usage
sentences = ["John Doe will visit New York on January 1st."]
modified_sentences = replace_entities_with_tags(sentences)
print("Original Sentences:", sentences)
print("Modified Sentences:", modified_sentences)
