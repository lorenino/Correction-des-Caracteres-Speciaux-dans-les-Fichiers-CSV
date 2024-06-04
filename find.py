import pandas as pd
import re

# Lire le fichier avec l'encodage latin1
csv_input_path = "tasks_with_real_values.csv"
data_latin1 = pd.read_csv(csv_input_path, encoding='latin1')

# Fonction pour trouver tous les caractères spéciaux mal encodés
def find_special_characters(dataframe):
    unique_chars = set()
    for column in dataframe.columns:
        unique_chars.update(re.findall(r'[^\x00-\x7F]', ' '.join(dataframe[column].astype(str))))
    return unique_chars

special_chars = find_special_characters(data_latin1)
print("Caractères spéciaux trouvés:", special_chars)
