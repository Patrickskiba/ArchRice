import json
from subprocess import run


with open('programs.json', 'r') as f:
    programs = json.load(f)

pacman_progs = {k for k, v in programs.items() if v["source"] == "pacman"}

run(['sudo', 'echo', '-S', '--needed', '--noconfirm', *pacman_progs])

if not '[archlinuxfr]\nSigLevel = Never\nServer = http://repo.archlinux.fr/$arch' in open('/etc/pacman.conf').read():
    with open("/etc/pacman.conf", "a") as myfile:
        myfile.write("[archlinuxfr]\nSigLevel = Never\nServer = http://repo.archlinux.fr/$arch")

    run(['sudo', 'pacman', '-Sy', 'yaourt'])


aur_progs = {k for k, v in programs.items() if v["source"] == "aur"}
run(['yaourt', '-S', '--needed', '--noconfirm', *aur_progs])
