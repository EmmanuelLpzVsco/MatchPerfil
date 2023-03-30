import os

if not os.environ.get("HANDLER_MODE"):
    os.environ["DYNAMODB_TABLE_PROFILES"] = "profiles"
    os.environ["DYNAMODB_TABLE_CLIENTS"] = "clients"
    os.environ["DYNAMODB_TABLE_PROFILE_STATUS"] = "profile_status"
    os.environ["DYNAMODB_TABLE_PROGRAMMING_LANGUAGES"] = "programming_languages"
    os.environ["DYNAMODB_TABLE_FRAMEWORKS"] = "frameworks"
    os.environ["DYNAMODB_TABLE_LIBRARIES"] = "libraries"
    os.environ["DYNAMODB_TABLE_COURSES"] = "courses"
    os.environ["DYNAMODB_TABLE_TOOLS"] = "tools"
    os.environ["DYNAMODB_TABLE_CERTIFICATIONS"] = "certifications"

    os.environ["DYNAMODB_HOST"] = "http://dynamodb:8000"
