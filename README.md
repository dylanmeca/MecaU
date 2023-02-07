# ☣ MecaU 🦠
[![Build Status](https://img.shields.io/github/stars/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU)
[![License](https://img.shields.io/github/license/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU/blob/main/LICENSE)
[![dylanmeca](https://img.shields.io/badge/author-dylanmeca-green.svg)](https://github.com/dylanmeca)
[![Python](https://img.shields.io/badge/language-Python%20-yellow.svg)](https://www.python.org)
![mecau](https://github.com/dylanmeca/MecaU/raw/main/logo.png)

MecaU is a security program designed to scan files for malware. It uses a database of known virus hashes and will compare the hash of each file on the system against the database to determine if it is infected. If an infected file is detected, the user has the choice to remove the malware or not. The program uses the OS Python library to walk through the files on the system and the hashlib library to calculate the hash of each file. The requests library is used to download the hash database from a local server. MecaU is an effective tool to keep the system safe and protected against malware.

## ⬇️ Installation

To install and use MecaU, follow these steps:

1. Make sure you have [Python](https://www.python.org/) installed on your system.
2. Run the following command to install the necessary dependencies: ```pip3 install requests argparse colorama```
3. Download the file: <a href="https://raw.githubusercontent.com/dylanmeca/MecaU/main/mecau.py" download="mecau.py">mecau.py</a>
4. Open a terminal and access the directory where the file is [mecau.py](https://raw.githubusercontent.com/dylanmeca/MecaU/main/mecau.py).
5. Run the following command to start a scan: ```python3 mecau.py -d /directory ```

```txt
usage: mecau.py [-h] -d DIRECTORY

Scan a directory for malware

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Directory to scan
```
