import os
import easyocr
from PIL import Image
from io import BytesIO

def process_images(image_data):
    """
    Process the image using OCR and return the extracted text.

    Args:
        image_data: either a file path to the image or the image data itself as bytes.

    Returns:
        str: extracted text.
    """
    reader = easyocr.Reader(['de'])

    # Initialize variable to store extracted text
    extracted_text = ""

    # If image_data is a file path, open the image
    if isinstance(image_data, str):
        if not os.path.exists(image_data):
            raise FileNotFoundError(f"Image file not found: {image_data}")
        with open(image_data, 'rb') as image_file:
            image_data = image_file.read()

    # Open image from image data
    image = Image.open(BytesIO(image_data))

    try:
        # Process the image using OCR
        result = reader.readtext(image)
        # Extract text from OCR result
        extracted_text = '\n'.join([entry[1] for entry in result]).strip()
    except Exception as e:
        print(f"Error processing image: {e}")

    return extracted_text
