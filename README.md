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

Taking in consideration that there exists a maintainer of each major section
of this documentation repository.

For example a person dedicated for `linux kernel` should not commit changes for the section that is not `linux kernel`.
If the changes are important then instead create a **patch** for the changes and send that patch over to the designated maintainer to pick and merge on his/her branch.

This will allow this repository to be conflictless and easy to maintain.

### 1. Cloning the repository

Clone the fresh copy of this repository.
```
git clone https://github.com/vicharak-in/vaaman-doc -b main && cd vaaman-doc
```

If there already exists a local clone then do this instead
```
cd path/to/vaaman-doc
git fetch origin main
```

### 2. Modifying and updating the source

Edit rst files in source/ directory as per your requirements and changes.

**Learn about rst** [**here**](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#restructuredtext-primer).

**Always make sure to compile the source before commiting**

Create the virtual environment and build the source with your changes.
```
pipenv update
pipenv shell make html -j $(nproc --all)
```

View the updated documentation site on your local computer using
```
${BROWSER} build/html/index.html
```

If the changes are satisfied then, ==git add + commit== them
```
git add <changed_files>
git commit
```

### 3. Pushing the modifications

If your branch doesn't exists then the first step will be to create your new dedicated branch.

To create a new branch use following command.
```
git checkout -b <your_name>
```
Example: `git checkout -b utsav`

Confirm the branch using `git branch -a`.

If your branch already exists then directly push your changes over to your branch.
```
    git push -u origin HEAD:<your_name>
```
Example: `git push origin HEAD:utsav`

### 4. Creating pull request for your modifications

Pull requests are requried in order to review the modifications that the developers are doing.
Reviewing can include typo/spelling errors, indentation errors, compilation errors, etc.

**Creating pull request using web browser**

1. Go to https://github.com/vicharak-in/vaaman-doc
2. Click on pull request
3. Click on the branch name you wish to commit
4. Create pull request

**Creating pull request using `gh` cli**

```
gh pr create -R https://github.com/vicharak-in/vaaman-doc
```

---

## Resources for reading

- [sphinx doc](https://www.sphinx-doc.org/en/master/index.html)
- [rst primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#restructuredtext-primer)
- [rst cheatsheet](https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html)
- [Theme config](https://sphinxawesome.xyz)
