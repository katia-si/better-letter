# language_model/tests/test_summarizer_long.py

from language_model.summarizer_long import generate_summary_longer

def test_generate_summary_longer():
    # Test case 1: Test with a simple text
    text = "This is a sample text. This text should be summarized."
    summary = generate_summary_longer(text)
    assert isinstance(summary, str)
    assert len(summary) > 0
