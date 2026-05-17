import requests

def get_rhyme(word):

    url = f"https://api.datamuse.com/words?rel_rhy={word}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Could not fetch rhymes."

    data = response.json()

    rhymes = []
    for item in data[:5]:
        rhymes.append(item["word"])

    return rhymes






