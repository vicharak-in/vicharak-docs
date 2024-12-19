# How to edit or modify the docs

## Cloning the repository

Clone the fresh copy of this repository.
```
git clone https://github.com/vicharak-in/vicharak-docs -b main
cd vicharak-docs
```

If there already exists a local clone then do this instead
```
cd <path/to/vicharak-docs>
git fetch origin main
git checkout FETCH_HEAD
```

## Modifying and updating the source

Create or edit `.rst` files in **source/** directory as per your requirements and changes.

**Learn about rst** [**here**](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#restructuredtext-primer).

**Always make sure to compile the source before committing**

Create the virtual environment and build the source with your changes.
Make sure you have followed the INSTALLATION guide for python environment setup.

**For Linux users**
```bash
pipenv update
pipenv shell make html -j $(nproc --all)
```

**For Windows users**
```bash
python -m pipenv update
python -m pipenv shell ./make.bat html
```

## View the updated documentation

### View the compiled source on your local computer using

**For Linux users**
```bash
${BROWSER} _build/html/index.html
```

> :warning: **Replace ${BROWSER} with your browser name.**\
> Example: `firefox _build/html/index.html`

**For Windows users**

1. Open the repository in file explorer.
2. Enter the `_build/html` folder
3. Open the `index.html` file in any web browser.

**If the changes are satifactory then, commit your local changes.**

```bash
git add source/
git commit
```

**While committing make sure to write a well described commit message and commit title.**

Some examples on how to write good commit messages:

Good:
```
vicharak-docs: Introduce documentation for fgpa write.
README: Add usage documentation for windows users.
vicharak-docs: linux: Document different vaaman kernel revisions.
```

Bad:
```
add doc
update readme
```

**To check the list of modified files:**
```bash
git status
```

## Use spellchecker to find mistakes in your changes

Read the [Spellchecker Guide](./SPELLING.md)

## Pushing the modifications to GitHub

1. Create a fork of the doc repository
2. [Add this repository as a
   remote](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories)
3. Push changes to your remote

## Creating pull request for your modifications

Pull requests are required in order to review the modifications that the developers are doing.
Reviewing can include typo/spelling errors, indentation errors, compilation errors, etc.

Refer to [Creating a pull
request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
for the steps to follow. 

Make sure base branch in the PR is `main`
