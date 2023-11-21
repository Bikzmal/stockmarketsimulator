import matplotlib.pyplot as plt
import numpy as np
import random

# inputs for customization
while True:
	try:
		startingprice = float(input("Enter your desired starting price: "))
		if startingprice < 0:
			print("Please enter a valid number.")
			continue
		break
	except:
		print("Please enter a valid number.")

while True:
	try:
		daysamount = int(input("Enter your desired amount of days to simulate: "))
		if daysamount < 1:
			print("Please enter a valid number.")
			continue
		break
	except:
		print("Please enter a valid number.")

while True:
	try:
		randseed = input("Enter your desired seed (leave empty if you want it to be randomized): ")
		if randseed == "":
			randseed = random.randint(-10000000, 10000000)
		else:
			randseed = int(randseed)
		print(f"Using seed: {randseed}")
		break
	except:
		print("Please enter a valid number or enter nothing.")

# set the seed
random.seed(randseed)

# variables
days = [1]
prices = [startingprice]
max_change = 0.02

# simulate for x amount of days
if daysamount != 1:
	for day in range(2, daysamount+1):
		percentage_change = random.uniform(0, max_change)
	
		# 50% chance to flip the number to a negative number
		if random.randint(0, 1) == 1:
			percentage_change = -percentage_change
	
		new_price = prices[-1] * (1 + percentage_change)
	
		days.append(day)
		prices.append(new_price)

# plot the values and customize
plt.plot(days, prices, label="Simulated Stock Prices")
plt.axhline(y=prices[0], color='gray', linestyle='--', label='First Price')

plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.title("Stock Price Simulation")
plt.legend()
plt.grid(True)

plt.show()
