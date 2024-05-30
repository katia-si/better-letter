from flask import Flask, request

better_letter = Flask(__name__)

# defining route for processing image
@better_letter.route('/process_image', methods=['POST'])
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
    better_letter.run(debug=True)
