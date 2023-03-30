from src.modules.catalogs.use_case.framework import getFrameworks
from src.utils.http import HTTP_CODES, Response


def catalogGetFrameworks() -> dict:
    frameworks = getFrameworks()
    return Response(body=frameworks, statusCode=HTTP_CODES.OK)
