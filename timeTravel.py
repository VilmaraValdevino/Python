#Calculates the time of a car trip.
#Requests the distance to be traveled and the average speed expected for the trip.

d = float(input('Distance km: '))
s = float(input('average speed km/h: '))
t = d / s
print (f'Time: {t:.1f}')
