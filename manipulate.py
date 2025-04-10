import string
def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.capitalize()

def remove_punctuation(s):
    string.punctuation
    return s.translate(str.maketrans('', '', string.punctuation))
    
