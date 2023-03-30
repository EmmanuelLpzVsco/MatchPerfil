import json


class HTTP_CODES:
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405


def Response(headers={}, body=None, statusCode=200) -> dict:
    defaultHeaders = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    }
    headers = defaultHeaders
    headers.update(defaultHeaders)
    if body is None:
        data = {}
    else:
        if isinstance(body, list):
            # TODO: este try-except es temporal, se debe quitar cuando todos los endpoints adopten el uso de mappers
            try:
                data = [obj.serialize() for obj in body]
            except Exception:
                data = body
        else:
            # TODO: este try-except es temporal, se debe quitar cuando todos los endpoints adopten el uso de mappers
            try:
                data = body.serialize()
            except Exception:
                data = body

    body = json.dumps(data)
    statusCode = statusCode
    return {"statusCode": statusCode, "headers": headers, "body": body}
