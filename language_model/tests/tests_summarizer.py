import os
from language_model.summarizer_long import generate_summary_longer, summarize_text

def test_generate_summary_longer():
    sample_text = (
        "Dies ist ein langer Text auf Deutsch, der zusammengefasst werden muss. "
        "Das Modell wird eine Zusammenfassung dieses Textes erstellen."
    )
    summary = generate_summary_longer(sample_text)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_summarize_text():
    input_directory = 'test_german_text'
    output_directory = 'test_german_summary'

    if not os.path.exists(input_directory):
        os.makedirs(input_directory)

    sample_filename = 'sample.txt'
    with open(os.path.join(input_directory, sample_filename), 'w', encoding='utf-8') as f:
        f.write(
            "Dies ist ein langer Text auf Deutsch, der zusammengefasst werden muss. "
            "Das Modell wird eine Zusammenfassung dieses Textes erstellen."
        )

    summarize_text(input_directory, output_directory)

    output_filename = os.path.join(output_directory, 'sample_sum.txt')
    assert os.path.exists(output_filename)

    with open(output_filename, 'r', encoding='utf-8') as f:
        summary = f.read()
    assert len(summary) > 0

# Uncomment the following lines if you want to run the tests manually without a test framework
# if __name__ == "__main__":
#     test_generate_summary_longer()
#     test_summarize_text()
#     print("All tests passed!")
