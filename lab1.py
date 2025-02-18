import csv
import re
symbols = 0
spaces = 0
pun_sym = 0
words = 0
sentence = 0
picture = 0
with open('steam_description_data.csv', encoding='utf-8') as f:
    r=csv.reader(f)
    for l in r:
        line = ','.join(l)
        symbols += len(line)
        spaces += line.count(' ')
        pun_sym += line.count('.') + line.count(',') + line.count('?')
        pun_sym += line.count('!') + line.count('-') + line.count(':')
        pun_sym += line.count(';') + line.count('(') + line.count(')')
        words += len(re.findall("(\w+-\w+)|(\w+'\w+)|(\w+-\w+'\w+)|(\w+)", line))        
        sentence += len(re.findall("([A-ZА-ЯЁ][^\.!?]*[\.!?])", line))
        picture += len(re.findall('(<img\ssrc[=]["]{1,}https[:][/]{2})', line))
print(symbols, symbols-spaces, symbols-pun_sym, words, sentence, picture)
