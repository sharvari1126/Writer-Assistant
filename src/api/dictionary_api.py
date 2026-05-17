import requests

def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(url)

    if response.status_code != 200:
        return "Word not found"


    data = response.json()

    meaning = data[0]["meanings"][0]["definitions"][0]["definition"]

    return meaning

