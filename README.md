My Home Lab Configuration
=========================

This is a pyinfra project that configures my home lab such that I can
get a fresh set of baremetal and KVM machines with just a single command.


# Usage

This project doesn't add wrappers around pyinfra, so once you get the hang
of [how to use pyinfra](https://docs.pyinfra.com/en/1.x/getting_started.html),
then you can easily move on to some of the stuff I do in the `config/` dir
of this project. Basically, you can try them out via:

```
pyinfra inventory/pxe.py tasks/pxe/install.py
```


## Prerequisites

1. [Python 3](https://www.python.org/downloads/)
2. Make


## Prepare Your Python Environment (pyenv style; one-time only)

You will need two additional dependencies for this style:

1. [pyenv](https://github.com/pyenv/pyenv-installer)
2. [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Once the above dependencies are installed, do the following:

1. Install an isolated environment for your preferred Python version.

```
python_version=<YOUR-PREFERRED-PYTHON-VERSION>
pyenv install --enable-shared $python_version
```

NOTE: For more available versions, run `pyenv install --list`

2. Create a virtualenv for this project

```
pyenv virtualenv $python_version config-home-lab
```

3. Add a `.python-version` file to this project dir

```
cat >.python-version<<EOF
config-home-lab
$python_version
EOF
```

Your newly created virtualenv should now be automatically activated if your
prompt changed to the following:

```
(config-home-lab) ubuntu@dev...
```

or, should you happen to be using [dotfiles.relaxdiego.com](https://dotfiles.relaxdiego.com),
if it changed to the following

```
... via 🐍 <YOUR-PREFERRED-PYTHON-VERSION> (config-home-lab)
```
Notice the things in parentheses that corresponds to the virtualenv you created
in the previous step. This is thanks to the coordination of pyenv-virtualenv and
the `.python-version` file in the rootdir of this project.

If you `cd ..` or `cd` anywhere else outside your project directory, the virtualenv
will automatically be deactivated. When you `cd` back into the project dir, the
virtualenv will automatically be activated.


## Prepare Your Python Environment (venv style)

If you'd rather manage your virtualenv manually, this section is for you.
Create your virtual environment:

```
python3 -m venv ./venv
```

Activate it in every shell session where you intend to run make or
the unit tests

```
source ./venv/bin/activate
```


## Install The Dependencies

Install all development and runtime dependencies.

WARNING: Make sure you are using a virtualenv before running this command. Since it
         uses pip-sync to install dependencies, it will remove any package that is not
         listed in `setup.py`. If you followed the steps in any of the Prepare Your
         Development Environment sections above, then you should be in good shape.

```
make dependencies
```


## Adding A Dependency

1. Add it to the `runtime_requirements` list in setup.py and then run:

```
make dependencies
```

This will create `requirements.txt` and then install all dependencies


2. Commit `setup.py` to let your teammates know of the new dependency.

```
git add setup.py
git commit -m "Add bar to requirements"
git push origin
```


## Other Make Goals

Run `make help` or check out the contents of `Makefile`.


# References

* [SecureBoot-Compatible UEFI netboot](https://wiki.ubuntu.com/UEFI/SecureBoot/PXE-IPv6)
* [dnsmasq](https://wiki.archlinux.org/index.php/dnsmasq#Configuration)
* [Fully Automated Ubuntu 20.04 Install](https://askubuntu.com/a/1235724)
* [Configuring PXE Network Boot Server on Ubuntu 18.04 LTS](https://linuxhint.com/pxe_boot_ubuntu_server/)
* [Ubuntu Network installation with PXE](https://xinau.ch/notes/ubuntu-network-installation-with-pxe/)
