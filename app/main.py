import sys
from language_model.ocr_processor import process_image
from language_model.text_cleaner import clean_extracted_text
from language_model.summarizer_long import generate_summary_dynamic
from language_model.translator_ger_eng import translate_to_english_and_print

def main(image_path):
    # step 1: process the provided image using ocr
    ocr_output_text = process_image(image_path)
    if not ocr_output_text:
        print("error: failed to extract text from the image.")
        return

    # print("ocr output text:")
    # print(ocr_output_text)

    # step 2: clean the extracted text
    cleaned_text = clean_extracted_text(ocr_output_text)
    # print("cleaned text:")
    # print(cleaned_text)

    # step 3: summarize the cleaned text
    summarized_text = generate_summary_dynamic(cleaned_text)
    # print("summarized text:")
    # print(summarized_text)

    # step 4: translate the summaries to english
    translated_text = translate_to_english_and_print(summarized_text)
    print("translated text:")
    print(translated_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python main.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)
