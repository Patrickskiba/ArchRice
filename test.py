from os import chdir
from subprocess import run

def run_cmd(commands):
    for cmd in commands:
        split_cmd = [ x for x in cmd.split(' ') ]
        print(split_cmd[0])
        if split_cmd[0] == 'cd':
            print(split_cmd[1])
            chdir(split_cmd[1])
            run(['pwd'])
        else:
            run(split_cmd)

