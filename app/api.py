from flask import Flask, request
from language_model.ocr_processor import perform_ocr
from language_model.ocr_processor import process_images
from language_model.text_cleaner import clean_text
from language_model.summarizer_long import generate_summary
from language_model.translator_ger_eng import translate_to_english

app = Flask(__name__)

# defining route for processing image
@app.route('/process_image', methods=['POST'])
def process_image():
    # Get uploaded image file
    image_file = request.files['file']

    # Save the image to a temporary location
    image_path = '/tmp/uploaded_image.jpg'
    image_file.save(image_path)

    # Perform OCR on the image to extract text
    text = perform_ocr(image_path)

    # Clean the extracted text
    cleaned_text = clean_text(text)

    # Summarize the cleaned text
    summary = generate_summary(cleaned_text)

    # Translate the summary to English
    translated_summary = translate_to_english(summary)

    return {
        'original_text': text,
        'cleaned_text': cleaned_text,
        'summary': summary,
        'translated_summary': translated_summary
    }

if __name__ == '__main__':
    app.run(debug=True)
