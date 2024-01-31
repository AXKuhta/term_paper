Template from https://github.com/KernelA/xelatex-gost-bac

Building:

```
sudo apt install texlive-full
sudo apt install fonts-liberation2
latexmk -verbose -xelatex -latexoption='-halt-on-error -enable-etex -enable-installer' ./Example.tex
```
