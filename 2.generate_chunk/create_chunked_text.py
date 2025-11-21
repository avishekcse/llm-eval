import os
import nltk
from transformers import GPT2Tokenizer

# Download the punkt sentence tokenizer (for sentence splitting)
nltk.download('punkt')

# Load the GPT-2 tokenizer (you can use other model tokenizers like GPT-3 or BERT)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Function to read text files from a folder
def read_txt_files_from_folder(folder_path):
    files_content = []
    
    # List all .txt files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            
            # Open the file and read content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                files_content.append((file_name, content))
    
    return files_content

# Function to chunk text by sentences and then by token count
def chunk_text_by_sentences(text, max_tokens=1024):
    # Split text into sentences
    sentences = nltk.sent_tokenize(text)
    current_chunk = ""
    chunks = []

    for sentence in sentences:
        # Tokenize the sentence
        sentence_tokens = tokenizer.encode(sentence)
        
        # If adding this sentence exceeds the token limit, create a new chunk
        if len(tokenizer.encode(current_chunk + sentence)) > max_tokens:
            if current_chunk:  # Add the current chunk if it's not empty
                chunks.append(current_chunk)
            current_chunk = sentence  # Start a new chunk with the current sentence
        else:
            current_chunk += " " + sentence  # Append sentence to current chunk
    
    if current_chunk:
        chunks.append(current_chunk)  # Add the last chunk

    return chunks

# Function to save chunks to files in the target folder
def save_chunks_to_files(chunks, source_file_name, target_folder):
    # Create the target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Save each chunk as a new file
    for idx, chunk in enumerate(chunks, start=1):
        chunk_file_name = f"{os.path.splitext(source_file_name)[0]}_chunk_{idx}.txt"
        chunk_file_path = os.path.join(target_folder, chunk_file_name)
        
        with open(chunk_file_path, 'w', encoding='utf-8') as chunk_file:
            chunk_file.write(chunk)
        
        print(f"Saved chunk {idx} from {source_file_name} as {chunk_file_name}")

# Example usage
source_folder = './input_txt_files'  # Replace with the relative path to your source folder
target_folder = './output_chunked_txt_files'  # Replace with the relative path to your target folder

# Read all .txt files in the source folder
texts = read_txt_files_from_folder(source_folder)

# Process each text file and save the chunks
for source_file_name, text in texts:
    # Create chunks of text from the file
    chunks = chunk_text_by_sentences(text, max_tokens=1024)  # You can adjust the token size
    
    # Save chunks to the target folder
    save_chunks_to_files(chunks, source_file_name, target_folder)

