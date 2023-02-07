import os
import hashlib
import requests
import argparse

def is_infected(file):
    # Calcula el hash del archivo
    print("[*] Escaneando archivo....")
    hasher = hashlib.md5()
    with open(file, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    file_hash = hasher.hexdigest()

    # Verifica si el hash coincide con el del virus conocido
    print("[*] El hash del archivo es: ", file_hash)
    response = requests.get('http://127.0.0.1/hashdb.txt')
    hash_db = response.text.splitlines()
    if file_hash in hash_db:
        return True
    else:
        return False

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_infected(file_path):
                # Elimina el archivo infectado
                print("[*] ¡Alerta! Se detecto malware")
                user = input("[*] Deseas eliminar el malware? (y/n) ")
                if user == "y":
                    print("[*] Eliminando malware...")
                    os.system(f"scrub -p dod {file_path} && shred -zun 10 -v {file_path}")
                    print(f'[*] Eliminado {file_path}')
            else:
                print("[*] No se encontro malware")

# Añade un argumento de línea de comandos para especificar el directorio a escanear
parser = argparse.ArgumentParser(description='Escanear un directorio para detectar malware')
parser.add_argument('-d', '--directory', required=True, help='Directorio a escanear')
args = parser.parse_args()

# Ejecuta el escaneo en el directorio especificado
scan_directory(args.directory)
