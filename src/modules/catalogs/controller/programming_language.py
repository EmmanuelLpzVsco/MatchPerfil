from src.modules.catalogs.use_case.programming_language import getProgrammingLanguages
from src.utils.http import HTTP_CODES, Response


def catalogGetProgrammingLanguages() -> dict:
    programminglanguages = getProgrammingLanguages()
    return Response(body=programminglanguages, statusCode=HTTP_CODES.OK)
