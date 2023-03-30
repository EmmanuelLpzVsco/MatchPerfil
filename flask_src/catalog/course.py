import os

from src.modules.catalogs.models.entity.course import CourseModel

courses_data = [
    {"key": "SCRUM", "name": "SCRUM", "description": "SCRUM agile framework"},
    {
        "key": "JAVA-ARCHITECT",
        "name": "JAVA ARCHITECT",
        "description": "Java ARCHITECT",
    },
]


def migrate_courses():
    if not CourseModel.exists() or os.environ.get("HANDLER_MODE"):
        if not CourseModel.exists():
            CourseModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )
        for data in courses_data:
            course = CourseModel(**data)
            course.save()
