# Maison Intelligente basé sur Protocol de XAAL
## Introduction
Ce projet IoT met en œuvre un système de contrôle simple pour une "maison intelligente". Le projet est implémenté par le SDK Python du protocole XAAL et comprend quatre scénarios.
## Installation et Lancement
1. Téléchargez d'abord le code source du projet :
```
git clone https://github.com/YinTAN-Stan/XAAL_TP.git
```
2. Installez l'environnement virtuel et la bibliothèque python de XAAL en suivant les instructions sur https://redmine.telecom-bretagne.eu/svn/xaal/code/Python/branches/0.7/README.html
3. Exécutez le Terminal (ou CMD) dans le répertoire racine du projet, activez l'environnement virtuel avec la bibliothèque XAAL installée, puis exécutez la commande pour lancer le projet: 
```
python smart_home.py
```
## Scénarios
1. **Contrôle automatique de l'éclairage de la cuisine**: Lorsque vous entrez dans la cuisine, le capteur détecte votre présence et l'éclairage de la cuisine s'allume. Lorsque vous quittez la cuisine, le capteur détectera également votre départ et la lumière de la cuisine s'éteindra après un délai de 5 secondes.
2. **Contrôle automatique de la lumière de la salle de bain**: Lorsque vous entrez dans la zone de la salle de bain, le capteur détecte votre présence et la lumière de la salle de bain s'allume. Lorsque vous quittez la salle de bain, le capteur détectera également votre départ et la lumière de la salle de bain s'éteindra après un délai de 5 secondes.
3. **Contrôle automatique du téléviseur**: Lorsque vous êtes assis sur le canapé du salon, le capteur de pression enverra un signal spécifique et le système allumera le téléviseur du salon après avoir reçu le signal. Lorsque vous vous levez du canapé, le téléviseur s'éteint après un délai de 5 secondes.
4. **Contrôle automatique des volets**: Lorsque vous vous allongez sur le lit, le capteur de pression enverra un signal spécifique et le système fermera les volets après avoir reçu le signal. Lorsque vous quittez le lit, les volets s'ouvrent après un délai de 10 secondes.
