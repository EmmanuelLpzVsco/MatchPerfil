import os
from src.modules.catalogs.models.entity.library import LibraryModel

libraries_data = [
    {
        "key": "NUMPY",
        "name": "NUMPY",
        "description": "Is considered as one of the most popular ML",
        "programmingLanguageId": "PYTHON",
    },
    {
        "key": "KERAS",
        "name": "KERAS",
        "description": "It provides an easier mechanism to express neural networks",
        "programmingLanguageId": "PYTHON",
    },
    {
        "key": "PANDAS",
        "name": "PANDAS",
        "description": "Provides data structures",
        "programmingLanguageId": "PYTHON",
    },
    {
        "key": "JQUERY",
        "name": "JQuery",
        "description": "It allows to add interactivity and visual effects on a website.",
        "programmingLanguageId": "JAVASCRIPT",
    },
    {
        "key": "GSON",
        "name": "Gson",
        "description": "It is used to convert Java objects to their JSON representation.",
        "programmingLanguageId": "JAVA",
    },
    {
        "key": "LOGGIN",
        "name": "Loggin",
        "description": "It is fundamental for the development of a software, especially in its production stage.",
        "programmingLanguageId": "JAVA",
    },
    {
        "key": "SLF4J",
        "name": "SLF4J",
        "description": "Provides a facade or abstraction for various logging frameworks",
        "programmingLanguageId": "JAVA",
    },
]


def migrate_libraries():
    if not LibraryModel.exists() or os.environ.get("HANDLER_MODE"):
        if not LibraryModel.exists():
            LibraryModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )
        for data in libraries_data:
            library = LibraryModel(**data)
            library.save()
