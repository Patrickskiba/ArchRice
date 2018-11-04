import json
from subprocess import run
from test import run_cmd

with open('programs.json', 'r') as f:
    programs = json.load(f)

pacman_progs = {k for k, v in programs.items() if v["source"] == "pacman"}

aur_progs = {k for k, v in programs.items() if v["source"] == "aur"}

install_yaourt = [
        'git clone https://aur.archlinux.org/package-query.git',
        'cd package-query',
        'makepkg -si',
        'cd ../',
        'git clone https://aur.archlinux.org/yaourt.git',
        'cd yaourt',
        'makepkg -si',
        'cd ../',
        'sudo rm -dR yaourt package-query',
        'sudo pacman -Sy yaourt',
        ]

install_dotfiles = [
        'cd ~/'
        'git init'
        'git remote add origin https://github.com/Patrickskiba/dotfiles',
        'git fetch',
        'git checkout -t origin/master'
        ]

run(['sudo', 'pacman', '-S', '--needed', '--noconfirm', *pacman_progs])

run_cmd(install_yaourt)

run(['yaourt', '-S', '--needed', '--noconfirm', *aur_progs])

run_cmd(install_dotfiles)
