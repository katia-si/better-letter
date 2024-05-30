import os
from language_model.text_cleaner import clean_extracted_text, clean_and_save_files

def test_clean_extracted_text():
    sample_text = """
    Dies ist ein Test-\ntext mit eini-gen Zeilenumbrüchen und; einigen: Satzzei-chen. Datum: 01.01.2024
    {Dies sollte entfernt werden} (Dies auch) [Und dies ebenso]
    Sehr geehrte Damen und Herren,
    Dies ist ein Testtext. Berliner Sparkasse
    """
    expected_output = " 01.01.2024 Sehr geehrte Damen und Herren, Dies ist ein Testtext. "
    assert clean_extracted_text(sample_text) == expected_output

def test_clean_and_save_files():
    input_directory = 'test_german_ocr_text'
    output_directory = 'test_german_ocr_text_cleaned'

    if not os.path.exists(input_directory):
        os.makedirs(input_directory)

    sample_filename = 'sample.txt'
    with open(os.path.join(input_directory, sample_filename), 'w', encoding='utf-8') as f:
        f.write("""
        Dies ist ein Test-\ntext mit eini-gen Zeilenumbrüchen und; einigen: Satzzei-chen. Datum: 01.01.2024
        {Dies sollte entfernt werden} (Dies auch) [Und dies ebenso]
        Sehr geehrte Damen und Herren,
        Dies ist ein Testtext. Berliner Sparkasse
        """)

    clean_and_save_files(input_directory, output_directory)

    output_filename = os.path.join(output_directory, 'sample_cldn.txt')
    assert os.path.exists(output_filename)

    with open(output_filename, 'r', encoding='utf-8') as f:
        cleaned_text = f.read()
    expected_output = " 01.01.2024 Sehr geehrte Damen und Herren, Dies ist ein Testtext. "
    assert cleaned_text == expected_output

# Uncomment the following lines if you want to run the tests manually without a test framework
# if __name__ == "__main__":
#     test_clean_extracted_text()
#     test_clean_and_save_files()
#     print("All tests passed!")
