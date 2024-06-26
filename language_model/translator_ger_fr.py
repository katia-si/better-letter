from transformers import MarianMTModel, MarianTokenizer
import os

# initialize the tokenizer and model for translation
tokenizer_translate = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-fr")
model_translate = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-de-fr")

def translate_and_print(german_text):
    """
    translates german text to french using a pre-trained MarianMT model and prints the translation.

    Args:
        german_text (str):  german text to translate.

    Returns:
        str:  translated french text.
    """
    inputs = tokenizer_translate(german_text, return_tensors="pt", padding=True, truncation=True)
    translated = model_translate.generate(**inputs)
    translated_text = tokenizer_translate.batch_decode(translated, skip_special_tokens=True)[0]

    # print("Translated text:")
    # print(translated_text)

    return translated_text
