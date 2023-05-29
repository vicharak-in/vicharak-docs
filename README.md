# Vicharak Vaaman Documentation

reStructuredText/Markdown preferred documentation, generated using [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

---

## Prerequisites

**Installing Python and Python pipenv packages**

**ArchLinux based distributions**
```bash
sudo pacman -S python python-pip python-pipenv
```

**Ubuntu/Debian based distributions**
```bash
sudo apt install -y python3 python3-pip python3-pipenv
```

---

## How to compile and visualize

1. **Update your python pipenv**

```bash
pipenv update
```

2. **Enter the virtual pipenv shell**
```bash
pipenv shell
```

3. **Compile the source files and view it on browser**
```bash
make html -j$(nproc --all)
${BROWSER} build/html/index.html
```
---

## Edit

`source/index.rst` is the index file, it contains the table of content.
Open index.html and index.rst side-by-side and compare for better understanding.

---

## Resources

- [sphinx doc](https://www.sphinx-doc.org/en/master/index.html)
- [rst primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#restructuredtext-primer)
- [rst cheatsheet](https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html)
- [Theme config](https://sphinxawesome.xyz)
