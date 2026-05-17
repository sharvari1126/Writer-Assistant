import requests

def get_synonyms(word):

    url = f"https://api.datamuse.com/words?rel_syn={word}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Could not fetch synonyms."

    data = response.json()

    synonyms = []
    for item in data[:5]:
        synonyms.append(item["word"])

    return synonyms





