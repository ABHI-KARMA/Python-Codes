import json
from difflib import get_close_matches

data = json.load(open("data.json"))

class Dictionary():
    def __init__(self,word):
        self.word = word
    
    def search_meaning(self):
        self.word = self.word.lower()
        if self.word in data:
            return data[self.word]
        elif len(get_close_matches(self.word,data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes, N if no: "% get_close_matches(self.word,data.keys())[0]).lower()
            if yn == 'y':
                return data[get_close_matches(self.word,data.keys())[0]]
            elif yn == 'n':
                return "the word doesn't exist, please check it"
            else:
                return "we didn't understand your entry"
        else:
            return "the word doesn't exist, please check it"
    
word = input()
d = Dictionary(word)

if type(d) == list:
    for item in d:
        print(item)
else:
    print(d.search_meaning())
