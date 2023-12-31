import os
import sys
import hashlib
import requests
import argparse
import yara
from colorama import init, Fore, Style

init(autoreset=True)

try:
    # Download the rules.yar file
    response = requests.get('https://dylanmeca.github.io/MecaU/rules.yar')
    yara_rules = response.text
    # Download the hashdb.txt file
    response = requests.get('https://dylanmeca.github.io/MecaU/hashdb.txt')
    hash_db = response.text.splitlines()
except:
    print(Style.BRIGHT + Fore.RED + "[*] Could not connect to the server")
    sys.exit()

# Compile the Yara rules
try: 
    rules = yara.compile(source=yara_rules)
except:
    rules = False

def is_infected(file):
    # Calculate the hash of the file
    print(Style.BRIGHT + Fore.GREEN + "[*] Scanning file....")
    hasher = hashlib.md5()
    with open(file, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    file_hash = hasher.hexdigest()

    # Check if the hash matches that of the known virus
    print(Style.BRIGHT + Fore.GREEN + "[*] The hash of the file is:", file_hash)
    if file_hash in hash_db:
        return True
    else:
        if rules != False: 
            matches = rules.match(file)
            if matches:
                print(Style.BRIGHT + Fore.RED + "[*] A suspicious file has been detected")
                print(Style.BRIGHT + Fore.RED + f"[*] Rules: {matches}")
                print(Style.BRIGHT + Fore.RED + f"[*] Strings: {matches[0].strings}")
                return True
            else:
                print(Style.BRIGHT + Fore.GREEN + "[*] The file does not seem suspicious")
                return False

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(Style.BRIGHT + Fore.WHITE + "----------------------")
            if is_infected(file_path):
                # Delete the infected file
                print(Style.BRIGHT + Fore.RED + f"[*] File: {file_path}")
                print(Style.BRIGHT + Fore.RED + "[*] ¡Alert! Malware detected")
                user = input(Style.BRIGHT + Fore.GREEN + "[*] Do you want to remove the malware? (y/n) ")
                if user == "y":
                    print(Style.BRIGHT + Fore.GREEN + "[*] Removing malware...")
                    #os.system(f"scrub -p dod {file_path} && shred -zun 10 -v {file_path}")
                    os.remove(file_path)
                    print(Style.BRIGHT + Fore.GREEN + f'[*] Removed {file_path}')
            else:
                print(Style.BRIGHT + Fore.GREEN + f"[*] File: {file_path}")
                print(Style.BRIGHT + Fore.GREEN + "[*] No malware found")

# Add a command line argument to specify the directory to scan
parser = argparse.ArgumentParser(description='Scan a directory for malware')
parser.add_argument('-d', '--directory', required=True, help='Directory to scan')
args = parser.parse_args()

# Run the scan in the specified directory
scan_directory(args.directory)
