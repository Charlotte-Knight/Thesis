# Searching for direct and indirect signatures of new physics with measurements of the Higgs boson

##  LaTeX source code for my PhD thesis

The [pdf](thesis.pdf) is built with `./build.sh` which uses latexmk, lualatex, and biber, which may be available to you if you have latex installed on your system. If not, I recommend installing full [TeX Live](https://www.tug.org/texlive/). On Ubuntu systems, you will be able to do this with
```
sudo apt install texlive-full
```
or on Fedora
```
sudo dnf install texlive-scheme-full
```
and I trust you can figure this out if you are on a different operating system. The full TeX Live installation is probably excessive but is the easiest way to ensure you have all the tools and packages you need.

The initial build will take rather long because there are many tikz diagrams (mostly Feynman diagrams) that need to be drawn. 

Subsequent builds are much quicker because I use the tikz library *external* which creates pdfs for the diagrams in `tikz/` which are reused in future builds of the thesis. If you change the diagram in its corresponding `.tex` file, it should recreate the diagram.

To students who are writing their thesis and are here for inspiration, I highly recommend using vscode and the [LaTeX](https://marketplace.visualstudio.com/items?itemName=mathematic.vscode-latex) and [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extensions. You'll probably also want a spell-check tool such as [LTeX](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex). Note that spell checking is often not perfect when writing in LaTeX so do be careful.

If you do use the LaTeX Workshop extension, it can build the thesis for you instead of you running `./build.sh`. You can trigger this manually, or it automatically attempts this when saving a `.tex` file. The build 'recipe' is specified by the first line in [thesis.tex](thesis.tex#L1) but we have to tell LaTeX workshop what each step in the recipe means. This is done via the 'tools' setting for the extension. See [here](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-tools) for the extension docs. You will need to insert the following tools
```
{
  "name": "lualatexmk",
  "command": "latexmk",
  "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-lualatex",
      "-outdir=%OUTDIR%",
      "--shell-escape",
      "%DOC%"
  ],
  "env": {}
},
{
  "name": "biber",
  "command": "biber",
  "args": [
      "%DOCFILE%"
  ],
  "env": {}
}
```
where the lualatexmk entry may already exist but you should overwrite it. The default tool definition does not include `--shell-escape` which is needed for the tikz externalize library.