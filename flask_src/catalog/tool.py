import os

from src.modules.catalogs.models.entity.tool import ToolModel

tools_data = [
    {"key": "ANSIBLE", "name": "ANSIBLE", "description": "Simple IT Automation"},
    {"key": "PENTAHO", "name": "PENTAHO", "description": "OPEN SOURCE ETL"},
    {"key": "CHEF", "name": "CHEF", "description": "IT Automation"},
    {"key": "PUPPET", "name": "PUPPET", "description": "IT Automation"},
    {"key": "DOCKER", "name": "DOCKER", "description": "Container Virtualization"},
    {
        "key": "DOCKER-COMPOSE",
        "name": "DOCKER-COMPOSE",
        "description": "Virtualization for development",
    },
    {
        "key": "VAGRANT",
        "name": "VAGRANT",
        "description": "VIRTUALIZATION FOR VIRTUALBOX",
    },
    {
        "key": "JENKINS",
        "name": "JENKINS",
        "description": "open source automation server",
    },
    {"key": "HUDSON", "name": "HUDSON", "description": "open source automation server"},
    {"key": "BAMBOO", "name": "BAMBOO", "description": "People Managment System"},
    {
        "key": "KUBERNETES",
        "name": "KUBERNETES",
        "description": "Platform for create microservices",
    },
    {"key": "GIT", "name": "GIT", "description": "Version control"},
    {
        "key": "GITLAB-CI",
        "name": "GITLAB-CI",
        "description": "Tool for create pipelines for ci/cd in gitlab",
    },
    {
        "key": "GITHUB-ACTIONS",
        "name": "GITHUB-ACTIONS",
        "description": "Tool for create pipelines for ci/cd in github",
    },
    {"key": "WORDPRESS", "name": "WORDPRESS", "description": "CMS created in PHP"},
    {"key": "DRUPAL", "name": "DRUPAL", "description": "CMS created in PHP"},
    {"key": "MOODLE", "name": "MOODLE", "description": "LMS created in PHP"},
    {"key": "TRELLO", "name": "TRELLO", "description": "Agile boards for SCRUM"},
]


def migrate_tools():
    if not ToolModel.exists() or os.environ.get("HANDLER_MODE"):
        if not ToolModel.exists():
            ToolModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )
        for data in tools_data:
            tool = ToolModel(**data)
            tool.save()
