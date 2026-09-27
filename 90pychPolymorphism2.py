class Employee:
    def work(self):
        print('Employee is working')

class Developer(Employee):
    def work(self):
        print('Developer is working')

class Tester(Employee):
    def work(self):
        print('Tester is Testing')

class Manager(Employee):
    def work(self):
        print('Manager is Managing')

employee=[Developer(),Tester(),Manager()]
for emp in employee:
    emp.work()