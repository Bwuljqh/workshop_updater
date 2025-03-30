from typing import TypedDict


class ModFile(TypedDict):
    name: str
    tags: list[str]
    picture: str
    supported_version: str
    remote_file_id: int
