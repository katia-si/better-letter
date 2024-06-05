
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

# Load pre-trained BART model and tokenizer for German
tokenizer = AutoTokenizer.from_pretrained("Shahm/bart-german")
model = AutoModelForSeq2SeqLM.from_pretrained("Shahm/bart-german")

def calculate_dynamic_lengths(input_text, max_tokens=1024):
    """
    calculate dynamic max_length and min_length based on the length of the input text.

    Args:
        input_text (str):  input text.
        max_tokens (int): maximum number of tokens the model can handle (default 1024 for BART).

    Returns:
        max_length (int): calculated maximum length for the summary.
        min_length (int): calculated minimum length for the summary.
    """
    # tkenize the input text
    tokenized_text = tokenizer.encode(input_text, return_tensors="pt", truncation=True)
    input_length = tokenized_text.size(1)

    # define the dynamic lengths as a percentage of the input length
    max_length = min(max(input_length // 2, 100), 500)  # max half the input length, but min 100 and at most 500
    min_length = max(min(input_length // 4, 50), 100)  # max a quarter of the input length, but min 50 and at most 100

    return max_length, min_length

def generate_summary_dynamic(text: str) -> str:
    """
    generate a dynamic summary of the input text.

    Args:
        text (str): input text.

    Returns:
        str: generated summary.
    """
    # calculate dynamic lengths
    max_length, min_length = calculate_dynamic_lengths(text)

    # Ttkenize and generate summary
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=2,
        early_stopping=False
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


def summarize_text_and_print(input_text):
    """
    summarize the input text and print the summary.

    Args:
        input_text (str): The input text to be summarized.

    Returns:
        str: generated summary.
    """
    summary = generate_summary_dynamic(input_text)
    # print("Summary:")
    # print(summary)
    return summary
