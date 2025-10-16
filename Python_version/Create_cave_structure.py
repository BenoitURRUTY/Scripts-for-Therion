# encoding: utf-8
"""
Released under a Creative Commons Attribution-ShareAlike-NonCommercial License:
http://creativecommons.org/licenses/by-nc-sa/4.0/

Written by Benoît Urruty
Converted to Python by ChatGPT (2025)
"""

import os
import shutil
import subprocess
from pathlib import Path

# === CONFIGURATION ===
# Chemin du modèle (à adapter selon ton système)
PATH_TEMPLATE = Path(r"C:\Users\TonNom\Documents\therion\Therion_survey")

def main():
    # --- Lecture du nom du système de grottes ---
    SN = input("Nom du système de grottes (ex: Reseau_kriska) : ").strip()
    if not SN:
        print("❌ Vous devez entrer un nom de système.")
        return

    print(f"📁 Création d’un dossier pour le système de grottes nommé : {SN}")

    # --- Création des dossiers ---
    base_dir = Path.cwd() / SN
    base_dir.mkdir(exist_ok=True)
    os.chdir(base_dir)

    (base_dir / "Outputs").mkdir(exist_ok=True)
    (base_dir / "GIS").mkdir(exist_ok=True)

    # --- Demander le nom du premier levé (survey) ---
    FS = input("Nom de votre premier levé (survey) : ").strip()
    if not FS:
        print("❌ Vous devez entrer un nom de levé.")
        return

    # --- Exécuter le script de création de levé ---
    create_survey_script = PATH_TEMPLATE / "create_survey.sh"
    if create_survey_script.exists():
        # Si on veut appeler directement le script shell existant
        subprocess.run(["bash", str(create_survey_script), FS], check=True)
    else:
        print("⚠️ Fichier create_survey.sh non trouvé, étape ignorée.")

    # --- Copier le fichier de configuration ---
    src_config = PATH_TEMPLATE / "Therion_files_pattern" / "config.thc"
    if src_config.exists():
        shutil.copy(src_config, base_dir)
    else:
        print("⚠️ config.thc introuvable.")

    # --- Créer le dossier des légendes ---
    legend_dir = base_dir / "legendes"
    legend_dir.mkdir(exist_ok=True)

    # --- Créer le fichier des coordonnées d’entrée ---
    src_entrances = PATH_TEMPLATE / "Therion_files_pattern" / "entrances_coordinates.th"
    dst_entrances = legend_dir / "entrances_coordinates.th"
    if src_entrances.exists():
        text = src_entrances.read_text(encoding="utf-8").replace("<RESEAUNAME>", SN)
        dst_entrances.write_text(text, encoding="utf-8")

    # --- Copier le script de compilation globale ---
    src_run_all = PATH_TEMPLATE / "Therion_files_pattern" / "run_all.sh"
    dst_run_all = base_dir.parent / "run_all.sh"
    if src_run_all.exists():
        shutil.copy(src_run_all, dst_run_all)

    # --- Fichier Maps.th ---
    src_maps = PATH_TEMPLATE / "Therion_files_pattern" / "Maps.th"
    dst_maps = base_dir / "Maps.th"
    if src_maps.exists():
        text = src_maps.read_text(encoding="utf-8")
        text = text.replace("<RESEAUNAME>", SN).replace("<CAVENAME>", FS)
        dst_maps.write_text(text, encoding="utf-8")

    # --- Fichier thconfig ---
    src_thconfig = PATH_TEMPLATE / "Therion_files_pattern" / "system.thconfig"
    dst_thconfig = base_dir / "thconfig"
    if src_thconfig.exists():
        text = src_thconfig.read_text(encoding="utf-8").replace("<RESEAUNAME>", SN)
        dst_thconfig.write_text(text, encoding="utf-8")

    # --- Fichier principal du réseau (RESEAUNAME.th) ---
    src_main_th = PATH_TEMPLATE / "Therion_files_pattern" / "RESEAUNAME.th"
    dst_main_th = base_dir / f"{SN}.th"
    if src_main_th.exists():
        text = src_main_th.read_text(encoding="utf-8")
        text = text.replace("<RESEAUNAME>", SN).replace("<CAVENAME>", FS)
        dst_main_th.write_text(text, encoding="utf-8")

    # --- Fichier atlas.thconfig ---
    src_atlas = PATH_TEMPLATE / "Therion_files_pattern" / "atlas.thconfig"
    dst_atlas = base_dir / "atlas.thconfig"
    if src_atlas.exists():
        text = src_atlas.read_text(encoding="utf-8").replace("<RESEAUNAME>", SN)
        dst_atlas.write_text(text, encoding="utf-8")

    # --- Copier le script create_survey.sh localement ---
    if create_survey_script.exists():
        shutil.copy(create_survey_script, base_dir)

    os.chdir(base_dir.parent)
    print(f"✅ Système de grottes '{SN}' créé avec succès dans {base_dir}")

if __name__ == "__main__":
    main()
