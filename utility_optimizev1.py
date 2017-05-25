#!user/bin/python
# SIMPLE EMERGENT AGI TEST
# By Jacob Beckerman, jacob [dot] beckerman [at] gmail
# Scene: person is in a closed room with a bed, a glass of water, and a hamburger.
# 		 the hamburger and water are infinitely consumable.

import numpy as np

def utility(sleep, hunger, thirst):
	return (sleep**0.5) + (hunger**0.5) + (thirst**0.5)
def decay_values(sleep, hunger, thirst):
	sleep -= 10
	hunger -= 30
	thirst -= 40

# Initialize with typical morning variables
sleep = 1200
hunger = 600
thirst = 700
# Initialize rate of chance
dsleep = 50
dhunger = 100
dthirst = 110
# Arbitrarily run 1000 iterations of main loop
# Discretized time of 10 minutes
for i in range(1, 1001):
	current_u = utility(sleep, hunger, thirst)
	sleep_choice = utility(sleep + dsleep, hunger, thirst)
	hunger_choice = utility(sleep, hunger + dhunger, thirst)
	thirst_choice = utility(sleep, hunger, thirst + dthirst)

	if sleep_choice >= hunger_choice and sleep_choice >= thirst_choice:
		print "SLEEP"
		sleep += dsleep
	if hunger_choice >= sleep_choice and hunger_choice >= thirst_choice:
		print "EAT"
		hunger += dhunger
	if thirst_choice >= hunger_choice and thirst_choice >= sleep_choice:
		print "DRINK"
		thirst += dthirst

	# Decay values of params
	sleep -= 10
	hunger -= 30
	thirst -= 40

	if sleep <= 0 or hunger <= 0 or thirst <= 0:
		print "Guy died"
		break

	#print "Sleep value: ", sleep
	#print "Hunger value: ", hunger
	#print "Thirst value: ", thirst