import os
import requests
import subprocess

def createAutomaticFolderTree():
    project_name = input("Le nom du projet : ")
    directory = os.path.join(os.getcwd(), project_name)
    
    # Vérifier si le dossier n'existe pas déjà
    if os.path.exists(directory):
        print(f"Le dossier '{project_name}' existe déjà.")
        return None, None
    
    os.makedirs(directory)
    
    # Liste des dossiers à créer
    folders = ["data/raw", "data/cleaned", "docs",
               "models", "notebooks", "reports", "src"]

    # Liste des fichiers à créer
    files = ["LICENSE", "Makefile", "README.md", ".gitignore",
             "requirements.txt", "src/utils.py", "notebooks/main.ipynb"]

    for folder in folders:
        os.makedirs(os.path.join(directory, folder))

    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            file_content = ''
            f.write(file_content)
    
    return project_name, directory  # Retourner les valeurs

# Crée la structure de dossiers automatiquement
project_name, path = createAutomaticFolderTree()

def initLocalRepository(path):
    subprocess.run(["git", "init"], cwd=path)

def createRepository(repository_name, base_url="https://api.github.com"):
    access_token = input('Fournissez votre access token : ')
    data = {
        "name": repository_name,
        "description": "This is my new repository",
        "private": False
    }
    response = requests.post(f"{base_url}/user/repos", json=data, headers={
        "Authorization": f"Bearer {access_token}"
    })
    return response.json()['clone_url']

def add_remote(path, repos_url):
    subprocess.run(["git", "remote", "add", "origin", repos_url], cwd=path)

def add_into_local_repos(path, fileToAdd='.'):
    subprocess.run(["git", "add", fileToAdd], cwd=path)
    add_commit(path, f"Add new file {fileToAdd}")  # Ajout de cette ligne pour faire un commit

def add_commit(path, message=""):
    subprocess.run(["git", "commit", "-m", message], cwd=path)

def pushToRemote(path, branch="master"):
    subprocess.run(["git", "push", "-u", "origin", branch], cwd=path)

# Initialisation du référentiel local
initLocalRepository(path)

# Création du référentiel sur GitHub et récupération de l'URL de clonage
repos_url = createRepository(project_name)

# Ajout de tous les fichiers au référentiel local  
add_into_local_repos(path)

# Ajout du référentiel distant au référentiel local
add_remote(path, repos_url)

# Pousse les modifications vers le référentiel distant
pushToRemote(path)
