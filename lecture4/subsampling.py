# take a list of sensor values
# return every 2nd, for the first half 
sensor = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
# should output [3.2, 2.8, 6.4]
print(sensor[ : 1 + (len(sensor) // 2) : 2] )