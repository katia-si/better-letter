import os
from language_model.ocr_processor import process_images
from language_model.text_cleaner import clean_and_save_files
from language_model.summarizer_long import summarize_text
from language_model.translator_ger_eng import translate_summaries

def main():
    # Define input and output directories
    image_directory = "text_extractor/data_images"
    output_directory_ocr = "raw_data/german_ocr_text"
    output_directory_cleaned = "raw_data/german_ocr_text_cleaned"
    output_directory_summarized = "raw_data/german_summary"
    output_directory_english = "raw_data/english_summary"

    # Step 1: Process the example image using OCR
    process_images(image_directory, output_directory_ocr)

    # Step 2: Clean the extracted text files
    clean_and_save_files(output_directory_ocr, output_directory_cleaned)

    # Step 3: Summarize the cleaned text
    summarize_text(output_directory_cleaned, output_directory_summarized)

    # Step 4: Translate the summaries to English
    translate_summaries(output_directory_summarized, output_directory_english)

if __name__ == "__main__":
    main()
