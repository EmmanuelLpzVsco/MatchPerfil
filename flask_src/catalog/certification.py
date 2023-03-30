import os

from src.modules.catalogs.models.entity.certification import CertificationModel

certifications_data = [
    {
        "key": "SCRUM",
        "name": "SCRUM",
        "description": "SCRUM agile framework",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "JAVA-CERTIFICATION",
        "name": "JAVA CERTIFICATION",
        "description": "Java certification",
        "programmingLanguageId": "JAVA",
        "isSoftware": True,
    },
    {
        "key": "ITIL",
        "name": "ITIL",
        "description": "ITIL",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "CDP",
        "name": "Certified data professional",
        "description": "Certified data professional",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "CISSP",
        "name": "Certified information systems security professional",
        "description": "Certified information systems security professional",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "CCIE",
        "name": "Cisco certified internetwork expert",
        "description": "Cisco certified internetwork expert",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "CCNA",
        "name": "Cisco certified network associate",
        "description": "Cisco certified network associate",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "CCNP",
        "name": "Cisco certified network professional",
        "description": "Cisco certified network professional",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "A+",
        "name": "CompTIA",
        "description": "CompTIA",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "MTA",
        "name": "Microsoft technology associate",
        "description": "Microsoft technology associate",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "PMP",
        "name": "Project management professional",
        "description": "Project management professional",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "SYMFONY",
        "name": "Symfony framework",
        "description": "Symfony framework",
        "programmingLanguageId": "PHP",
        "isSoftware": True,
    },
]


def migrate_certifications():
    if not CertificationModel.exists() or os.environ.get("HANDLER_MODE"):
        if not CertificationModel.exists():
            CertificationModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )
        for data in certifications_data:
            certification = CertificationModel(**data)
            certification.save()
