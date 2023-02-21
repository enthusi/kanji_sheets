import sys
import random

pick = False

infile=open('newvocab.txt','r')
outfile_learn=open('words_learn.tex','w')
outfile_full =open('words_full.tex','w')
wordlist=[]
for line in infile:
    if len(line)<3: continue
    word=line.strip()
    wordlist.append(word)
full_list=wordlist.copy()

start=-30
end=-1

if pick:
    start=0
    end=-1
    
if end<0: end=len(wordlist)+1
wordlist=wordlist[start:end]
#optionally: only above num blabla    
if not pick:
    random.seed(1339)
    
random.shuffle(wordlist)

if pick:
    #cut the shuffled list and ick top 30 AFTER shuffle
    wordlist=wordlist[0:30]
    
for line in wordlist:
    num,kanji,word=line.split(':')
    outfile_full.write('\kariert{2}{2} \\vspace{0.2cm}%s / {\Huge \\begin{CJK}{UTF8}{min} %s \\end{CJK}} / %s\\\\\n' % (word,kanji,num))
    outfile_learn.write('\kariert{2}{2} \\vspace{0.2cm}%s \\phantom{/ {\Huge \\begin{CJK}{UTF8}{min} %s \\end{CJK}} / %s}\\\\\n' % (word,kanji,num))
        
        
    
#and add a list of all words
outfile_full.write('\\cleardoublepage\n')
for line in wordlist:
    num,kanji,word=line.split(':')
    outfile_full.write('{\Huge \\begin{CJK}{UTF8}{min} %s\\end{CJK}}\hspace{0.1cm}\n' % (kanji))


outfile_full.write('\\cleardoublepage\n \onecolumn \n\\begin{spacing}{2.5}\n')
for line in full_list:
    num,kanji,word=line.split(':')
    outfile_full.write('{\Huge \\begin{CJK}{UTF8}{min} %s\\end{CJK}}\hspace{0.1cm}\n' % (kanji))
outfile_full.write('\\end{spacing}\n')    
