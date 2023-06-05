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

## Editing Guide

### 1. Clone 

Clone local version of the repository. 
```
    git clone https://github.com/vicharak-in/vaaman-doc
    cd vaaman-doc
    git checkout main
```
or, if you already have a local copy
```
	cd path/to/vaaman-doc
    git fetch main
    git checkout origin/main
```

### 2. Make Changes 

Edit rst files in source/ directory. Learn about rst [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#restructuredtext-primer).

Create and enter the virtual environment.
```
    pipenv update
    pipenv shell 
```
Make your changes now and build/view them
```
    make html -j $(nproc)
    ${BROWSER} build/html/index.html
```
If satisfied, add+commit them
```
    git add <changed_files>
    git commit
```

### 3. Create a branch with your name

Create a branch with your name. If it already exists, omit the `-b` flag.
```
    git checkout -b <your_name>
```
and push your changes to this branch.
```
    git push -u origin HEAD:<your_name>
```

### 4. Create a pull request

#### With a web browser 
1. Go to https://github.com/vicharak-in/vaaman-doc > 
2. Click on pull request 
3. Click on the branch name you wish to commit
4. Create pull request

#### With `gh` cli


---

## Resources

- [sphinx doc](https://www.sphinx-doc.org/en/master/index.html)
- [rst primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#restructuredtext-primer)
- [rst cheatsheet](https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html)
- [Theme config](https://sphinxawesome.xyz)
