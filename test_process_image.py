from language_model.ocr_processor import process_image
import os


# List of image paths
images = [
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_arbeitsamt_invitation.jpg",
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_dog_tax.jpg",
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_school_hamburg.png",
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_taxes.jpg",
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_tk_insurance_internet.jpg",
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_tk_insurance_sick_leave.jpg",
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_vattenfall_cancelation.jpg",
    "/Users/carstenvolland/code/katia-si/better-letter/text_extractor/data_images/letter_vattenfall_counter.jpg"
]

# Loop through each image path and apply the process_image function
for image in images:
    filename = os.path.basename(image).upper()
    processed_text = process_image(image)
    print(f"{filename}: {processed_text}")
