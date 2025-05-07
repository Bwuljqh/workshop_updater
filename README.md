# steam_workshop_downloader

Downloads and updates mods from the steam workshop using steamcmd and part of the implementation of https://github.com/f0rkz/pysteamcmd

# TODO and ideas

## Must Have
- implement prompt via prompt_toolkit
- connect the game number to the game name and add it to the prompt name
- separating by games will allow independant updates of games and mods

## Nice To Have/Won't have
- init games and ask target version
- when updating mods, backup first, checksum and verify version match
- add backup options to backup your current mod folder
- add states of the different mods as a recup when updating or installing
- try to find a way to know if a mod has been updated (maybe a checksum?)

## CLI Commands

- info games
- info mods {game}
- install mod {mod_link|mod_id}
- install collection {collection_link|collection_id}
- update game {game}
- update all

# Project Management

I don't known when I'll ever work on this again. I'm open to pull requests
