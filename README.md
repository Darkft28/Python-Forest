✨ Simulation d'Incendie de Forêt ✨

Bienvenue dans ce projet de simulation d'incendie de forêt ! 🌳🔥 Ce programme modélise la propagation du feu à travers une forêt en utilisant une grille bidimensionnelle.

📚 Description du Projet

Ce projet simule un incendie de forêt sur une grille de taille personnalisable. Chaque case représente un
élément de la forêt qui peut être un arbre, un rocher, un feu, ou un arbre brûlé.

📊 Règles de propagation :

🌲 Un arbre (“1” 🌳) peut prendre feu s'il est adjacent à un arbre en feu.

🔥 Un arbre en feu (“2” 🔥) devient un arbre brûlé (“3” 🕸️) au tour suivant.

⛰️ Une montagne (“0”) est ininflammable.

♻️ La simulation s'arrête lorsque plus aucun arbre n'est en feu.

🔧 Installation et Exécution

Cloner le dépôt :

git clone https://github.com/votre-repo.git
cd votre-repo

Exécuter le programme :

python3 simulation.py

Entrer les paramètres :

Taille de la forêt (ex : 10 pour une grille 10x10)

Probabilité de présence d'un arbre (ex : 0.6 pour 60%)

📈 Exemple de Simulation

Entrée :

Entrez la taille de la forêt: 5
Entrez la probabilité de présence d'un arbre (entre 0 et 1): 0.7

Sortie (affichage de la forêt à chaque étape) :

Étape 0:
🌳 ⛰️ 🌳 🌳 ⛰️
🌳 🌳 🔥 🌳 🌳
🌳 ⛰️ 🌳 🌳 🌳
...
La forêt a brûlé en X itérations.

🌟 Fonctionnalités

🏢 Génération aléatoire d'une forêt avec des arbres et montagnes

🔥 Propagation dynamique du feu

📈 Affichage étape par étape de l'évolution du feu

♻️ Arrêt automatique lorsque le feu s'est éteint

🌟 Améliorations Possibles

📊 Ajouter un vent influençant la propagation

💧 Ajouter la possibilité d'arroser certaines zones

🛡️ Ajouter un pare-feu ralentissant la propagation

📢 Auteurs

Ce projet a été réalisé par Darkft28.
N'hésitez pas à contribuer ou à poser des questions ! ✨



Bon courage avec votre forêt ! 🌳🔥
