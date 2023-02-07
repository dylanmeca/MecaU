# ☣ MecaU 🦠
[![Build Status](https://img.shields.io/github/stars/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU)
[![License](https://img.shields.io/github/license/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU/blob/main/LICENSE)
[![dylanmeca](https://img.shields.io/badge/author-dylanmeca-green.svg)](https://github.com/dylanmeca)
[![Python](https://img.shields.io/badge/language-Python%20-yellow.svg)](https://www.python.org)
![mecau](https://github.com/dylanmeca/MecaU/raw/main/logo.png)

MecaU is a security program designed to scan files for malware. It uses a database of known virus hashes and will compare the hash of each file 
on the system against the database to determine if it is infected. If an infected file is detected, the user has the choice to remove the malware or not. 
The program uses the OS Python library to walk through the files on the system and the hashlib library to calculate the hash of each file. 
The requests library is used to download the hash database from a server. MecaU is an effective tool to keep the system safe and protected against malware.

More information in the [Mecau Repository](https://github.com/dylanmeca/MecaU).
