   
from src.api.dictionary_api import get_word_meaning
from src.api.synonym_api import get_synonyms
from src.api.rhyme_api import get_rhymes
from src.api.phrase_api import get_phrase_to_word   
from rich import print 
while True:
   

    print("[bold Magenta]=====Writer Assistant=====[bold Magenta]")
    print("1. Meaning")
    print("2. Synonyms")
    print("3. Rhymes")
    print("4. Phrase to Word")
    print("5. Exit")

    choice = input("Choose an option : ")

    if choice=="1":
        word = input("Enter a word : ")
        print(get_word_meaning(word))
    elif choice=="2":
        word = input("Enter a word : ")
        print(get_synonyms(word))
    elif choice=="3":
        word = input("Enter a word : ")
        print(get_rhymes(word)) 
    elif choice=="4":
        phrase = input("Enter the phrase : ")
        print(get_phrase_to_word(phrase))
    elif choice=="5":
        print("Thank you for using Writer Assistant.")
        break
    else:
        print("Invalid choice.")
        

        