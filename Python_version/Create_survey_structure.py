from pathlib import Path
import shutil
import argparse
import re

# =====================================
# CONFIG
# =====================================

TEMPLATE_DIR = Path(r".\Templates")
PROJECT_ROOT = Path(r".")
th2_templates = [
        "CAVENAME-plan.th2",
        "CAVENAME-coupe.th2"
    ]
# =====================================
# ARGUMENTS
# =====================================

parser = argparse.ArgumentParser(
    description="""
Création automatique d'un projet Therion.

Le script :
- crée l'arborescence du projet
- copie les fichiers template
- remplace CAVENAME par le nom de la survey
- importe éventuellement les exports TopoDroid
""",
    epilog="""
Exemples :

Créer un projet avec imports TopoDroid :
python new_survey.py gouffre --th export.th --th2 export.th2

Créer un projet avec un th2 vide template :
python new_survey.py gouffre --empty-th2
""",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument(
    "survey",
    help="Nom de la survey (sans espaces ni accents)"
)

parser.add_argument(
    "--th",
    help="Fichier .th exporté depuis TopoDroid",
)

parser.add_argument(
    "--th2",
    help="Fichier .th2 exporté depuis TopoDroid",
)

parser.add_argument(
    "--empty-th2",
    action="store_true",
    help="Créer un fichier .th2 vide depuis le template"
)

args = parser.parse_args()

SURVEY = args.survey

# =====================================
# VALIDATION
# =====================================

if not re.fullmatch(r"[a-z0-9_-]+", SURVEY):
    raise ValueError(
        "Nom invalide : uniquement minuscules, chiffres, _ et -"
    )

if args.empty_th2 and args.th2:
    raise ValueError(
        "Impossible d'utiliser --th2 et --empty-th2 ensemble"
    )

# =====================================
# CREATE FOLDERS
# =====================================

project_dir = PROJECT_ROOT / SURVEY
data_dir = project_dir / "Data"
outputs_dir = project_dir / "Outputs"

data_dir.mkdir(parents=True, exist_ok=True)
outputs_dir.mkdir(parents=True, exist_ok=True)

# =====================================
# COPY TEMPLATE FILES
# =====================================

for template_file in TEMPLATE_DIR.iterdir():

    if not template_file.is_file():
        continue

    new_name = template_file.name.replace(
            "CAVENAME",
            SURVEY
        )

    if template_file.name in th2_templates:
        
        continue

    destination = project_dir / new_name

    content = template_file.read_text(
        encoding="utf-8"
    )

    content = content.replace(
        "<CAVENAME>",
        SURVEY
    )

    destination.write_text(
        content,
        encoding="utf-8"
    )

# =====================================
# IMPORT TH
# =====================================

if args.th:

    shutil.copy2(
        Path(args.th),
        data_dir / f"{SURVEY}.th"
    )

# =====================================
# IMPORT TH2
# =====================================

if args.th2:

    shutil.copy2(
        Path(args.th2),
        data_dir / f"{SURVEY}.th2"
    )

# =====================================
# EMPTY TEMPLATE TH2
# =====================================

elif args.empty_th2:

    
    for template_name in th2_templates:

        template_path = TEMPLATE_DIR / template_name

        content = template_path.read_text(
            encoding="utf-8"
        )

        content = content.replace(
            "<CAVENAME>",
            SURVEY
        )

        output_name = template_name.replace(
            "CAVENAME",
            SURVEY
        )

        (
            data_dir / output_name
        ).write_text(
            content,
            encoding="utf-8"
        )
    print(data_dir/output_name)
print(f"Projet créé : {project_dir}")