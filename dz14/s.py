import re
import string

LET = string.ascii_letters + " "

def str_replace(text):
    return "".join(i for i in text if i in LET).lower()

test_text = "asdasdsfagagFFFf    12324"

print(str_replace(test_text))

def get_new_text(text):
    return re.sub(r'[^a-zA-Z ]+', '', text).lower()

print(get_new_text(test_text))