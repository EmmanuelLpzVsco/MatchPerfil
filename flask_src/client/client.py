import os
from datetime import datetime

from src.modules.clients.models.client import ClientModel
from src.modules.clients.models.entity.project import ProjectMap

client_data = [
    {
        "id": "4d606f1c-dc4d-4307-ae11-1db0d47e0017",
        "contactEmail": "email@gmail.com",
        "phone": "5544332211",
        "company": "EDUTECNO",
        "rfc": "ABC34234231332",
        "street": "Lombardos",
        "intNumber": 92,
        "extNumber": 2,
        "zipCode": "12345",
        "projects": [
            {
                "id": "d225ad82-dcd5-4ee3-92b1-78e8bd9a21fc",
                "name": "",
                "owner": "",
                "contactPhone": "",
                "contactEmail": "",
                "cost": 300000,
                "beginDate": "1988-04-04 08:15:27.243860",
                "endDate": "1988-04-04 08:15:27.243860",
                "desiredProfiles": [
                    {
                        "id": "e36c6ed4-74ab-11eb-9439-0242ac130002",
                        "title": "Software Engineer",
                        "openPositions": 3,
                        "closePositions": 1,
                        "beginDate": "1988-04-04 08:15:27.243860",
                        "endDate": "1988-04-04 08:15:27.243860",
                        "active": "true",
                        "degree": "University",
                        "certifications": [
                            {
                                "certificationId": "SCRUM",
                                "needed": "false",
                            }
                        ],
                        "programmingLanguages": [
                            {
                                "programmingLanguageId": "PHP",
                                "experienceInYears": 5,
                                "needed": "true",
                            },
                            {
                                "programmingLanguageId": "PYTHON",
                                "experienceInYears": 2,
                                "needed": "true",
                            },
                        ],
                        "tools": [
                            {
                                "toolId": "VAGRANT",
                                "experienceInYears": 5,
                                "needed": "true",
                            },
                            {
                                "toolId": "DOCKER",
                                "experienceInYears": 3,
                                "needed": "false",
                            },
                            {
                                "toolId": "DOCKER-COMPOSE",
                                "experienceInYears": 2,
                                "needed": "true",
                            },
                        ],
                        "frameworks": [
                            {"frameworkId": "TSP", "experienceInYears": 2},
                            {"frameworkId": "SYMFONY", "experienceInYears": 4},
                            {"frameworkId": "SLIMPHP", "experienceInYears": 6},
                        ],
                        "courses": [
                            {"courseId": "SCRUM", "needed": "true"},
                            {"courseId": "JAVA-CERTIFICATION", "needed": "false"},
                        ],
                    }
                ],
            }
        ],
    },
    {
        "id": "f62fd2e5-b329-4330-aa52-f676d0b9a887",
        "contactEmail": "email2@gmail.com",
        "phone": "112233445566",
        "company": "Tecno-System",
        "rfc": "2332423445ASDF",
        "street": "Silos",
        "intNumber": 9222,
        "extNumber": 213,
        "zipCode": "98764",
        "projects": [
            {
                "id": "05d5895c-d7ea-416d-86a1-70a19ff76e74",
                "name": "",
                "owner": "",
                "contactPhone": "",
                "contactEmail": "",
                "cost": 1234344,
                "beginDate": "1988-04-04 08:15:27.243860",
                "endDate": "1988-04-04 08:15:27.243860",
            },
            {
                "id": "f039be2b-0838-48af-ad0b-bfbce8b4ed0f",
                "name": "",
                "owner": "",
                "contactPhone": "",
                "contactEmail": "",
                "cost": 56456,
                "beginDate": "1988-04-04 08:15:27.243860",
                "endDate": "1988-04-04 08:15:27.243860",
            },
            {
                "id": "6e403ecd-d4b2-46a9-9ef5-e727efff9bc8",
                "name": "",
                "owner": "",
                "contactPhone": "",
                "contactEmail": "",
                "cost": 23423423,
                "beginDate": "1988-04-04 08:15:27.243860",
                "endDate": "1988-04-04 08:15:27.243860",
            },
        ],
    },
]


def migrate_clients():
    if not ClientModel.exists() or os.environ.get("HANDLER_MODE"):
        if not ClientModel.exists():
            ClientModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )

        for data in client_data:
            projects = []
            if "projects" in data:
                for project in data["projects"]:
                    date_time_str = project["beginDate"]
                    date_time_obj = datetime.strptime(
                        date_time_str, "%Y-%m-%d %H:%M:%S.%f"
                    )
                    beginDate = date_time_obj
                    date_time_str = project["endDate"]
                    date_time_obj = datetime.strptime(
                        date_time_str, "%Y-%m-%d %H:%M:%S.%f"
                    )
                    endDate = date_time_obj
                    projectObj = ProjectMap(
                        id=project["id"],
                        name=project["name"],
                        owner=project["owner"],
                        contactPhone=project["contactPhone"],
                        contactEmail=project["contactEmail"],
                        cost=project["cost"],
                        beginDate=beginDate,
                        endDate=endDate,
                    )
                    projects.append(projectObj)
            else:
                projects = None
            client = ClientModel(
                id=data["id"],
                contactEmail=data["contactEmail"],
                phone=data["phone"],
                company=data["company"],
                rfc=data["rfc"],
                street=data["street"],
                intNumber=data["intNumber"],
                extNumber=data["extNumber"],
                zipCode=data["zipCode"],
                projects=projects,
            )
            client.save()
