# Update all mods available in C:\Users\Bwuljqh\Documents\steamcmd\steamapps\workshop\content\
# Update all mods in a certain folder, can update only a certain game, returns a table with all updates and their game version
import os
from os import walk

from steam_workshop_downloader.steamcmd import SteamCMD

steam_folders = ["steamapps", "workshop", "content"]


def get_steam_workshop_folder(folder: str):
    pass


def update_mods(steam_handler: SteamCMD, folder: str):
    if (
        "steamapps" not in folder
        and "steamcmd" not in folder
        and "steamapps" not in os.listdir(folder)
    ):
        raise ValueError("Folder must contain steamcmd or steamapps")

    new_path: None | str = None

    mods_to_update: dict[str, list[str]] = {}
    # Find the workshop folder in the given folder
    for dirpath, dirnames, filenames in walk(folder):
        if dirpath.endswith(os.path.join(*steam_folders)):
            new_path = dirpath
            mods_to_update.update({id: [] for id in dirnames})
            break

    if new_path is None:
        raise ValueError("No steam workshop folder found")
    if mods_to_update.keys() == []:
        raise ValueError("No games found")

    # Get the install_path which is 3 directories up from the workshop folder
    install_path = os.path.dirname(os.path.dirname(os.path.dirname(new_path)))
    for id in mods_to_update.keys():
        for workshop_item_id in os.listdir(os.path.join(new_path, id)):
            steam_handler.install_workshopfiles(id, workshop_item_id, install_path)
steamcmd = SteamCMD(install_path=r"C:\Users\Bwuljqh\Documents\steamcmd")


update_mods(steamcmd, r"C:\Users\Bwuljqh\Documents\steamcmd\steamapps\workshop\content")
