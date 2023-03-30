import os

from src.modules.catalogs.models.entity.framework import FrameworkModel

frameworks_data = [
    {
        "key": "LARAVEL",
        "name": "LARAVEL",
        "description": "Artisan framework for PHP",
        "programmingLanguageId": "PHP",
        "isSoftware": True,
    },
    {
        "key": "SCRUM",
        "name": "Scrum",
        "description": "Agile framework",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "PSP",
        "name": "Personal Software Process",
        "description": "Personal Software Progress",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "TSP",
        "name": "Team Software Process",
        "description": "Team Software Progress",
        "programmingLanguageId": None,
        "isSoftware": False,
    },
    {
        "key": "SYMFONY",
        "name": "Symfony Framework",
        "description": "Symfony Framework",
        "programmingLanguageId": "PHP",
        "isSoftware": True,
    },
    {
        "key": "SLIMPHP",
        "name": "Slim Framework",
        "description": "Microframework for create Rest APIs",
        "programmingLanguageId": "PHP",
        "isSoftware": True,
    },
    {
        "key": "MONORAIL",
        "name": "Mono Rail",
        "description": "Framework for ASP .NET",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "ASP.NET",
        "name": "ASP.NET",
        "description": "is a free web framework for building great web sites and applications",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "COALESCE",
        "name": "Coalesce",
        "description": "Coalesce is a framework for rapid-development of ASP.NET Core web applications.",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "FUBUMVC",
        "name": "FubuMVC",
        "description": "A front-controller style MVC framework for .NET",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "NANCYFX",
        "name": "NancyFx",
        "description": "Lightweight, low-ceremony, framework for building HTTP-based services on .NET and Mono",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "IISNODE",
        "name": "IISNode",
        "description": "Host Node.js applications in IIS",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "SUAVE.IO",
        "name": "Suave.IO",
        "description": "Framework/library/web server that makes you cry tears of joy after finishing your project ahead-of-time when you look at the beautiful code you've written in F#.",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "DOTVVM",
        "name": "DotVVM",
        "description": "MVVM framework for people who don't like to write JavaScript, with OWIN and ASP.NET Core support and a free extension for Visual Studio 2015 and 2017.",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "GIRAFFE",
        "name": "Giraffe",
        "description": "Functional (F#) ASP.NET Core micro framework for building rich web applications",
        "programmingLanguageId": "ASP .NET",
        "isSoftware": True,
    },
    {
        "key": "The C++ REST SDK",
        "name": "The C++ REST SDK code name CASABLANCA",
        "description": "Rest framework for C++",
        "programmingLanguageId": "C++",
        "isSoftware": True,
    },
    {
        "key": "PHOENIX",
        "name": "phoenix framework for elixir",
        "description": "Rest framework for elixir",
        "programmingLanguageId": "ELIXIR",
        "isSoftware": True,
    },
    {
        "key": "SNAP",
        "name": "Snap framework for Haskell",
        "description": "Rest framework for haskell",
        "programmingLanguageId": "ELIXIR",
        "isSoftware": True,
    },
    {
        "key": "FOUNDATION",
        "name": "Foundation framework for frontend",
        "description": "Framework for html and javascript",
        "programmingLanguageId": "CSS",
        "isSoftware": True,
    },
    {
        "key": "BOOTSTRAP",
        "name": "Bootstrap framework for frontend",
        "description": "Framework for html, css y javascript",
        "programmingLanguageId": "CSS",
        "isSoftware": True,
    },
]


def migrate_frameworks():
    if not FrameworkModel.exists() or os.environ.get("HANDLER_MODE"):
        if not FrameworkModel.exists():
            FrameworkModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )
        for data in frameworks_data:
            framework = FrameworkModel(**data)
            framework.save()
