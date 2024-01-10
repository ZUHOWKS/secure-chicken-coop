# Secure Chicken Coop
Ce projet vise à créer un alogrithme capable de contrôler les composants électroniques du le Raspberry Pi couplés avec la puissance d'une intélligence artificielle. 
L'exploitation de la force de cette IA (Chicken Detection) nous permet, à l'aide de la Raspberry Pi Camera V2, efficacement d'identifier la présence
d'un élèment en mouvement.

---
## Pré-requis

Le **SCC** (**S**ecure **C**hicken **C**oop) demande l'utilisation d'un ___Raspberry Pi minium de version 3___. Il demande aussi l'utilisation de la ___Raspberry Pi Camera V2___,
d'un ___capteur de mouvement___ (connecté au port **GPIO 22**) et d'un ___électro-aimant___ (5V 500mA maximum) (port **GPIO 17**).

## Environnement Virtuel

Ce programme nécessite la configuration d'un environnement virtuel python intégrant la librairie **Roblow** ainsi que toutes ses dépendances. 
Cepdandant, il faut aussi installer sur l'environnement python native les librairies **picamera2** et **RPi.GPIO**.

---

# Execution

Utiliser le script scc_start.sh ci-dessous pour le bon fonctionnement du programme:
```sh
cd
source py-secure-chicken-coop/bin/activate # Virtual Python Environnement
cd file/path/to/secure-chicken-coop/
python3 src/main.py
```
