import json

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, jsonify, request
from flask_apispec import FlaskApiSpec, doc, marshal_with, use_kwargs
from flask_compress import Compress
from flask_cors import CORS
from webargs import fields

import flask_src.init
from src.modules.catalogs.controller.certification import catalogGetCertifications
from src.modules.catalogs.controller.course import catalogGetCourses
from src.modules.catalogs.controller.framework import catalogGetFrameworks
from src.modules.catalogs.controller.library import catalogGetLibraries
from src.modules.catalogs.controller.programming_language import (
    catalogGetProgrammingLanguages,
)
from src.modules.catalogs.controller.tool import catalogGetTools
from src.modules.catalogs.controller.validator.certification import (
    CertificationResponseSchema,
)
from src.modules.catalogs.controller.validator.course import CourseResponseSchema
from src.modules.catalogs.controller.validator.framework import FrameworkResponseSchema
from src.modules.catalogs.controller.validator.library import LibraryResponseSchema
from src.modules.catalogs.controller.validator.programming_language import (
    ProgrammingLanguageResponseSchema,
)
from src.modules.catalogs.controller.validator.tool import ToolResponseSchema
from src.modules.clients.controller.client import clientGetProjects
from src.modules.clients.controller.validator.client import (
    ClientPostRequestSchema,
    ClientResponseSchema,
    ClientUpdateRequestSchema,
)
from src.modules.clients.controller.validator.project import (
    ProjectPostRequestSchema,
    ProjectResponseSchema,
    ProjectUpdateRequestSchema,
)
from src.modules.clients.service.client import Client
from src.modules.profiles.controller.profile import (
    profileAddCertification,
    profileAddCourse,
    profileAddFramework,
    profileAddJob,
    profileAddProfile,
    profileAddProgrammingLanguage,
    profileAddStudyLevel,
    profileAddTool,
    profileGetAllProfiles,
    profileGetById,
)
from src.modules.profiles.controller.validator.certification import (
    ProfileCertificationPostRequestSchema,
    ProfileCertificationResponseSchema,
)
from src.modules.profiles.controller.validator.course import (
    ProfileCoursePostRequestSchema,
    ProfileCourseResponseSchema,
)
from src.modules.profiles.controller.validator.framework import (
    ProfileFrameworkPostRequestSchema,
    ProfileFrameworkResponseSchema,
)
from src.modules.profiles.controller.validator.job import (
    ProfileJobPostRequestSchema,
    ProfileJobResponseSchema,
)
from src.modules.profiles.controller.validator.profile import (
    ProfilePostRequestSchema,
    ProfileResponseSchema,
    ProfileUpdateRequestSchema,
)
from src.modules.profiles.controller.validator.programming_language import (
    ProfileProgrammingLanguagePostRequestSchema,
    ProfileProgrammingLanguageResponseSchema,
)
from src.modules.profiles.controller.validator.study_level import (
    ProfileStudyLevelPostRequestSchema,
    ProfileStudyLevelResponseSchema,
)
from src.modules.profiles.controller.validator.tool import (
    ProfileToolPostRequestSchema,
    ProfileToolResponseSchema,
)
from src.modules.profiles.service.profile import Profile
from src.utils.http import HTTP_CODES

app = Flask(__name__)

app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="ProfileMatcher",
            description="API from Profile Matcher",
            version="1.0.0",
            openapi_version="2.0.0",
            plugins=[MarshmallowPlugin()],
            # servers=[
            #     {
            #         'url':'https://{host}/dev',
            #         'variables':{
            #             'host':{
            #                 'default':'s3zz3rte8j.execute-api.us-east-2.amazonaws.com'
            #             }
            #         },
            #         'description': 'Development API server'
            #     },
            #     {
            #         'url':'http://localhost:{port}',
            #         'variables':{
            #             'port':{
            #                 'default':"5000"
            #             }
            #         },
            #         'description': 'Local API server'
            #     }
            # ]
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",
    }
)

docs = FlaskApiSpec(app, document_options=False)

compress = Compress(app)
CORS(app)


@docs.register
@doc(tags=["Profile"], description="Get all profiles")
@marshal_with(
    ProfileResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The profiles found",
)
@app.route("/manager/v1/profiles", methods=["GET"])
def get_profiles():
    response = profileGetAllProfiles()
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Store a profile")
@use_kwargs(ProfilePostRequestSchema, required=True)
@marshal_with(
    ProfileResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The profile stored",
)
@app.route("/manager/v1/profiles", methods=["POST"])
def add_profile():
    data = request.json
    response = profileAddProfile(data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Get a profile by Id")
@marshal_with(
    ProfileResponseSchema(many=False),
    code=HTTP_CODES.OK,
    description="The profile found",
)
@app.route("/manager/v1/profiles/<profileId>", methods=["GET"])
def get_profile_by_id(profileId):
    response = profileGetById(profileId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Update a profile by Id")
@use_kwargs(ProfileUpdateRequestSchema, required=True)
@marshal_with(
    ProfileResponseSchema(many=False),
    code=HTTP_CODES.OK,
    description="The profile updated",
)
@app.route("/manager/v1/profiles/<profileId>", methods=["PUT"])
def update_by_id(profileId):
    data = request.json
    response = Profile().update(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Delete profile by Id")
@marshal_with(None, code=HTTP_CODES.NO_CONTENT, description="The profile was deleted")
@app.route("/manager/v1/profiles/<profileId>", methods=["DELETE"])
def delete_by_id(profileId):
    response = Profile().delete(profileId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Add programming language for a specific profile")
@use_kwargs(ProfileProgrammingLanguagePostRequestSchema, required=True)
@marshal_with(
    ProfileProgrammingLanguageResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The programming language was added",
)
@app.route("/manager/v1/profiles/<profileId>/programmingLanguages", methods=["POST"])
def add_programming_language(profileId):
    data = request.json
    response = profileAddProgrammingLanguage(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(
    tags=["Profile"], description="Delete a programming language for a specific profile"
)
@marshal_with(
    None, code=HTTP_CODES.NO_CONTENT, description="The programming language was deleted"
)
@app.route(
    "/manager/v1/profiles/<profileId>/programmingLanguages/<programmingLanguageId>",
    methods=["DELETE"],
)
def delete_programming_language(profileId, programmingLanguageId):
    response = Profile().deleteProgrammingLanguage(profileId, programmingLanguageId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Add a new course for a specific profile")
@use_kwargs(ProfileCoursePostRequestSchema, required=True)
@marshal_with(
    ProfileCourseResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The course was added",
)
@app.route("/manager/v1/profiles/<profileId>/courses", methods=["POST"])
def add_course(profileId):
    data = request.json
    response = profileAddCourse(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Delete a course for a specific profile")
@marshal_with(None, code=HTTP_CODES.NO_CONTENT, description="The course was deleted")
@app.route("/manager/v1/profiles/<profileId>/courses/<courseId>", methods=["DELETE"])
def delete_course(profileId, courseId):
    response = Profile().deleteCourse(profileId, courseId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Add certification for a specific profile")
@use_kwargs(ProfileCertificationPostRequestSchema, required=True)
@marshal_with(
    ProfileCertificationResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The certification was added",
)
@app.route("/manager/v1/profiles/<profileId>/certifications", methods=["POST"])
def add_certification(profileId):
    data = request.json
    response = profileAddCertification(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Delete a certification for a specific profile")
@marshal_with(
    None, code=HTTP_CODES.NO_CONTENT, description="The certification was deleted"
)
@app.route(
    "/manager/v1/profiles/<profileId>/certifications/<certificationId>",
    methods=["DELETE"],
)
def delete_certification(profileId, certificationId):
    response = Profile().deleteCertification(profileId, certificationId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@use_kwargs(ProfileToolPostRequestSchema, required=True)
@marshal_with(
    ProfileToolResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The tool was added",
)
@doc(tags=["Profile"], description="Add a tool for a specific profile")
@app.route("/manager/v1/profiles/<profileId>/tools", methods=["POST"])
def add_tool(profileId):
    data = request.json
    response = profileAddTool(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Delete a tool for a specific profile")
@marshal_with(None, code=HTTP_CODES.NO_CONTENT, description="The tool was deleted")
@app.route("/manager/v1/profiles/<profileId>/tools/<toolId>", methods=["DELETE"])
def delete_tool(profileId, toolId):
    response = Profile().deleteTool(profileId, toolId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Add a framework for a specific profile")
@use_kwargs(ProfileFrameworkPostRequestSchema, required=True)
@marshal_with(
    ProfileFrameworkResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The framework was added",
)
@app.route("/manager/v1/profiles/<profileId>/frameworks", methods=["POST"])
def add_framework(profileId):
    data = request.json
    response = profileAddFramework(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Delete a framework for a specific profile")
@marshal_with(None, code=HTTP_CODES.NO_CONTENT, description="The framework was deleted")
@app.route(
    "/manager/v1/profiles/<profileId>/frameworks/<frameworkId>", methods=["DELETE"]
)
def delete_framework(profileId, frameworkId):
    response = Profile().deleteFramework(profileId, frameworkId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Add a job for a specific profile")
@use_kwargs(ProfileJobPostRequestSchema, required=True)
@marshal_with(
    ProfileJobResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The job was added",
)
@app.route("/manager/v1/profiles/<profileId>/jobs", methods=["POST"])
def add_job(profileId):
    data = request.json
    response = profileAddJob(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Delete a job for a specific profile")
@marshal_with(None, code=HTTP_CODES.NO_CONTENT, description="The job was deleted")
@app.route("/manager/v1/profiles/<profileId>/jobs/<jobId>", methods=["DELETE"])
def delete_job(profileId, jobId):
    response = Profile().deleteJob(profileId, jobId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Add a study level for a specific profile")
@use_kwargs(ProfileStudyLevelPostRequestSchema, required=True)
@marshal_with(
    ProfileStudyLevelResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The study level was added",
)
@app.route("/manager/v1/profiles/<profileId>/studyLevels", methods=["POST"])
def add_study_level(profileId):
    data = request.json
    response = profileAddStudyLevel(profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Profile"], description="Delete a study level for a specific profile")
@marshal_with(
    None, code=HTTP_CODES.NO_CONTENT, description="The study level was deleted"
)
@app.route(
    "/manager/v1/profiles/<profileId>/studyLevels/<studyLevelId>", methods=["DELETE"]
)
def delete_study_level(profileId, studyLevelId):
    response = Profile().deleteStudyLevel(profileId, studyLevelId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Get all clients")
@marshal_with(
    ClientResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The clients found",
)
@app.route("/manager/v1/clients", methods=["GET"])
def get_clients():
    response = Client().getAll()
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Add a client")
@use_kwargs(ClientPostRequestSchema, required=True)
@marshal_with(
    ClientResponseSchema(many=False),
    code=HTTP_CODES.CREATED,
    description="The client was added",
)
@app.route("/manager/v1/clients", methods=["POST"])
def post_client():
    data = request.json
    response = Client().create(data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Get a client by id")
@marshal_with(
    ClientResponseSchema(many=False),
    code=HTTP_CODES.OK,
    description="The client found",
)
@app.route("/manager/v1/clients/<clientId>", methods=["GET"])
def get_client_by_id(clientId):
    response = Client().getById(clientId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Update a client by id")
@use_kwargs(ClientUpdateRequestSchema, required=True)
@marshal_with(
    ClientResponseSchema(many=False),
    code=HTTP_CODES.OK,
    description="The client updated",
)
@app.route("/manager/v1/clients/<clientId>", methods=["PUT"])
def update_client(clientId):
    data = request.json
    response = Client().update(clientId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Delete a client by id")
@marshal_with(None, code=HTTP_CODES.NO_CONTENT, description="The client was deleted")
@app.route("/manager/v1/clients/<clientId>", methods=["DELETE"])
def delete_client(clientId):
    response = Client().delete(clientId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Get all projects by clientId")
@marshal_with(
    ProjectResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The projects found by specific client",
)
@app.route("/manager/v1/clients/<clientId>/projects", methods=["GET"])
def get_projects(clientId):
    response = clientGetProjects(clientId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Add a project for a specific client")
@use_kwargs(ProjectPostRequestSchema, required=True)
@marshal_with(
    ProjectResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The projects found by specific client",
)
@app.route("/manager/v1/clients/<clientId>/projects", methods=["POST"])
def add_project(clientId):
    data = request.json
    response = Client().addProject(clientId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Get a specific project for a specific client")
@marshal_with(
    ProjectResponseSchema(many=False),
    code=HTTP_CODES.OK,
    description="The project found by specific client",
)
@app.route("/manager/v1/clients/<clientId>/projects/<projectId>", methods=["GET"])
def get_project_by_id(clientId, projectId):
    response = Client().getProjectById(clientId, projectId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Update a specific project for a specific client")
@use_kwargs(ProjectUpdateRequestSchema, required=True)
@marshal_with(
    ProjectResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The project updated",
)
@app.route("/manager/v1/clients/<clientId>/projects/<projectId>", methods=["PUT"])
def update_project_by_id(clientId, projectId):
    data = request.json
    response = Client().updateProjectById(clientId, projectId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Client"], description="Delete a specific project for a specific client")
@marshal_with(None, code=HTTP_CODES.NO_CONTENT, description="The project was deleted")
@app.route("/manager/v1/clients/<clientId>/projects/<projectId>", methods=["DELETE"])
def delete_project_by_id(clientId, projectId):
    response = Client().deleteProjectById(clientId, projectId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(
    tags=["Client"],
    description="Get all required profiles for a specific project from specific client",
)
@app.route(
    "/manager/v1/clients/<clientId>/projects/<projectId>/profiles", methods=["GET"]
)
def get_profiles_by_project_id(clientId, projectId):
    response = Client().getProjects(clientId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(
    tags=["Client"],
    description="Add a required profile for a specific project from specific client",
    deprecated=True,
)
@app.route(
    "/manager/v1/clients/<clientId>/projects/<projectId>/profiles", methods=["POST"]
)
def add_profile_to_project(clientId, profileId):
    data = request.json
    response = Client().addProfileToProject(clientId, profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(
    tags=["Client"],
    description="Get a required profile for a specific project from specific client",
    deprecated=True,
)
@app.route(
    "/manager/v1/clients/<clientId>/projects/<projectId>/profiles/<profileId>",
    methods=["GET"],
)
def get_profile_by_project_id(clientId, projectId, profileId):
    response = Client().getProfileByIdByProjectId(clientId, projectId, profileId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(
    tags=["Client"],
    description="Update a required profile for a specific project from specific client",
    deprecated=True,
)
@app.route(
    "/manager/v1/clients/<clientId>/projects/<projectId>/profiles/<profileId>",
    methods=["PUT"],
)
def update_profile_by_project_id(clientId, projectId, profileId):
    data = request.json
    response = Client().updateProfileByProjectId(clientId, projectId, profileId, data)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(
    tags=["Client"],
    description="Delete a required profile for a specific project from specific client",
    deprecated=True,
)
@marshal_with(
    None, code=HTTP_CODES.NO_CONTENT, description="The project's profile was deleted"
)
@app.route(
    "/manager/v1/clients/<clientId>/projects/<projectId>/profiles/<profileId>",
    methods=["DELETE"],
)
def delete_profile_by_project_id(clientId, projectId, profileId):
    response = Client().deleteProfileByProjectId(clientId, projectId, profileId)
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Catalog"], description="Get programming languages")
@marshal_with(
    ProgrammingLanguageResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The programming languages stored",
)
@app.route("/manager/v1/catalogs/programmingLanguages", methods=["GET"])
def get_programming_languages():
    response = catalogGetProgrammingLanguages()
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Catalog"], description="Get frameworks")
@marshal_with(
    FrameworkResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The frameworks stored",
)
@app.route("/manager/v1/catalogs/frameworks", methods=["GET"])
def get_frameworks():
    response = catalogGetFrameworks()
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Catalog"], description="Get libraries")
@marshal_with(
    LibraryResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The libraries stored",
)
@app.route("/manager/v1/catalogs/libraries", methods=["GET"])
def get_libraries():
    response = catalogGetLibraries()
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Catalog"], description="Get certifications")
@marshal_with(
    CertificationResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The certifications stored",
)
@app.route("/manager/v1/catalogs/certifications", methods=["GET"])
def get_certifications():
    response = catalogGetCertifications()
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Catalog"], description="Get courses")
@marshal_with(
    CourseResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The courses stored",
)
@app.route("/manager/v1/catalogs/courses", methods=["GET"])
def get_courses():
    response = catalogGetCourses()
    return jsonify(json.loads(response["body"])), response["statusCode"]


@docs.register
@doc(tags=["Catalog"], description="Get tools")
@marshal_with(
    ToolResponseSchema(many=True),
    code=HTTP_CODES.OK,
    description="The tools stored",
)
@app.route("/manager/v1/catalogs/tools", methods=["GET"])
def get_tools():
    response = catalogGetTools()
    return jsonify(json.loads(response["body"])), response["statusCode"]
