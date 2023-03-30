import json
import os


def set_seeders(event, context):
    os.environ["HANDLER_MODE"] = "True"
    import flask_src.migration
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "the providers were executed..."}),
    }
