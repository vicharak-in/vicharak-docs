# Vicharak Vaaman Documentation

reStructuredText/Markdown preferred documentation, generated using [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html).


## Prerequisites

**ArchLinux based distributions**
```bash
sudo pacman -S python python-pip python-sphinx python-breathe
```

**Ubuntu/Debian based distributions**
```bash
sudo apt install -y python3 python3-pip python3-sphinx python3-breathe
```


## How to compile and visualize

```bash
pip install sphinxawesome-theme --pre
make html -j$(nproc --all)
${BROWSER} build/html/index.html
```


## Edit

`source/index.rst` is the index file, it contains the table of content. Open
index.html and index.rst side-by-side and compare for better understanding.


## Resources

- [sphinx doc](https://www.sphinx-doc.org/en/master/index.html)
- [rst primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#restructuredtext-primer)
- [rst cheatsheet](https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html)
- [Theme config](https://sphinxawesome.xyz)
