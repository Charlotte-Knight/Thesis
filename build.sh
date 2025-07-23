latexmk -synctex=1 -interaction=nonstopmode -file-line-error -lualatex --shell-escape thesis.tex
biber thesis
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -lualatex --shell-escape thesis.tex
