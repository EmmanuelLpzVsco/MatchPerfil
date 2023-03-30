from src.modules.catalogs.service.programming_language import ProgrammingLanguage


def getProgrammingLanguages():
    return ProgrammingLanguage().getAll()
