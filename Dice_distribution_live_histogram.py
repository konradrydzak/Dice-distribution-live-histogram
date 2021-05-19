import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as mtick

number_of_dice = int(input("How many dice?\n"))
max_trials = int(input("How many trials?\n"))
interval = int(input("What's the interval between updating the plot?\n"))
max_value = 5 * number_of_dice + 1  # Because the minimal value is sum of ones and there can't be a lower value
results = [0] * max_value
calculated_results = [0] * max_value
t = np.arange(number_of_dice, max_value + number_of_dice)

for i in range(max_trials):
    result = 0
    for die in range(number_of_dice):
        result += np.random.randint(1, 6 + 1)
    results[result - number_of_dice] += 1
    if (i + 1) % interval == 0:
        os.system('cls')
        print(f"Results after {i + 1} iterations:")
        for j in range(max_value):
            calculated_results[j] = round(results[j] / (i + 1) * 100, 3)
            print(str(j + number_of_dice) + ': ' + str(calculated_results[j]) + '%')
        plt.clf()
        plt.plot(t, calculated_results, 'bo')
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
        plt.grid(True)
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        plt.minorticks_on()
        plt.ion()
        plt.pause(0.01)
        plt.show()
input("\nPress any key to exit")
