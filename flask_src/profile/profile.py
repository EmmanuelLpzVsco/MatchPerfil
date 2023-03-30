import os
from datetime import datetime

from src.modules.profiles.models.entity.achievement import AchievementMap
from src.modules.profiles.models.entity.certification import (
    CertificationMap as ProfileCertificationMap,
)
from src.modules.profiles.models.entity.course import CourseMap as ProfileCourseMap
from src.modules.profiles.models.entity.framework import (
    FrameworkMap as ProfileFrameworkMap,
)
from src.modules.profiles.models.entity.job import JobMap as ProfileJobMap
from src.modules.profiles.models.entity.profile import ProfileModel
from src.modules.profiles.models.entity.programming_language import (
    ProgrammingLanguageMap as ProfileProgrammingLanguageMap,
)
from src.modules.profiles.models.entity.study_level import (
    StudyLevelMap as ProfileStudyLevelMap,
)
from src.modules.profiles.models.entity.tool import ToolMap as ProfileToolMap

profile_data = [
    {
        "id": "e36c6ed4-74ab-11eb-9439-0242ac130002",
        "birthDay": "1988-04-04",
        "curp": "RORL880404MDFNZB04",
        "email": "bluedrayco@gmail.com",
        "extNumber": 1,
        "intNumber": 45,
        "firstName": "Roberto Leroy",
        "gender": "H",
        "lastName": "Monroy Ruiz",
        "rfc": "MORR890908DT4",
        "street": "Don Pascuale",
        "zipCode": "13200",
        "studyLevels": [
            {
                "id": "063c69aa-74ac-11eb-9439-0242ac130002",
                "degree": "University",
                "school": "Escuela superior de computo ESCOM",
                "entryMonth": 7,
                "exitMonth": 7,
                "entryYear": 2008,
                "exitYear": 2012,
            }
        ],
        "certifications": [
            {
                "certificationId": "SCRUM",
                "folio": "12345678",
                "institution": "Scrum-Academy",
                "validUntil": "2021-09-25",
            }
        ],
        "programmingLanguages": [
            {"programmingLanguageId": "PHP", "experienceInYears": 5},
            {"programmingLanguageId": "JAVA", "experienceInYears": 3},
            {"programmingLanguageId": "PYTHON", "experienceInYears": 2},
        ],
        "tools": [
            {"toolId": "VAGRANT", "experienceInYears": 5},
            {"toolId": "DOCKER", "experienceInYears": 3},
            {"toolId": "DOCKER-COMPOSE", "experienceInYears": 2},
        ],
        "frameworks": [
            {"frameworkId": "TSP", "experienceInYears": 2},
            {"frameworkId": "SYMFONY", "experienceInYears": 4},
            {"frameworkId": "SLIMPHP", "experienceInYears": 6},
        ],
        "courses": [
            {"courseId": "SCRUM", "institution": "SCRUM ACADEMY", "date": "2022-01-12"},
            {
                "courseId": "JAVA-CERTIFICATION",
                "institution": "ORACLE ACADEMY",
                "date": "2020-09-08",
            },
        ],
        "jobs": [
            {
                "id": "1620a3c2-74ac-11eb-9439-0242ac130002",
                "company": "Enova",
                "position": "Software Architect",
                "department": "Software development",
                "entryMonth": 1,
                "exitMonth": 12,
                "entryYear": 2018,
                "exitYear": 2019,
                "achievements": [
                    {
                        "id": "49467d3a-74ac-11eb-9439-0242ac130002",
                        "achievement": "logro1",
                    },
                    {
                        "id": "5c884b30-74ac-11eb-9439-0242ac130002",
                        "achievement": "logro2",
                    },
                ],
            }
        ],
    },
    {
        "id": "25aa596e-74ac-11eb-9439-0242ac130002",
        "birthDay": "1988-04-04",
        "curp": "RORL880404MDFNZB04",
        "email": "iscprincess@gmail.com",
        "extNumber": 1,
        "intNumber": 45,
        "firstName": "Lourdes Gabriela",
        "gender": "M",
        "lastName": "Rodriguez Rodriguez",
        "rfc": "RORL880404TQ3",
        "street": "Silos",
        "zipCode": "13300",
        "studies": [
            {
                "id": "309f6bca-74ac-11eb-9439-0242ac130002",
                "degree": "University",
                "school": "Escuela superior de computo ESCOM",
                "entryMonth": 7,
                "exitMonth": 7,
                "entryYear": 2008,
                "exitYear": 2012,
            }
        ],
    },
]


def migrate_profiles():
    if not ProfileModel.exists() or os.environ.get("HANDLER_MODE"):
        if not ProfileModel.exists():
            ProfileModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )
        for data in profile_data:
            # logging.error(json.dumps(data))
            courses = []
            if "courses" in data:
                for course in data["courses"]:
                    course_date = datetime.strptime(course["date"], "%Y-%m-%d")
                    courseObj = ProfileCourseMap(
                        courseId=course["courseId"],
                        institution=course["institution"],
                        date=course_date,
                    )
                    courses.append(courseObj)
            else:
                courses = None
            programmingLanguages = []
            if "programmingLanguages" in data:
                for programmingLanguage in data["programmingLanguages"]:
                    programmingLanguageObj = ProfileProgrammingLanguageMap(
                        programmingLanguageId=programmingLanguage[
                            "programmingLanguageId"
                        ],
                        experienceInYears=programmingLanguage["experienceInYears"],
                    )
                    programmingLanguages.append(programmingLanguageObj)
            else:
                programmingLanguages = None
            tools = []
            if "tools" in data:
                for tool in data["tools"]:
                    toolObj = ProfileToolMap(
                        toolId=tool["toolId"],
                        experienceInYears=tool["experienceInYears"],
                    )
                    tools.append(toolObj)
            else:
                tools = None
            frameworks = []
            if "frameworks" in data:
                for framework in data["frameworks"]:
                    frameworkObj = ProfileFrameworkMap(
                        frameworkId=framework["frameworkId"],
                        experienceInYears=framework["experienceInYears"],
                    )
                    frameworks.append(frameworkObj)
            else:
                frameworks = None
            studies = []
            if "studies" in data:
                for study in data["studies"]:
                    studyObj = ProfileStudyLevelMap(
                        id=study["id"],
                        degree=study["degree"],
                        school=study["school"],
                        entryMonth=study["entryMonth"],
                        exitMonth=study["exitMonth"],
                        entryYear=study["entryYear"],
                        exitYear=study["exitYear"],
                    )
                    studies.append(studyObj)
            else:
                studies = None
            jobs = []
            if "jobs" in data:
                for job in data["jobs"]:
                    achievements = []
                    for achievement in job["achievements"]:
                        achievementObj = AchievementMap(
                            id=achievement["id"], achievement=achievement["achievement"]
                        )
                        achievements.append(achievementObj)
                    jobObj = ProfileJobMap(
                        id=job["id"],
                        company=job["company"],
                        position=job["position"],
                        department=job["department"],
                        entryMonth=job["entryMonth"],
                        exitMonth=job["exitMonth"],
                        entryYear=job["entryYear"],
                        exitYear=job["exitYear"],
                        achievements=achievements,
                    )
                    jobs.append(jobObj)
            else:
                jobs = None
            certifications = []
            if "certifications" in data:
                for certification in data["certifications"]:
                    certificationObj = ProfileCertificationMap(
                        certificationId=certification["certificationId"],
                        folio=certification["folio"],
                        institution=certification["institution"],
                        validUntil=certification["validUntil"],
                    )
                    certifications.append(certificationObj)
            else:
                certifications = None

            date_time_str = data["birthDay"]
            date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d")
            birthDay = date_time_obj

            profile = ProfileModel(
                id=data["id"],
                birthDay=birthDay,
                curp=data["curp"],
                email=data["email"],
                extNumber=data["extNumber"],
                intNumber=data["intNumber"],
                firstName=data["firstName"],
                gender=data["gender"],
                lastName=data["lastName"],
                rfc=data["rfc"],
                street=data["street"],
                zipCode=data["zipCode"],
                studies=studies,
                jobs=jobs,
                programmingLanguages=programmingLanguages,
                courses=courses,
                certifications=certifications,
                tools=tools,
                frameworks=frameworks,
            )
            profile.save()
