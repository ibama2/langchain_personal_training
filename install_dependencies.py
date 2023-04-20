import subprocess

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

for requirement in requirements:
    subprocess.call(['pip', 'install', requirement])
