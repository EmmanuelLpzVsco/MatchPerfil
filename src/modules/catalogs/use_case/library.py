from src.modules.catalogs.service.library import Library


def getLibraries():
    return Library().getAll()
