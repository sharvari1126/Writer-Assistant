import requests

def get_phrase_to_word(phrase):

    url = f"https://api.datamuse.com/words?ml={phrase}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Could not fetch suggestions."

    data = response.json()

    words = []

    for item in data[:5]:
        words.append(item["word"])

    return words




