import os

from src.modules.catalogs.models.entity.programming_language import (
    ProgrammingLanguageModel,
)

programming_languages_data = [
    {"key": "ABAP", "name": "ABAP", "description": "ABAP"},
    {"key": "ASP NET", "name": "ASP NET", "description": "ASP NET"},
    {"key": "ALGOL", "name": "ALGOL", "description": "ALGOL"},
    {"key": "ACTION SCRIPT", "name": "ACTION SCRIPT", "description": "ACTION SCRIPT"},
    {"key": "ADA", "name": "ADA", "description": "ADA"},
    {"key": "APEX", "name": "APEX", "description": "APEX"},
    {"key": "ASSAMBLE X86", "name": "ASSAMBLE X86", "description": "ASSAMBLE X86"},
    {"key": "ASSAMBLE ARM", "name": "ASSAMBLE ARM", "description": "ASSAMBLE ARM"},
    {"key": "B", "name": "B", "description": "B"},
    {"key": "BASH", "name": "BASH", "description": "BASH"},
    {"key": "BASIC", "name": "BASIC", "description": "BASIC"},
    {"key": "BATCH MICROSOFT", "name": "BATCH", "description": "BATCH"},
    {"key": "C", "name": "C", "description": "C"},
    {"key": "C++", "name": "C++", "description": "C++"},
    {"key": "C#", "name": "C#", "description": "C#"},
    {"key": "C SHELL", "name": "C SHELL", "description": "C SHELL"},
    {"key": "CL", "name": "CL", "description": "CL"},
    {"key": "CLOJURE", "name": "CLOJURE", "description": "CLOJURE"},
    {"key": "COBOL", "name": "COBOL", "description": "COBOL"},
    {"key": "COFFE SCRIPT", "name": "COFFE SCRIPT", "description": "COFFE SCRIPT"},
    {"key": "LISP", "name": "LISP", "description": "LISP"},
    {"key": "D", "name": "D", "description": "D"},
    {"key": "DART", "name": "DART", "description": "DART"},
    {"key": "DARWIN", "name": "DARWIN", "description": "DARWIN"},
    {"key": "DBASE", "name": "DBASE", "description": "DBASE"},
    {"key": "DELPHI", "name": "DELPHI", "description": "DELPHI"},
    {"key": "ECMA SCRIPT", "name": "ECMA SCRIPT", "description": "ECMA SCRIPT"},
    {"key": "EIFFEL", "name": "EIFFEL", "description": "EIFFEL"},
    {"key": "ELIXIR", "name": "ELIXIR", "description": "ELIXIR"},
    {"key": "ELM", "name": "ELM", "description": "ELM"},
    {"key": "ERLANG", "name": "ERLANG", "description": "ERLANG"},
    {"key": "F", "name": "F", "description": "F"},
    {"key": "F#", "name": "F#", "description": "F#"},
    {"key": "F*", "name": "F*", "description": "F*"},
    {"key": "FACTOR", "name": "FACTOR", "description": "FACTOR"},
    {"key": "FLEX", "name": "FLEX", "description": "FLEX"},
    {"key": "FORMULA", "name": "FORMULA", "description": "FORMULA"},
    {"key": "FORTRAN", "name": "FORTRAN", "description": "FORTRAN"},
    {"key": "FORTRESS", "name": "FORTRESS", "description": "FORTRESS"},
    {"key": "F-SCRIPT", "name": "F-SCRIPT", "description": "F-SCRIPT"},
    {"key": "GAME MAKER", "name": "GAME MAKER", "description": "GAME MAKER"},
    {"key": "GO", "name": "GO", "description": "GO"},
    {
        "key": "GOOGLE APPS SCRIPT",
        "name": "GOOGLE APPS SCRIPT",
        "description": "GOOGLE APPS SCRIPT",
    },
    {"key": "GROOVY", "name": "GROOVY", "description": "GROOVY"},
    {"key": "HACK", "name": "HACK", "description": "HACK"},
    {"key": "HASKELL", "name": "HASKELL", "description": "HASKELL"},
    {"key": "J", "name": "J", "description": "J"},
    {"key": "J#", "name": "J#", "description": "J#"},
    {"key": "J++", "name": "J++", "description": "J++"},
    {"key": "JADE", "name": "JADE", "description": "JADE"},
    {"key": "JAVA", "name": "JAVA", "description": "JAVA"},
    {"key": "JAVASCRIPT", "name": "JAVASCRIPT", "description": "JAVACRIPT"},
    {"key": "JSCRIPT", "name": "JSCRIPT", "description": "JSCRIPT"},
    {"key": "JYTHON", "name": "JYTHON", "description": "JYTHON"},
    {"key": "K", "name": "K", "description": "K"},
    {"key": "KOTLIN", "name": "KOTLIN", "description": "KOTLIN"},
    {"key": "KORN SHELL", "name": "KORN SHELL", "description": "KORN SHELL"},
    {"key": "LABVIEW", "name": "LABVIEW", "description": "LABVIEW"},
    {"key": "LINQ", "name": "LINQ", "description": "LINQ"},
    {"key": "LOGO", "name": "LOGO", "description": "LOGO"},
    {"key": "LUA", "name": "LUA", "description": "LUA"},
    {"key": "MATLAB", "name": "MATLAB", "description": "MATLAB"},
    {
        "key": "MASM (MACRO ASSAMBLER)",
        "name": "MASM (MACRO ASSAMBLER)",
        "description": "MASM",
    },
    {"key": "MODULA", "name": "MODULA", "description": "MODULA"},
    {"key": "NASM", "name": "NASM", "description": "NASM"},
    {
        "key": "NOT QUITE C (C language for Lego Mindstorm)",
        "name": "NOT QUITE C (C language for Lego Mindstorm)",
        "description": "NQC",
    },
    {"key": "OBJECT LISP", "name": "OBJECT LISP", "description": "OBJECT LISP"},
    {"key": "PASCAL", "name": "PASCAL", "description": "PASCAL"},
    {"key": "OBJECTIVE-C", "name": "OBJECTIVE-C", "description": "OBJECTIVE-C"},
    {"key": "OBJECTIVE-J", "name": "OBJECTIVE-J", "description": "OBJECTIVE-J"},
    {"key": "P", "name": "P", "description": "P"},
    {"key": "PHP", "name": "PHP", "description": "PHP"},
    {"key": "PICO", "name": "PICO", "description": "PICO"},
    {"key": "PERL", "name": "PERL", "description": "PERL"},
    {"key": "PLC", "name": "PLC", "description": "PLC"},
    {"key": "POWERSHELL", "name": "POWERSHELL", "description": "POWERSHELL"},
    {
        "key": "PROCESSING (ARDUINO)",
        "name": "PROCESSING (ARDUINO)",
        "description": "PROCESSING",
    },
    {"key": "MICRO PYTHON", "name": "MICRO PYTHON", "description": "MICRO PYTHON"},
    {"key": "PYTHON", "name": "PYTHON", "description": "PYTHON"},
    {"key": "R", "name": "R", "description": "R"},
    {"key": "RUBY", "name": "RUBY", "description": "RUBY"},
    {"key": "SIMULA", "name": "SIMULA", "description": "SIMULA"},
    {"key": "SMALLTALK", "name": "SMALLTALK", "description": "SMALLTALK"},
    {"key": "SQL", "name": "SQL", "description": "SQL"},
    {"key": "NoSQL", "name": "NoSQL", "description": "NoSQL"},
    {"key": "SWIFT", "name": "SWIFT", "description": "SWIFT"},
    {"key": "TeX", "name": "TeX", "description": "TEX"},
    {"key": "TYPESCRIPT", "name": "TYPESCRIPT", "description": "TYPESCRIPT"},
    {"key": "SHELL", "name": "SHELL", "description": "SHELL"},
    {"key": "UNITY", "name": "UNITY", "description": "UNITY"},
    {"key": "VHDL", "name": "VHDL", "description": "VHDL"},
    {"key": "VISUAL FOXPRO", "name": "VISUAL FOXPRO", "description": "VISUAL FOXPRO"},
    {"key": "VISUAL J++", "name": "VISUAL J++", "description": "VISUAL J++"},
    {
        "key": "VISUAL BASIC 6",
        "name": "VISUAL BASIC 6",
        "description": "VISUAL BASIC 6",
    },
    {
        "key": "VISUAL BASIC .NET",
        "name": "VISUAL BASIC .NET",
        "description": "VISUAL BASIC .NET",
    },
]


def migrate_programming_languages():
    if not ProgrammingLanguageModel.exists() or os.environ.get("HANDLER_MODE"):
        if not ProgrammingLanguageModel.exists():
            ProgrammingLanguageModel.create_table(
                read_capacity_units=1, write_capacity_units=1, wait=True
            )
        for data in programming_languages_data:
            programmingLanguage = ProgrammingLanguageModel(
                key=data["key"], name=data["name"], description=data["description"]
            )
            programmingLanguage.save()
