import os
from language_model.translator_ger_eng import translate_to_english, translate_summaries

def test_translate_to_english():
    german_text = "Dies ist ein Test."
    english_text = translate_to_english(german_text)
    assert isinstance(english_text, str)
    assert len(english_text) > 0
    assert "test" in english_text.lower()

def test_translate_summaries():
    input_directory = 'test_german_summaries'
    output_directory = 'test_english_summaries'

    if not os.path.exists(input_directory):
        os.makedirs(input_directory)

    sample_filename = 'sample.txt'
    with open(os.path.join(input_directory, sample_filename), 'w', encoding='utf-8') as f:
        f.write("Dies ist ein Test.")

    translate_summaries(input_directory, output_directory)

    output_filename = os.path.join(output_directory, 'sample.txt')
    assert os.path.exists(output_filename)

    with open(output_filename, 'r', encoding='utf-8') as f:
        translated_text = f.read()
    assert len(translated_text) > 0
    assert "test" in translated_text.lower()

# Uncomment the following lines if you want to run the tests manually without a test framework
# if __name__ == "__main__":
#     test_translate_to_english()
#     test_translate_summaries()
#     print("All tests passed!")
