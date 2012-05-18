MAIN = main.ltx

BASE := $(basename $(MAIN))

XFIGS := $(wildcard figures/*.fig)
TEXFIGS := $(XFIGS:.fig=.tex)

XGRAPHS := $(wildcard graph/*.gnuplot)
FIGGRAPHS := $(XGRAPHS:.gnuplot=.fig)
TEXGRAPHS := $(XGRAPHS:.gnuplot=.tex)

TEXFILES := $(sort $(MAIN) $(wildcard *.tex) $(TEXFIGS) $(TEXGRAPHS))
BIBFILES := $(wildcard *.bib)
STYFILES := $(wildcard *.sty)

LATEX = pdflatex \\nonstopmode\\input
BIBTEX = bibtex -min-crossrefs=1000
DVIPS = dvips -j0 -G0 -t letter
PS2PDF = GS_OPTIONS=-sPAPERSIZE=letter ps2pdf -sPAPERSIZE=letter

all: $(BASE).ps $(BASE).pdf

.PRECIOUS: $(FIGGRAPHS)

%.pdf %.tex: %.fig
	fig2dev -L pdftex -p1 $< > $*.pdf
	fig2dev -L pstex_t -p $*.pdf $< > $*.tex

%.ps: %.pdf
	pdf2ps $< $@

RERUN = egrep -q '(^LaTeX Warning:|\(natbib\)).* Rerun'
UNDEFINED = egrep -q '^(LaTeX|Package natbib) Warning:.* undefined'

$(BASE).pdf: $(TEXFILES) $(STYFILES) $(BIBFILES) $(EPSFIGS) $(PDFFIGS) $(PDFGRAPHS)
	test ! -s $*.aux || $(BIBTEX) $* || rm -f $*.aux $*.bbl
	$(LATEX) $(MAIN)
	@if test ! -f $*.bbl || $(RERUN) $(BASE).log \
			|| $(UNDEFINED) $(BASE).log; then \
		set -x; \
		$(BIBTEX) $(BASE); \
		$(LATEX) $(MAIN); \
		! $(RERUN) $(BASE).log || $(LATEX) $(MAIN); \
		! $(RERUN) $(BASE).log || $(LATEX) $(MAIN); \
	fi
	test ! -f .xpdf-running || xpdf -remote $(BASE)-server -reload
	touch $(BASE).dvi

.SECONDARY: $(BASE).pdf $(EPSGRAPHS)

xpdf: $(BASE).pdf
	if test -f .xpdf-running; then			\
		xpdf -remote $(BASE)-server -quit;	\
		sleep 1;				\
	fi
	touch .xpdf-running
	(xpdf -remote $(BASE)-server $(BASE).pdf; rm -f .xpdf-running) &

clean:
	rm -f $(BASE).ps $(BASE).pdf
	rm -f $(TEXFIGS) $(EPSFIGS) $(EPSGRAPHS) $(PDFGRAPHS)
	rm -f *.dvi *.aux *.log *.bbl *.blg *.lof *.lot *.toc *.bak
	rm -f *~ *.core core

always:
	@:

spell:
	for A in *.tex; do aspell -t -p ./aspell.words -c $$A; done
	for A in *.tex; do perl double.pl $$A; done

.PHONY: clean all always ignore xpdf
