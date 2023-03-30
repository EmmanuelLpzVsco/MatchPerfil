from src.modules.catalogs.service.course import Course


def getCourses():
    return Course().getAll()
