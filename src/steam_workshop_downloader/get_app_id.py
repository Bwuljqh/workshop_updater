import requests


def get_game_id_from_mod_id(mod_id: str) -> str | None:
    """Get game id from mod id using the Steam API"""
    url_workshop = (
        "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"
    )
    data = {"itemcount": 1, "publishedfileids[0]": mod_id}
    response = requests.post(url_workshop, data=data)
    data = response.json()

    if data:
        return data["response"]["publishedfiledetails"][0]["creator_app_id"]
    else:
        return None


def get_app_and_workshop_id(url: str) -> None | tuple[str, str]:
    # Envoyer une requête HTTP pour obtenir le contenu de la page

    id = url.split("&")[0].split("/?id=")[-1]

    game_id = get_game_id_from_mod_id(id)
    if game_id:
        return game_id, id  # type: ignore
    else:
        return None


def get_app_name_from_id(game_id: int) -> str | None:
    """
    Get the app name from the app id
    :param game_id: app id
    :return: app name
    """
    pass
    url = f"https://store.steampowered.com/api/appdetails?appids={game_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if str(game_id) in data:
            app_name = data[str(game_id)]["data"]["name"]
            return app_name
        else:
            return None


if __name__ == "__main__":
    print(
        get_app_and_workshop_id(
            "https://steamcommunity.com/sharedfiles/filedetails/?id=3451188081&searchtext="
        )
    )
    print(get_app_name_from_id(281990))
