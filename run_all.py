import os
import subprocess
from pathlib import Path
import sys

def main():
    # Demander à l'utilisateur le chemin racine
    if len(sys.argv) > 1:
        PATH_SURVEY = Path(sys.argv[1]).expanduser().resolve()
    else:
        chemin_saisi = input("Entrez le chemin du dossier principal (ex : C:\\Users\\Moi\\Documents\\projet) : ").strip()
        # Conversion en objet Path (gère automatiquement Windows/Linux)
        PATH_SURVEY = Path(chemin_saisi).expanduser().resolve()

    # Vérifie que le chemin existe
    if not PATH_SURVEY.exists():
        print(f"Erreur : le chemin {PATH_SURVEY} n'existe pas.")
        return

    # Recherche récursive des fichiers 'thconfig'
    for thconfig_path in PATH_SURVEY.rglob("thconfig"):
        print(f"Processing file '{thconfig_path}'")

        # Répertoire contenant le fichier
        folder = thconfig_path.parent

        output_dir = folder / "Outputs"
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
            print(f"📁 Dossier 'Outputs' créé dans : {output_dir}")
        else:
            print(f"📁 Dossier 'Outputs' déjà présent.")


        # Exécute la commande "therion thconfig" dans ce dossier
        try:
            subprocess.run(["therion", "thconfig"], cwd=folder, check=True)
        except FileNotFoundError:
            print("Erreur : la commande 'therion' n'a pas été trouvée dans le PATH système.")
            print("👉 Installe Therion ou ajoute-le à la variable d'environnement PATH.")
            break
        except subprocess.CalledProcessError:
            print(f"⚠️ Échec de l'exécution dans {folder}")
        else:
            print(f"✅ Compilation réussie dans {folder}\n")

if __name__ == "__main__":
    main()
