from src.modules.catalogs.use_case.course import getCourses
from src.utils.http import HTTP_CODES, Response


def catalogGetCourses() -> dict:
    courses = getCourses()
    return Response(body=courses, statusCode=HTTP_CODES.OK)
