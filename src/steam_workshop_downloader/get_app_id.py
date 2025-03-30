import requests
from bs4 import BeautifulSoup


def get_app_and_workshop_id(url: str) -> None | tuple[str, str]:
    # Envoyer une requête HTTP pour obtenir le contenu de la page
    response = requests.get(url)
    response.raise_for_status()  # Vérifier si la requête a réussi
    id = url.split("&")[0].split("/?id=")[-1]
    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver la balise <a> avec les classes spécifiées
    link = soup.find("a", class_="btnv6_blue_hoverfade btn_medium")

    # Retourner le contenu de la balise <a>
    if link:
        return link.get("data-appid"), id  # type: ignore
    else:
        return None


if __name__ == "__main__":
    print(
        get_app_and_workshop_id(
            "https://steamcommunity.com/sharedfiles/filedetails/?id=3451188081&searchtext="
        )
    )
