import time
import sys
from language_model.ocr_processor import process_image
from language_model.text_cleaner import clean_extracted_text
from language_model.summarizer_ger import generate_summary_dynamic
from language_model.translator_ger_eng import translate_and_print

def main(image_path):
    total_start_time = time.time() # meausre the total start time

    # step 1: process the provided image using ocr
    start_time = time.time()
    ocr_output_text = process_image(image_path)
    ocr_time = time.time() - start_time
    if not ocr_output_text:
        print("error: failed to extract text from the image.")
        return

    print("💁 ocr output text:")
    print(ocr_output_text)
    print(f"🕒 Time taken for OCR: {ocr_time:.2f} seconds\n")

    # step 2: clean the extracted text
    start_time = time.time()
    cleaned_text = clean_extracted_text(ocr_output_text)
    clean_time = time.time() - start_time
    print("💁 cleaned text:")
    print(cleaned_text)
    print(f"🕒 Time taken for cleaning text: {clean_time:.2f} seconds\n")

    # step 3: summarize the cleaned text
    start_time = time.time()
    summarized_text = generate_summary_dynamic(cleaned_text)
    summarize_time = time.time() - start_time
    print("💁 Summarized text:")
    print(summarized_text)
    print(f"🕒 Time taken for summarizing text: {summarize_time:.2f} seconds\n")

    # step 4: translate the summaries to english
    start_time = time.time()
    translated_text = translate_and_print(summarized_text)
    translate_time = time.time() - start_time
    print("💁 Translated text:")
    print(translated_text)
    print(f"🕒 Time taken for translating text: {translate_time:.2f} seconds\n")


    total_time = time.time() - total_start_time
    print(f"🕒 Total time taken: {total_time:.2f} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python main.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)


