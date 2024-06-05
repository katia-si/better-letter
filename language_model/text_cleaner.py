import re

def clean_extracted_text(text):
    """
    cleans the extracted text by removing hyphens at line breaks, newlines,
    extra spaces, and text inside brackets. Also processes specific markers
    and removes unnecessary parts.

    Args:
        text (str): the extracted text to be cleaned.

    returns:
        str: the cleaned text.
    """
    text = re.sub(r'(\w+)-\n+(\w+)', r'\1\2', text)  # remove hyphens at line breaks
    text = text.replace('\n', ' ')  # replace newlines with spaces
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    text = re.sub(r';', ',', text)  # replace semicolons with commas
#    text = re.sub(r':', '.', text)  # replace colons with periods
    text = re.sub(r'_', ',', text)  # replace underscore with commas
    text = re.sub(r' 8 ', ' ', text) # remove the strange 8 from the arbeitsamt invite


    # remove text inside curly or other brackets
    text = re.sub(r'\{.*?\}', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)

    # find the index of the first occurrence of "Datum:" and remove text before it
    datum_index = text.find("Datum:")
    if datum_index != -1:
        text = text[datum_index+len("Datum:"):]

#    # find the index of the first occurrence of "E-Mail:" and remove text before it
#    email_index = text.find("E-Mail")
#    if email_index != -1:
#        text = text[email_index:]


    # remove text before "Sehr geehrt" followed by any characters
    sehr_geehrt_index = re.search(r'Sehr geehrt.*', text, flags=re.IGNORECASE)
    if sehr_geehrt_index:
        text = text[sehr_geehrt_index.start():]

    # remove text before "Guten Tag" followed by any characters
    guten_tag_index = re.search(r'Guten Tag.*', text, flags=re.IGNORECASE)
    if guten_tag_index:
        text = text[guten_tag_index.start():]

    # find the index of "Berliner Sparkasse" and remove everything after it
    berliner_sparkasse_index = text.find("Berliner Sparkasse")
    if berliner_sparkasse_index != -1:
        text = text[:berliner_sparkasse_index]

    # find the index of the first comma and remove it and everything before it
    first_comma_index = text.find(',')
    if first_comma_index != -1:
        text = text[first_comma_index+1:]

    return text


def clean_extracted_text_and_print(text):
    """
    Cleans the extracted text and prints the cleaned text.

    Args:
        text (str): The extracted text to be cleaned.
    """
    cleaned_text = clean_extracted_text(text)
    return cleaned_text
