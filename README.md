La description complete du mode de fonctionnement de l'application avec les 8 fonctions et leurs roles
1-)Création d'une structure d'arborescence automatique :
L'utilisateur est invité à fournir le nom du projet.
Le programme crée un dossier avec ce nom dans le répertoire de travail actuel (où se trouve le script).
Il vérifie si le dossier existe déjà. Si c'est le cas, il affiche un message indiquant que le dossier existe et arrête le processus. Sinon, il crée la structure d'arborescence 
2-)Initialisation du référentiel local avec Git :
Le programme utilise la commande git init pour initialiser un référentiel Git local dans le dossier du projet
3-)Création d'un référentiel sur GitHub :
L'utilisateur est invité à fournir son access token pour l'authentification.
Le programme envoie une requête POST à l'API GitHub pour créer un nouveau référentiel pour l'utilisateur.
Le nom du référentiel est celui fourni par l'utilisateur.
Le programme reçoit l'URL de clonage du nouveau référentiel
4-)Ajout de fichiers au référentiel local:
Les fichiers nouvellement créés dans la structure d'arborescence sont ajoutés au référentiel Git local en utilisant la commande git add. 
5-)Effectuer un commit au référentiel local :cette fonction permet de faire de commit après chaque ajout de new file or folder
6-)Effectuer un commit au référentiel local :
Le programme effectue un commit avec un message passé en argument ou par défaut.
Le programme utilise la commande git commit -m pour enregistrer les modifications.
7-)Ajout du référentiel distant au référentiel local:cette fonction nous permet d'ajouter le référentiel distant (GitHub) comme une "remote" nommée "origin" en utilisant la commande git remote add
8-)Pousser les modifications vers le référentiel distant :
Le programme utilise la commande git push pour pousser les modifications locales vers le référentiel distant (GitHub).
