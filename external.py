hello_world = "Hello world, from an external python script!"



def fetch_repo_license:
    !wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/LICENSE -O LICENSE

def fetch_repo_readme:
    !wget https://github.com/NUROISEA/dumb-colab-tests/raw/main/README.md -O README.md

