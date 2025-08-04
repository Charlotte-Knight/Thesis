# PDF/A compliance

As part of your thesis submission process, you may be asked to convert your PDF such that it meets a special archiving standard called PDF/A. The standard requires all fonts to be embedded, meaning that they are part of the PDF itself and no assumption is made about which fonts are available on the system that a reader is viewing your PDF on. There are also some requirements on colour management and maybe other things which I do not understand. The point is that you may have to do the conversion, and it will likely be a pain. Luckily for you, I have gone through the pain first and have written some instructions below to hopefully ease your pain. I include specific commands to use if you're on Linux, specifically ubuntu. First thing you should do is `cd PDFA` where we will keep things all things PDF/A-related.

First thing you should do is find out which particular PDF/A standard you have been asked to adhere to. In my case, I needed to adhere to PDF/A-2B.

## Verapdf

Second thing you should do is install software that checks your PDF's conformance to the standard. I recommend [verapdf](https://verapdf.org/software/). It's available on Windows, Mac, and Linux. Download it and unzip:
```
curl -O https://software.verapdf.org/rel/verapdf-installer.zip && unzip verapdf-installer.zip
```
To install it, you first need Java Runtime Environment (JRE), which you can install with
```
sudo apt install default-jre
```
and then to install verapdf, do
```
mkdir verapdf
./verapdf-*/verapdf-install
```
This will bring up a GUI. When it asks where to install verapdf, choose the directory we just made (`Thesis/PDFA/verapdf`).

You can use verapdf via its GUI with `./verapdf/verapdf-gui` or via the command line with commands like
```
./verapdf/verapdf -f 2b --format text -v ../thesis.pdf
```
Note, the verification can take a minute to complete. The particular PDF/A standard is specified with the `-f` option which in this case is set to `2b` for PDF/A-2B. On a first run-through, it will almost definitely tell you that your PDF has failed the verification, and you'll get an output like this
```
FAIL /home/charlotteknight/Documents/ThesisPublic/Thesis/PDFA/../thesis.pdf 2b
  FAIL 6.1.13-3
  FAIL 6.2.4.3-3
  FAIL 6.2.5-1
  FAIL 6.2.11.8-1
  FAIL 6.2.11.5-1
  FAIL 6.2.11.3.2-1
  FAIL 6.2.11.4.1-1
```
You can get most detailed information by creating a HTML file:
```
./verapdf/verapdf -f 2b --format html -v ../thesis.pdf > verapdf.html
```
and opening `verapdf.html` in a browser. Tip: you can open the HTML with your default browser with `xdg-open verapdf.html` and this works with open types of files too.

## Converting to PDF/A standard

Now that you know your PDF is not PDF/A compliant, we need to fix that. In my experience, it takes several steps to get the PDF to conform. If you want, you can try skipping to the very last step which would be [pdftools](#pdftools) or [Adobe Acrobat Pro](#adobe-acrobat-pro-if-all-else-fails). However, I have a feeling that this will be more brute-force and the conversion might not be as nice as you'd like, e.g. broken hyperlinks. 

### pdfx LateX package

First thing I did was use the `pdfx` LaTeX package. This required two changes, to insert `\usepackage[a-2b]{pdfx}` at the beginning of [thesis.sty](../thesis.sty), and to replace `\usepackage[hidelinks]{hyperref}` with `\hypersetup{hidelinks}` (also in [thesis.sty](../thesis.sty)). 

I also created [thesis.xmp](thesis.xmp) to insert metadata like the author, abstract and keywords into the pdf which is recommended for the PDF/A standard but is not enforced, at least I don't think it is by `verapdf`. You can see the inserted metapdf by looking at the PDF's properties via your file explorer or a pdf viewer. The ghostscipt step (see later in instructions) actually removes some of this metadata :(. If you can find a way around this, please let me know so I can update the instructions. 

This will not create a completely-PDF/A compliant document. My understanding is that no changes are made to the PDFs that are inserted as figures, i.e. via `\includegraphics` which is why we have to do a bit more work. The most obvious way it's probably noncompliant is via a lack of font embedding. You can check this with
```
pdffonts ../thesis.pdf
```
which will produce an output like
```
name                                 type              encoding         emb sub uni object ID
------------------------------------ ----------------- ---------------- --- --- --- ---------
MDBPDQ+LMRoman12-Bold                CID Type 0C       Identity-H       yes yes yes    369  0
UJGYFO+LMRoman10-Regular             CID Type 0C       Identity-H       yes yes yes    370  0
JHFKST+CMR10                         Type 1            Builtin          yes yes yes    376  0
YATPOX+CMMI10                        Type 1            Builtin          yes yes yes    377  0
GHCFQC+CMR8                          Type 1            Builtin          yes yes yes    378  0
CSFPDX+CMSY8                         Type 1            Builtin          yes yes yes    379  0
AGSXMD+CMMI8                         Type 1            Builtin          yes yes yes    380  0
KOLJTR+LMRoman10-Bold                CID Type 0C       Identity-H       yes yes yes    444  0
.
.
.
```
where you'll find fonts which have "no" under the "emb" (embedded) column. In this example, the first 7 fonts were correctly embedded but I did find others that were not much further down the list.

### Ghostscript

Next step is to use ghostscript to embed all those fonts and to try force other types of compliance, though I am not sure if it does anything more than embed the fonts properly. You can install ghostscript with
```
sudo apt install ghostscript
```
and then the conversion command is
```
gs -dPDFA=2 -dBATCH -dNOPAUSE -sProcessColorModel=DeviceCMYK -sDEVICE=pdfwrite -sPDFACompatibilityPolicy=1 -dEmbedAllFonts=true -dSubsetFonts=true -dPDFSETTINGS=/prepress -sOutputFile=thesis_ghostscript.pdf ../thesis.pdf
```

At this stage, it's worth checking whether you have a compliant PDF
```
./verapdf/verapdf -f 2b --format text -v thesis_ghostscript.pdf
```
In my case, it is still not compliant.

### Pdftools

The (hopefully) final step is to use the pdftools SDK to fix any remaining issues. You can see these (sorta) [docs](https://www.pdf-tools.com/docs/other-shell-tools-and-sdks/pdf-pdfa-converter/) if you'd like. We will use the [validate_convert.py](validate_convert.py) python script to do the conversion. You may find a more up-to-date version via the [docs](https://www.pdf-tools.com/docs/other-shell-tools-and-sdks/pdf-pdfa-converter/). 

To run the script, you'll need to install the sdk:
```
pip install pdftools_sdk
```
and then do
```
python ./validate_convert.py thesis_ghostscript.pdf thesis_pdfa.pdf
```
and check compliance again
```
./verapdf/verapdf -f 2b --format text -v thesis_pdfa.pdf
```
which for me, returned
```
PASS /home/charlotteknight/Documents/ThesisPublic/Thesis/PDFA/thesis_pdfa.pdf 2b
```
meaning that my PDF passed the PDF/A-2b standard! 

Note, this conversion script is meant for PDF/A-2B. I leave it to you to find the equivalent for a different standard.

By default, this script uses a test licence for the pdftools sdk and as such, leaves a watermark on your pdf. Luckily, you can get a free licence for pdftools sdk. Go to [https://www.pdf-tools.com/](https://www.pdf-tools.com/) and get a free pdftools SDK licence. Copy the licence key and follow the instructions in [validate_convert.py](validate_convert.py#L89) to use it. **Note, the free version may only give you one or two chances to convert the PDF without the watermark, so do not do this until the verification is working. You may also want to check the PDF thoroughly with the test licence to make sure there aren't any weird artefacts.**

You can compare two pdfs with online tools, or with [diffpdf](https://manpages.ubuntu.com/manpages/trusty/man1/diffpdf.1.html) which you can install with
```
sudo apt install diffpdf
```
In the top-right of the diffpdf application, you can choose between comparing the "Appearance", "Characters", or "Words". In a sense, each one is more sensitive than the last. For a final check, I recommend using the "Appearance" since it should pick up any differences in figures too.

Some PDF figures may look weird and if that's the case, I recommend converting them to PNG and inserting them that way instead. This will mean recompliling your thesis and redoing the steps above. You can convert PDF to PNG in the command line with
```
pdftoppm -png -r 300 figure.pdf > figure.png
```
Here, the `-r` option corresponds to the resolution in DPI. If the PNG looks too blurry, increase this number. You may need to install ImageMagick for this command to work:
```
sudo apt install imagemagick
```

### Adobe Acrobat Pro (if all else fails)

If after all that, you still do not have a PDF/A compliant document, I recommend getting a free trial of Adobe Acrobat Pro and using that to convert to PDF/A. Adobe have their own instructions for that [here](https://www.adobe.com/acrobat/hub/how-to-convert-pdf-to-pdfa.html#:~:text=PDF%2FA%20is%20best%20used,%2C%20scanned%20documents%2C%20and%20spreadsheets.). I recommend using Acrobat Pro to convert the output from ghostscript. This is actually what I did for my thesis submission. I only discovered the pdftools converter afterwards.

Adobe Acrobat only has Windows and Mac versions. If you're running Linux, I recommend finding a Windows machine, or setting up a Windows virtual machine. You can find instructions for that on Google. Good luck.