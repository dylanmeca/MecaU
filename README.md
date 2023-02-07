# ☣ MecaU 🦠
[![Build Status](https://img.shields.io/github/stars/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU)
[![License](https://img.shields.io/github/license/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU/blob/main/LICENSE)
[![dylanmeca](https://img.shields.io/badge/author-dylanmeca-green.svg)](https://github.com/dylanmeca)
[![Python](https://img.shields.io/badge/language-Python%20-yellow.svg)](https://www.python.org)
![mecau](https://github.com/dylanmeca/MecaU/raw/main/logo.png)

MecaU is a security program designed to scan files for malware. It uses a database of known virus hashes and will compare the hash of each file on the system against the database to determine if it is infected. If an infected file is detected, the user has the choice to remove the malware or not. The program uses the OS Python library to walk through the files on the system and the hashlib library to calculate the hash of each file. The requests library is used to download the hash database from a local server. MecaU is an effective tool to keep the system safe and protected against malware.

## ⬇️ Installation

To install and use MecaU, follow these steps:

1. Asegúrate de tener instalado [Python](https://www.python.org/) en tu sistema.
2. Ejecuta el siguiente comando para instalar las dependencias necesarias: ```pip3 install requests argparse colorama```
3. Descarga el archivo: <a href="https://raw.githubusercontent.com/dylanmeca/MecaU/main/mecau.py" download="mecau.py">mecau.py</a>
4. Abre una terminal y accede al directorio donde esta el archivo [mecau.py](https://raw.githubusercontent.com/dylanmeca/MecaU/main/mecau.py).
5. Ejecuta el siguiente comando para iniciar un escaneo: ```python3 mecau.py -d /directory ```
