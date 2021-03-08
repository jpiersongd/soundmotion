# Generate a random number series between 0 and 100 and call the soundware function

import time
from random import *

val1 = 0
play = True

def play_soundware():
	print(val1)
	
	
def get_agg_accel():
	global val1
	#decide if adding or subtracting
	variance1 = randint(1,2)
	#decide how much
	variance2 = randint(0,10)

	# subtract some amount
	if variance1 ==1 and val1 - variance2 >= 0:
		val1 = val1 - variance2
	# add some amount
	if variance1 > 1 and val1 + variance2 <=100:
		val1 = val1 + variance2
	
	
while play == True:
	get_agg_accel()
	play_soundware()
	time.sleep(.1)
