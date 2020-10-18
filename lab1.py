import csv
import re
symbols=int()
spaces=int()
pun_sym=int()
words=int()
sent=int()
with open('steam_description_data.csv') as f:
    r=csv.reader(f)
    for line in r:
        string = ','.join(r)
        symbols+=len(string)
        spaces+=string.count(' ')
        pun_sym+=string.count('.')+string.count(',')+string.count('?')
        pun_sym+=string.count('!')+string.count('-')+string.count(':')
        pun_sym+=string.count(';')+string.count('(')+string.count(')')
        words=len(re.findall(r"(\w+-\w+)|(\w+'\w+)|(\w+-\w+'\w+)|(\w+)",string))
        
        sent=len(re.findall(r"([A-ZА-ЯЁ][^\.!?]*[\.!?])",string))
print(symbols,symbols-spaces,symbols-pun_sym,words,sent)
