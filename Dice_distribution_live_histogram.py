import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

if __name__ == "__main__":
    number_of_dice = int(input("How many dice?\n"))
    max_trials = int(input("How many trials?\n"))
    interval = int(input("What's the interval between updating the plot?\n"))
    max_value = 5 * number_of_dice + 1  # Excluding not possible values
    results = [0] * max_value
    calculated_results = [0] * max_value
    t = np.arange(start=number_of_dice, stop=max_value + number_of_dice)

    for i in range(max_trials):
        result = 0
        result = np.sum(np.random.randint(low=1, high=6 + 1, size=number_of_dice))
        results[result - number_of_dice] += 1
        if (i + 1) % interval == 0:
            os.system('cls')
            print(f"Results after {i + 1} iterations:")
            for j in range(max_value):
                calculated_results[j] = round(number=results[j] / (i + 1) * 100, ndigits=3)
                print(str(j + number_of_dice) + ': ' + str(calculated_results[j]) + '%')
            plt.clf()
            plt.plot(t, calculated_results, 'bo')
            plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
            plt.grid(b=True)
            plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
            plt.minorticks_on()
            plt.ion()
            plt.pause(0.01)
            plt.show()
    input("\nPress any key to exit")
