import os
from subprocess import Popen, PIPE, CalledProcessError

hello_world = "Hello world, from an external python script!"

def fetch_repo_license():
    #!wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/LICENSE -O LICENSE
    os.system('wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/LICENSE -O LICENSE')

def fetch_repo_readme():
    #!wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/README.md -O README.md
    os.system('wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/README.md -O README.md')

def continous_shell(cmd):
    with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        print(line, end='') # process line here

    if p.returncode != 0:
        raise CalledProcessError(p.returncode, p.args)

def clone_a_repo():
    cmd = 'git clone https://github.com/NUROISEA/stable-diffusion-webui.git'
    continous_shell(cmd)
    print("Done cloning")

def download_large_file():
    cmd = 'wget https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0.ckpt'
    continous_shell(cmd)
    print("Done downloading")
