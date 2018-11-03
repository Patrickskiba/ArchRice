from subprocess import run

def run_cmd(commands):
    for cmd in commands:
        split_cmd = [ x for x in cmd.split(' ') ]
        run(split_cmd)
