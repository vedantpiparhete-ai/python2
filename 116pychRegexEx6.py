import re
empcode= ['Emp0022','EMP12','EM1234','1234']
for emp in empcode:
    if re.fullmatch(r'EMP\d{4}',emp):
        print(emp,'Valid')
    else:
        print(emp,'Invalid')