km = int(input('Enter Distance in km: '))
met = km * 1000
print('Distance in meter: ',met)
print('-----------------------')
mt=int(input('Enter Distance in met: '))
km = mt/1000
print('Distance in km: ',km)

print('------------------------')

th = int(input('Enter time in hours: '))
min = th*60
sec = min*60
print('time in min: ',min)
print('time in sec: ',sec)

print('---------------------------------')

min = int(input('Enter Time in min: '))
h = min/60
sec = 60*min
print('Time in hr: ',h)
print('Time in sec: ',sec)


print('-----------------------------------')


sec = int(input('Enter time in sec: '))
min = sec/60
hr = min/60
print('Time in min: ',min)
print('Time in hr: ',hr)
