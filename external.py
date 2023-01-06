import os
import subprocess
import shlex

hello_world = "Hello world, from an external python script!"

def fetch_repo_license():
    #!wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/LICENSE -O LICENSE
    os.system('wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/LICENSE -O LICENSE')

def fetch_repo_readme():
    #!wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/README.md -O README.md
    os.system('wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/README.md -O README.md')

# https://www.endpointdev.com/blog/2015/01/getting-realtime-output-using-python/
def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc

def clone_a_repo():
    cmd = '"git" clone https://github.com/NUROISEA/stable-diffusion-webui.git'
    run_command(cmd)
    print("Done cloning")

def download_large_file():
    cmd = '"wget" https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0.ckpt'
    run_command(cmd)
    print("Done downloading")
