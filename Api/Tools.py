from guesslang import Guess


def detectLanguage(snippet:str):
    guess=Guess()
    language = guess.language_name(snippet)
    return language

