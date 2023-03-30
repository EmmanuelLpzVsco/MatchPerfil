from flask_src.catalog.certification import migrate_certifications
from flask_src.catalog.course import migrate_courses
from flask_src.catalog.framework import migrate_frameworks
from flask_src.catalog.library import migrate_libraries
from flask_src.catalog.programming_language import migrate_programming_languages
from flask_src.catalog.tool import migrate_tools
from flask_src.client.client import migrate_clients
from flask_src.profile.profile import migrate_profiles

migrate_programming_languages()
migrate_frameworks()
migrate_libraries
migrate_certifications()
migrate_tools()
migrate_courses()

migrate_profiles()
migrate_clients()
