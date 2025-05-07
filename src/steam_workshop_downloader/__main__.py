from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter

from steam_workshop_downloader.steamcmd import SteamCMD
from steam_workshop_downloader.updater import update_mods_from_game_id


def get_names(names) -> list[str]:
    return names


def main():
    NAMES = ["show", "exit", "clear", "help", "ping", "traceroute", "telnet"]

    session = PromptSession()

    while True:
        try:
            completer = NestedCompleter.from_nested_dict(
                {
                    "install": {
                        "version": None,
                        "clock": None,
                        "ip": {"interface": {"brief": None}},
                    },
                    "update": {i: None for i in get_names(NAMES)},
                }
            )
            text = session.prompt(
                ">>",
                completer=completer,
                complete_while_typing=True,
                complete_in_thread=True,
            )
            print(text)
            if text.startswith("exit"):
                NAMES += [text.split(" ")[1]]
        except KeyboardInterrupt:
            break
        else:
            print("You entered:", text)
        print(f"You said: {text}")


if __name__ == "__main__":
    steamcmd = SteamCMD(install_path=r"C:\Users\Bwuljqh\Documents\steamcmd")
    update_mods_from_game_id(steamcmd, "281990")
    # answer = confirm("Should we do that?")
    # print(f"Answer: {answer}")
    main()
