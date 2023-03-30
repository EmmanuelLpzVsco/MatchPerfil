from src.modules.catalogs.use_case.tool import getTools
from src.utils.http import HTTP_CODES, Response


def catalogGetTools() -> dict:
    tools = getTools()
    return Response(body=tools, statusCode=HTTP_CODES.OK)
