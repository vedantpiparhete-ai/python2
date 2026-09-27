import re
username = [
    "Vedant\n"
    "Student\n"
    "CM25121\n"
    "SBJIT.EDU2026\n"
    "vedantp.ml25@sbjit.edu.in\n"
]
for uname in username:
    if re.fullmatch(r'[a-zA-Z0-9_]{5,15}',uname):
        print(uname,'Valid')
    else:
        print(uname,'Invalid')

# Employee ID start with EMP followed by exactly 4 digits.