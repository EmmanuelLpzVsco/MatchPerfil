from src.modules.catalogs.use_case.certification import getCertifications
from src.utils.http import HTTP_CODES, Response


def catalogGetCertifications() -> dict:
    certifications = getCertifications()
    return Response(body=certifications, statusCode=HTTP_CODES.OK)
