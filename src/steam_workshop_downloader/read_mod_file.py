from typing import cast

from steam_workshop_downloader.utils import ModFile


def read_file_to_dict(file_path: str) -> ModFile:
    mod_info = {}
    current_key = None

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip().replace('"', "")

            if "=" in line:
                current_key, value = line.split("=", 1)
                # Si la clé est "tags", initialiser une liste vide
                if current_key == "tags":
                    mod_info[current_key] = []
                elif current_key == "remote_file_id":
                    mod_info[current_key] = int(value)
                else:
                    mod_info[current_key] = value
            elif current_key == "tags":
                # Ajouter les tags à la liste
                if "}" not in line:
                    mod_info[current_key].append(line)

    return cast(ModFile, mod_info)


# Exemple d'utilisation
file_path = r"C:\Users\Bwuljqh\Documents\steamcmd\steamapps\workshop\content\281990\1623423360\descriptor.mod"
mod_info = read_file_to_dict(file_path)
