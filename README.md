# Thermomètre

Ce projet contient deux versions d'une application de thermomètre simple, `thermometerV1` et `thermometerV2`.

## Sommaire
- [Structure du projet](#structure-du-projet)
    - [thermometerV1](#thermometerv1)
    - [thermometerV2](#thermometerv2)
- [Requirements](#requirements)
    - [Python](#python)
    - [pip](#pip)
    - [tkinter](#tkinter)
- [Installation](#installation)
- [Exécution](#exécution)

## Structure du projet

Le projet a la structure suivante :

### thermometerV1

La première version de l'application est contenue dans le dossier `thermometerV1`. Elle contient un seul fichier, `application.py`, qui définit une classe `Application`. Cette classe gère l'interface utilisateur et la logique de l'application.

L'application permet d'augmenter et de diminuer une température, et de la convertir entre les degrés Celsius et Fahrenheit.

### thermometerV2

La deuxième version de l'application est contenue dans le dossier `thermometerV2`. Elle suit le modèle MVC (Modèle-Vue-Contrôleur) et contient quatre fichiers :

- `application.py` : Crée et gère l'application.
- `controller.py` : Contient la classe `Controller` qui gère la logique de l'application.
- `model.py` : Contient la classe `Model` qui gère les données de l'application.
- `view.py` : Contient la classe `View` qui gère l'interface utilisateur de l'application.

Cette version de l'application permet également d'augmenter et de diminuer une température, et de la convertir entre les degrés Celsius, Fahrenheit et Kelvin.

## Requirements

### Python

**Windows** (binaires): [Télécharger Python](https://www.python.org/downloads/)

**Windows** (Chocolatey) : 
```ps1
choco install python
```

**Windows** (Scoop) : 
```ps1
scoop install python
```

**Windows** (WinGet) : 
```ps1
winget install python
```

Utilisateurs de **MacOS Homebrew** : 
```bash
brew install python
```

Utilisateurs de **MacPorts** : 
```bash
sudo port install python38
```

**Debian/Ubuntu** : 
```bash
sudo apt update
sudo apt install python3
```

**Arch Linux** (pacman) : 
```bash
sudo pacman -S python
```

**Gentoo** : 
```bash
sudo emerge --ask dev-lang/python
```

**Fedora** : 
```bash
sudo dnf install python3
```

**openSUSE** :
```bash
sudo zypper install python3
```

### pip

Vous pouvez aller sur [le site officiel de pip](https://pip.pypa.io/en/stable/installation/) pour installer pip.

### tkinter

pip :
```bash
pip install tk
```

Debian/Ubuntu ([PEP 668](https://peps.python.org/pep-0668/)) :
```bash
sudo apt-get install python3-tk
```


## Installation

Pour installer l'application, clonez le dépôt sur votre machine locale :

```bash
git clone https://github.com/Illumye/thermometer.git
```

## Exécution

Pour exécuter l'application, ouvrez un terminal et exécutez les commandes suivantes :

```bash
cd thermometer/thermometerV1
python3 application.py
```

ou

```bash
cd thermometer/thermometerV2
python3 application.py
```