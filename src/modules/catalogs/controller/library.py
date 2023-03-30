from src.modules.catalogs.use_case.library import getLibraries
from src.utils.http import HTTP_CODES, Response


def catalogGetLibraries() -> dict:
    libraries = getLibraries()
    return Response(body=libraries, statusCode=HTTP_CODES.OK)
