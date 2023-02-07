import os
import hashlib
import requests

def is_infected(file):
    # Calcula el hash del archivo # Calculate the hash of the file
    print("[*] Scanning file....")
    hasher = hashlib.md5()
    with open(file, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    file_hash = hasher.hexdigest()

    # Verifica si el hash coincide con el del virus conocido # Check if the hash matches that of the known virus
    print("[*] El hash del archivo es: ", file_hash)
    response = requests.get('https://dylanmeca.github.io/MecaU/hashdb.txt')
    hash_db = response.text.splitlines()
    hash_db = list(hash_db)
    if file_hash in hash_db:
        return True
    else:
        return False

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_infected(file_path):
                # Elimina el archivo infectado # Delete the infected file
                print("[*] ¡Alerta! Se detecto malware")
                user = input("[*] Deseas eliminar el malware? (y/n) ")
                if user == "y":
                    print("[*] Eliminando malware...")
                    #os.remove(file_path)
                    os.system(f"scrub -p dod {file_path} && shred -zun 10 -v {file_path}")
                    print(f'[*] Eliminado {file_path}')
            else:
                print("[*] No se encontro malware")

# Ejecuta el escaneo en la siguiente carpeta # Run the scan in the following folder
#scan_directory('/home/use/directory')
user = input("[*] Escribe la ruta de la carpeta: ")
scan_directory(user)
