import matplotlib.pyplot as plt
import numpy as np

import pathlib


#read csv


#find files in directory
def find_csv_files(directory) -> list:
    result = []
    for f_name in pathlib.Path(directory).iterdir():
        if f_name.name.endswith('.csv'):
            result.append(f_name)
    return result


if __name__ == '__main__':
    files = find_csv_files(pathlib.Path().resolve())
    arr_data = []
    arr_data.append([3, 7, 1, 1, 4])
    arr_data.append([4, 6, 1, 1, 6])
    arr_data.append([3, 7, 1, 3, 5])
    arr_data.append([6, 3, 7, 1, 5])
    arr_data.append([3, 7, 6, 1, 2])


    # Data
    groups = ['G1', 'G2', 'G3', 'G4', 'G5']
    values1 = [12, 19, 14, 27, 16]
    values2 = [21, 30, 15, 17, 20]
    values3 = [15, 23, 12, 11, 15]

    fig, ax = plt.subplots()

    # Stacked bar chart
    ax.bar(groups, values1)
    ax.bar(groups, values2, bottom=values1)
    ax.bar(groups, values3, bottom=np.add(values1, values2))

    plt.savefig('test', format='png')


