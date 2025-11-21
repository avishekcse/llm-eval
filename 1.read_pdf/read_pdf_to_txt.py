import os
import PyPDF2
import glob

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

# Function to process PDF files in the folder and save to a destination folder
def convert_pdfs_to_txt(source_folder, destination_folder):
    # Ensure destination folder exists, create it if it doesn't
    os.makedirs(destination_folder, exist_ok=True)
    
    # Get all PDF files in the source folder
    pdf_files = glob.glob(os.path.join(source_folder, "*.pdf"))
    
    for pdf_file in pdf_files:
        # Extract text from PDF
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            # Generate a txt filename based on the PDF filename
            txt_filename = os.path.splitext(os.path.basename(pdf_file))[0] + ".txt"
            txt_filepath = os.path.join(destination_folder, txt_filename)
            
            # Write the extracted text to a txt file
            try:
                with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text)
                print(f"Converted: {pdf_file} -> {txt_filepath}")
            except Exception as e:
                print(f"Error writing to {txt_filepath}: {e}")
        else:
            print(f"Failed to extract text from {pdf_file}")

# Specify the source folder containing PDFs and the destination folder for text files
source_folder = './input_pdf_files'  # Relative path to your PDF folder
destination_folder = './output_txt_files'  # Relative path to your destination folder for txt files

# Run the conversion process
convert_pdfs_to_txt(source_folder, destination_folder)

