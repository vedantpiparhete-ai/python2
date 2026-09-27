stu ={"Name": "Vedant", "Age": 20, "Course": "Python"}
print('All Keys: ',stu.keys())
print('All Values: ',stu.values())
print('All Enteries: ',stu.items())
print(stu.get('College','Not found')) # not found is for which things are not available in there it will display it or availabe.
# It will not display that it will display the perticular value
stu.update({"Age": 23,"city": "Nagpur"})
print(stu)