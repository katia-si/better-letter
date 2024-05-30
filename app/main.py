import os
import sys

# add the project root directory to the python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# import modules from the language_model package
from language_model.ocr_processor import process_images
from language_model.text_cleaner import clean_and_save_files
from language_model.summarizer_long import summarize_text
from language_model.translator_ger_eng import translate_summaries

def main():
    # define input and output directories
    image_directory = os.path.join(project_root, "text_extractor/data_images")
    output_directory_ocr = os.path.join(project_root, "raw_data/german_ocr_text")
    output_directory_cleaned = os.path.join(project_root, "raw_data/german_ocr_text_cleaned")
    output_directory_summarized = os.path.join(project_root, "raw_data/german_summary")
    output_directory_english = os.path.join(project_root, "raw_data/english_summary")

    # step 1: process the example image using ocr
    process_images(image_directory, output_directory_ocr)

    # step 2: clean the extracted text files
    clean_and_save_files(output_directory_ocr, output_directory_cleaned)

    # step 3: summarize the cleaned text
    summarize_text(output_directory_cleaned, output_directory_summarized)

    # step 4: translate the summaries to english
    translate_summaries(output_directory_summarized, output_directory_english)

if __name__ == "__main__":
    main()
