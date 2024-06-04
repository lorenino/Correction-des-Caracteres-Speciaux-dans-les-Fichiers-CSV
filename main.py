
### script_correction_caracteres.py

```python
import pandas as pd

# Chemin du fichier CSV d'entrée
csv_input_path = "votre_fichier.csv"

# Lire le fichier avec l'encodage latin1
data_latin1 = pd.read_csv(csv_input_path, encoding='latin1')

# Correction des caractères spéciaux mal encodés
replacements = {
    'Ð¹': 'é',
    'Ð´': 'd',
    'Ðµ': 'e',
    'Ð¾': 'o',
    'Ð¸': 'i',
    'Ð½': 'n',
    'Ð¼': 'm',
    'Ð°': 'a',
    'Ð»': 'l',
    'Ð': 'D',
    'Ð²': 'v',
    'Ð¿': 'p',
    'Ã©': 'é',
    'Ã¨': 'è',
    'Ãª': 'ê',
    'Ã ': 'à',
    'Ã¹': 'ù',
    'Ã´': 'ô',
    'Ã§': 'ç',
    'Ã¼': 'ü',
    'Ã¯': 'ï',
    'Ã«': 'ë',
    'Ã¡': 'á',
    'Ã¢': 'â',
    'ÃÂ™': 'É',
    'iÃ©': 'ié',
    'Â°': '°',
    'Â': ''
}

data_corrected = data_latin1.replace(replacements, regex=True)

# Chemin du fichier Excel de sortie
excel_output_path = "votre_fichier_corrige.xlsx"

# Sauvegarder le fichier corrigé au format Excel
data_corrected.to_excel(excel_output_path, index=False)

print(f"Le fichier corrigé a été sauvegardé à l'emplacement : {excel_output_path}")
