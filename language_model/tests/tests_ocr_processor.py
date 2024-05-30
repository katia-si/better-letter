import os
from language_model.ocr_processor import process_images

def test_process_images():
    image_directory = 'test_images'
    output_directory = 'test_output'

    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    # Add a sample image to the test_images directory for testing
    # For example purposes, let's assume 'sample.jpg' is your test image
    # Ensure this image exists or create a mock image for testing
    with open(os.path.join(image_directory, 'sample.jpg'), 'w') as f:
        f.write("test image content")

    process_images(image_directory, output_directory)

    # Check if the output file is created
    assert os.path.exists(os.path.join(output_directory, 'sample.txt'))
