import os
import json
from sentence_transformers import SentenceTransformer

# Load the Sentence-BERT model (pre-trained model for generating embeddings)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # A smaller, fast, and efficient model

# Function to read the entire content of a file
def read_text_from_file(file_path):
    """Reads the entire text from a .txt file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

# Function to generate embeddings using Sentence-BERT
def generate_embedding(text):
    """Generates embeddings for a given text using Sentence-BERT."""
    # Use the model to generate embeddings (a vector for each sentence/chunk)
    embedding = model.encode(text)
    return embedding

# Function to save embeddings to a target file
def save_embeddings(embeddings, target_file_path):
    """Saves embeddings to a target file in JSON format."""
    with open(target_file_path, 'w', encoding='utf-8') as f:
        json.dump(embeddings.tolist(), f)  # Convert numpy array to list before saving

# Function to process multiple .txt files in the source folder
def process_multiple_files(source_folder, target_folder):
    """Process all .txt files in the source folder, generate embeddings, and save to the target folder."""
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Get all .txt files from the source folder
    source_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]

    if not source_files:
        print("No .txt files found in the source folder.")
        return

    # Process each source file
    for source_file in source_files:
        source_path = os.path.join(source_folder, source_file)
        target_file = f"{os.path.splitext(source_file)[0]}_embeddings.json"  # Name the target file based on the source file name
        target_path = os.path.join(target_folder, target_file)

        # Read the entire text from the source .txt file and generate embeddings
        text = read_text_from_file(source_path)
        embedding = generate_embedding(text)

        # Save embeddings to the target .json file
        save_embeddings(embedding, target_path)
        print(f"Embeddings for '{source_file}' saved to '{target_path}'.")

# Main function to execute the entire process
def main():
    # Get the script's current directory (relative to the location of the script)
    script_dir = os.path.dirname(os.path.abspath(__file__))  # This will give the folder of the current script
    
    # Define the relative paths for the source and target folders
    source_folder = os.path.join(script_dir, './input_chunked_txt_files')  # Relative path to source folder
    target_folder = os.path.join(script_dir, './output_embedded_files')  # Relative path to target folder

    # Process the files in the source folder
    process_multiple_files(source_folder, target_folder)

if __name__ == "__main__":
    main()

