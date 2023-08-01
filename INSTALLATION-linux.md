## Prerequisites

### Installing Python and Python pipenv packages

**ArchLinux based distributions**
```bash
sudo pacman -S python python-pip python-pipenv enchant aspell nuspell voikko hspell
```

**Ubuntu/Debian based distributions**
```bash
sudo apt install -y python3 python3-pip libenchant-2-dev libenchant-2-voikko aspell nuspell hspell
```

### Install pipenv using pip

For installing `pipenv` on your system use the following command.

> :warning: Not required for ArchLinux

```bash
pip install pipenv
```

### Install the dependencies inside python virtual environment

Use following command to setup python virtual environment for building **vaaman-doc**.
```bash
pipenv update
```

### Enter the python virtual environment

Use following command to enter python virtual environment.
```bash
pipenv shell
```

---

After successfully following the setup you have proper environment setup to build vaaman-doc.

Follow the [Editing Guide](./EDITING.md) for more information.
