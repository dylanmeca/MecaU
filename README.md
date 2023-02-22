# ☣ MecaU 🦠
[![Build Status](https://img.shields.io/github/stars/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU)
[![License](https://img.shields.io/github/license/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU/blob/main/LICENSE)
[![dylanmeca](https://img.shields.io/badge/author-dylanmeca-green.svg)](https://github.com/dylanmeca)
[![Python](https://img.shields.io/badge/language-Python%20-yellow.svg)](https://www.python.org)
![mecau](https://github.com/dylanmeca/MecaU/raw/main/presentation.png)

MecaU is a security program designed to scan files for malware. It uses a database of known virus hashes and will compare the hash of each file on the system against the database to determine if it is infected. If an infected file is detected, the user has the choice to remove the malware or not. The program uses the OS Python library to walk through the files on the system and the hashlib library to calculate the hash of each file. The requests library is used to download the hash database from a server. MecaU is an effective tool to keep the system safe and protected against malware.

## ⬇️ Installation

To install and use MecaU, follow these steps:

> ⚠️ It is recommended to install [Yara](https://virustotal.github.io/yara/) for it to work correctly

1. Make sure you have [Python](https://www.python.org/) installed on your system.
2. Run the following command to install the necessary dependencies: ```pip3 install requests argparse colorama yara-python```
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

📦 It is also possible to install MecaU from an executable file: 
* 🐧 [Linux](https://github.com/dylanmeca/MecaU/releases/download/1.1/mecau)
    * ✅ Only tested on Debian 11
* 🪟 [Windows](https://github.com/dylanmeca/MecaU/releases/download/1.1/mecau.exe)
    * ✅ Only tested on Windows 11

## 🚨 Report Malware ☣

If when analyzing a program in [Tria.ge](https://tria.ge/), [VirusTotal](https://www.virustotal.com/) or you think a program is malware, you can report it in this repository in [the Issues Section](https://github.com/dylanmeca/MecaU/issues), to add the hash of said malware to our database and thus help our scanner detect more programs that are malware.

## 👷 Contributions
This project is open source and we are open to any kind of contribution. If you want to collaborate with the project, follow these steps:

- Fork this repository.
- Create a branch with your contribution.
- Make a pull request to this repository. 

Be sure to include a detailed description of your contribution and to follow our code standards.

## 📜 License
This project is released under the [GPL-3.0](https://github.com/dylanmeca/MecaU/blob/main/LICENSE) license. This means that the code and documentation in this project are free to use, modify, and distribute as long as you respect the license terms.

For more information about the license, see the [LICENSE](https://github.com/dylanmeca/MecaU/blob/main/LICENSE) file included in this repository.

## 🧾 Credits
This project has been developed by [Dylan Meca](https://github.com/dylanmeca) and contributions from [users](https://github.com/dylanmeca/MecaU/contributors).
