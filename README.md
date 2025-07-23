# Searching for direct and indirect signatures of new physics with measurements of the Higgs boson

##  LaTeX source code for my PhD thesis

The [pdf](thesis.pdf) is built with `./build.sh` which uses lualatex and biber, both of which are probably available to you if you have latex installed on your system. If not, I recommend installing [TeX Live](https://www.tug.org/texlive/). On most Linux systems, you will be able to do this with
```
sudo apt install texlive
```
or
```
sudo dnf install texlive
```
and you may want to install `texlive-full` to ensure all dependencies are available. 

The initial build will take rather long because there are many tikz diagrams (mostly Feynman diagrams) that need to be drawn. 

Subsequent builds are much quicker because I use the tikz library *external* which creates pdfs for the diagrams in `tikz/` which are reused in future builds on the thesis. If you change the diagram in its corresponding `.tex` file, it should recreate the diagram.

To students who are writing their thesis and are here for inspiration, I highly recommend using vscode and the [LaTeX](https://marketplace.visualstudio.com/items?itemName=mathematic.vscode-latex) and [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extensions. You'll probably also want a spell-check tool such as [LTeX](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex). Note that spell checking is often not perfect when writing in LaTeX so do be careful.