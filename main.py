import json
from subprocess import run


with open('programs.json', 'r') as f:
    programs = json.load(f)

pacman_progs = {k for k, v in programs.items() if v["source"] == "pacman"}

run(['sudo', 'pacman', '-S', '--needed', '--noconfirm', *pacman_progs])

run(['git', 'clone', 'https://aur.archlinux.org/package-query.git'])

run(['cd', 'package-query'])

run(['makepkg', '-si'])

run(['cd', '-'])

run(['git', 'clone', 'https://aur.archlinux.org/yaourt.git'])

run(['cd', 'yaourt'])

run(['makepkg', '-si'])

run(['cd', '-'])

run(['sudo', 'rm', 'dR', 'yaourt/', 'package-query/'])

run(['sudo', 'pacman', '-Sy', 'yaourt'])


aur_progs = {k for k, v in programs.items() if v["source"] == "aur"}
run(['yaourt', '-S', '--needed', '--noconfirm', *aur_progs])
