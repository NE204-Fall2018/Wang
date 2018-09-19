manuscript = report
latexopt = -file-line-error -halt-on-error

# Build the PDF of the lab report from the source files
$(manuscript).pdf: $(manuscript).tex text/*.tex references.bib images/*.png
	pdflatex $(latexopt) $(manuscript).tex
	bibtex $(manuscript).aux
	bibtex $(manuscript).aux
	pdflatex $(latexopt) $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex

# Get/download necessary data
data :
	wget https://www.dropbox.com/s/hutmwip3681xlup/lab0_spectral_data.txt?dl=0 -O lab0_spectral_data.txt

# Validate that downloaded data is not corrupted
validate :
	echo "WARNING: make validate has not yet been implemented."

# Run tests on analysis code
test :
	nosetests --no-byte-compile test/*

# Automate running the analysis code
analysis :
	cd code/ && python2 example.py
	cd code/ && python2 analysis.py

clean :
	rm -f *.aux *.log *.bbl *.lof *.lot *.blg *.out *.toc *.run.xml *.bcf
	rm -f text/*.aux
	rm $(manuscript).pdf
	rm code/*.pyc

# Make keyword for commands that don't have dependencies
.PHONY : test data validate analysis clean
