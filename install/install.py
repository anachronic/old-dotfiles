#!/usr/bin/python3

# This file will create any symlink to make this directory work

import os
import os.path
import pathlib
import shutil


def get_dotfiles_dir():
    curpath = os.getcwd()
    dotfiles = str(pathlib.Path(curpath).parent)

    return dotfiles


def install(source, destination):
    source = os.path.expanduser(source)
    dest = os.path.expanduser(destination)

    if os.path.exists(dest):
        print("[SKIPPING]: {} already exists in the file system".format(dest))
        return

    os.symlink(source, dest)
    print("Created symlink: {}".format(dest))


def copy_binaries():
    dotfiles = get_dotfiles_dir()

    local_bin = os.path.expanduser("~/.local/bin")
    if not os.path.exists(local_bin):
        os.makedirs(local_bin)

    dotfiles_bin = os.path.join(dotfiles, "bin")

    for file in os.listdir(dotfiles_bin):
        dest_path = os.path.join(local_bin, file)
        source_path = os.path.join(dotfiles_bin, file)

        if not os.path.exists(dest_path):
            shutil.copyfile(source_path, dest_path)
            print("Copied: {} to {}".format(file, dest_path))
        else:
            print("[SKIPPING]: {} already exists in the file system".format(
                dest_path))


if __name__ == '__main__':
    dotfiles = get_dotfiles_dir()

    home = os.path.expanduser("~")

    files = (".Xresources", ".Xmodmap", ".tmux.conf", ".xinitrc", ".zshrc",
             ".vim", ".offlineimaprc", ".offlineimap.py")

    for file in files:
        source = os.path.join(dotfiles, file)
        destination = os.path.join(home, file)

        install(source, destination)

    # now binaries
    copy_binaries()
