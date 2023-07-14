from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import sys

def format_number(value,  pos):
    if value >= 1000000:
        formatter = '{:1.1f}M'.format(value*0.000_001)
    elif value >= 1000:
        formatter = '{:1.0f}K'.format(value*0.001)
    else:
        formatter = '{:1.0f}'.format(value)
    return formatter


def main(argv):
    '''
    A program that calls the load function from the first exercise, loads the file population_total.csv, and displays the country information of your campus versus other country of your choice
    '''
    path:str = 'population_total.csv'
    list_all_countries:bool = False
    if len(argv) == 1:
        selected_countries:list = ['Finland', 'Sweden']
    elif len(argv) == 2 and str(argv[1]).upper() == 'ALL':
        list_all_countries:bool = True
    else:
        selected_countries:list = list()
        for country in argv[1:]:
            selected_countries.append(country)
    data_set:pd.DataFrame = load(path)
    if list_all_countries is True:
        for country in list(data_set.index):
            print(country)
    else:
        data_set_selected_countries:pd.DataFrame = data_set.loc[selected_countries]
        data_set_selected_countries:pd.DataFrame = data_set_selected_countries.T
        data_set_selected_countries.index = data_set_selected_countries.index.astype(int, copy=False)
        data_set_selected_countries = data_set_selected_countries.sort_index()
        data_set_selected_countries:pd.DataFrame = data_set_selected_countries.loc[1800:2040]
        ax = data_set_selected_countries.plot()
        ax.yaxis.set_major_formatter(format_number)
        (y_min, y_max) = ax.get_ylim()
        (x_min, x_max) = ax.get_xlim()
        plt.legend(loc='lower right')
        formatter:FuncFormatter = FuncFormatter(format_number)
        plt.title('Population projections')
        plt.ylabel('Population')
        plt.xlabel('Year')
        plt.xticks(range(int(1800), 2040 + 1, 40))
        plt.yticks(range(0, int(y_max) + 1, int(y_max / 4)))
        plt.show()

if __name__ == '__main__':
    main(sys.argv)
