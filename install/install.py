#!/usr/bin/python3

# This file will create any symlink to make this directory work

import os
import os.path
import pathlib


def install(source, destination):
    source = os.path.expanduser(source)
    dest = os.path.expanduser(destination)

    if os.path.exists(dest):
        print(
            "[SKIPPING]: {} already exists in the file system".format(dest))
        return

    os.symlink(source, dest)
    print("Created symlink: {}".format(dest))


if __name__ == '__main__':
    curpath = os.getcwd()
    dotfiles = str(pathlib.Path(curpath).parent)

    home = os.path.expanduser("~")

    files = (".Xresources",
             ".tmux.conf",
             ".xinitrc",
             ".zshrc",
             ".vim")

    for file in files:
        source = os.path.join(dotfiles, file)
        destination = os.path.join(home, file)

        install(source, destination)
