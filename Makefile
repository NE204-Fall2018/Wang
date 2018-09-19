# Define variables
manuscript = report
latexopt = -file-line-error -halt-on-error

# Generate the lab report in PDF format from the *.tex files
$(manuscript).pdf: 
$(manuscript).tex text/*.tex references.bib images/*.png
	pdflatex $(latexopt) $(manuscript).tex
	bibtex $(manuscript).aux
	bibtex $(manuscript).aux
	pdflatex $(latexopt) $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex

# Download data
data :
	wget https://www.dropbox.com/s/k692avun0144n90/lab0_spectral_data.txt?dl=0 -O data.txt

# Validate the downloaded data not corrupted by md5 checksum
validate :
	md5sum lab0_spectral_data.txt
	md5sum -c lab0_spectral_data.md5
# if not validate
# echo "WARNING: make validate has not yet been implemented."

# Run tests on analysis code
test :
	nosetests --no-byte-compile test/*

# Automate running the analysis code
analysis :
	cd code/ && python2 example.py
	cd code/ && python2 analysis.py
	
# Clean unnecessary files in the repository
clean :
	rm -f *.aux *.log *.bbl *.lof *.lot *.blg *.out *.toc *.run.xml *.bcf
	rm -f text/*.aux
	rm $(manuscript).pdf
	rm code/*.pyc

# Make keyword for commands that don't have dependencies
.PHONY : test data validate analysis clean
