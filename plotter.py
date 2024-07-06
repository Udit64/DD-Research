import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
def plot_eeg_vs_mean_k(csv_file):
    eeg_values = []
    mean_k_values = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            eeg_values.append(float(row['eeg_value']))
            mean_k_values.append(float(row['mean_k']))
    x=np.array(mean_k_values)
    y=np.array(eeg_values)
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    best_fit_line = slope * x + intercept
    # plt.scatter(mean_k_values,eeg_values, marker='o')
    
    # plt.grid(True)
    # plt.show()
    plt.scatter(x, y, label='Data Points')
    plt.plot(x, best_fit_line, color='red', label='Best Fit Line')
    plt.ylabel('EEG Value')
    plt.xlabel('Mean_k')
    plt.title('EEG Value vs. Mean_k')
    # plt.xlabel('Independent Variable (x)')
    # plt.ylabel('Dependent Variable (y)')
    plt.legend()
    plt.grid(True)
    plt.show()
    

csv_file = "eeg_values.csv"
plot_eeg_vs_mean_k(csv_file)
