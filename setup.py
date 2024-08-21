import subprocess

with open("commands.txt", "r") as fh:
    cmds = fh.readlines()
    for item in cmds:
        subprocess.run(item.split(" "))
