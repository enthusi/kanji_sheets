sheet.pdf: newvocab.txt randomize_vocab.py
	python randomize_vocab.py
	pdflatex sheet.tex
	rm sheet.log
	rm sheet.aux
	
    

