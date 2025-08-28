# CLI Reverse shell generator
## inspired by [https://github.com/0dayCTF/reverse-shell-generator](https://github.com/0dayCTF/reverse-shell-generator)
---
## Requirements
```shell
# Linux package
xclip
# Python3 module
pyperclip
```
## Usage
```shell
cd /opt
sudo git clone https://github.com/umbrocker/revsheller.git
cd revsheller
sudo chmod 755 revshell.py
sudo ln -s /opt/revsheller/revshell.py /usr/local/bin/revsheller
revsheller
```
