from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    '''
    A program that calls the load function from the previous exercise, loads the file life_expectancy_years.csv, and displays the country information of your campus.
    '''
    data_set:pd.DataFrame = load('life_expectancy_years.csv')
    country:str = 'Finland'
    data_set_country:pd.Series = data_set.loc[country]
    plt.plot(data_set_country)
    plt.title('{} Life expectancy Projections'.format(country))
    plt.ylabel('Life expectancy (years)')
    plt.xlabel('Years')
    plt.xticks(range(0, 300, 40))
    plt.show()


if __name__ == '__main__':
    main()
