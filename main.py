import json
from subprocess import run
from test import run_cmd

with open('programs.json', 'r') as f:
    programs = json.load(f)

pacman_progs = {k for k, v in programs.items() if v["source"] == "pacman"}

aur_progs = {k for k, v in programs.items() if v["source"] == "aur"}

commands = [
    f'sudo pacman -S --needed --noconfirm {*pacman_progs}',
    'git clone https://aur.archlinux.org/package-query.git',
    'cd package-query',
    'makepkg -si',
    'cd -',
    'git clone https://aur.archlinux.org/yaourt.git',
    'cd  yaourt',
    'makepkg -si',
    'cd -',
    'sudo rm -dR yaourt package-query',
    'sudo pacman -Sy yaourt',
    f'yaourt -S --needed --noconfirm {*aur_progs}',
    ]

run_cmd(commands)
