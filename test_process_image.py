from ocr_processor import process_images

# Path to the image file
image_path = "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_arbeitsamt_internet.jpeg"

# Call the process_images function and print the output
extracted_text = process_images(image_path)
print("Extracted Text:")
print(extracted_text)
