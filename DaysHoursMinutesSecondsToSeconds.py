# Algorithm that reads the quantity of days, hours, minutes and seconds of the user, and then calculates the total in seconds. 

d = int(input('Days: '))
h = int(input('Hours: '))
m = int(input('Minutes: '))
s = int(input('Seconds: '))

total = d*24*60*60 + h*60*60 + m*60 + s
print (f' {total} Seconds ')
