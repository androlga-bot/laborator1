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
        symbols+=len(line)
        spaces+=line.count(' ')
        pun_sym+=line.count('.')+line.count(',')+line.count('?')
        pun_sym+=line.count('!')+line.count('-')+line.count(':')
        pun_sym+=line.count(';')+line.count('(')+line.count(')')
        words=len(re.findall(r"(\w+-\w+)|(\w+'\w+)|(\w+-\w+'\w+)|(\w+)",line))
        
        sent=len(re.findall(r"([A-ZА-ЯЁ][^\.!?]*[\.!?])",line))
print(symbols,symbols-spaces,symbols-pun_sym,words,sent)
