# Install a mod from a link

# Optional: install a mod from a name game and a name mod, give a prompt for the game and the mod to check if it's the right mod



from steam_workshop_downloader.get_app_id import get_app_and_workshop_id
from steam_workshop_downloader.steamcmd import SteamCMD


def install_mod(steam_handler: SteamCMD, file: str, game_install_dir: str):
    ids = get_app_and_workshop_id(file)
    if ids is None:
        print("Invalid URL")
        return
    app_id, workshop_id = ids
    steam_handler.install_workshopfiles(app_id, workshop_id, game_install_dir)


def install_mods(steam_handler: SteamCMD, files: list[str], game_install_dir: str):
    for file in files:
        install_mod(steam_handler, file, game_install_dir)


steamcmd = SteamCMD(install_path=r"C:\Users\Bwuljqh\Documents\steamcmd")
install_mods(
    steamcmd,
    ["https://steamcommunity.com/sharedfiles/filedetails/?id=3451188081&searchtext="],
    r"C:\Users\Bwuljqh\Documents\steamcmd",
)
