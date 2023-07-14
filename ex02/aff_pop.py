from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import re

def convert(value):
    m = re.match('^([\d\.]+)M$', str(value))
    if not m is None:
        value:float = float(m.group(1)) * 1000000
    else:
        m = re.match('^([\d\.]+)k$', str(value))
        if not m is None:
            value:float = float(m.group(1)) * 1000
    return value

def convert_row(row:pd.Series):
    row = row.map(convert)
    return row

def main():
    '''
    A program that calls the load function from the first exercise, loads the file population_total.csv, and displays the country information of your campus versus other country of your choice
    '''
    path:str = 'population_total.csv'
    data_set:pd.DataFrame = load(path)
    print(data_set.head())
    data_set = data_set.apply(convert_row)
    two_countries:list = ['Finland', 'Sweden']
    data_set_two_countries:pd.DataFrame = data_set.loc[two_countries]
    data_set_two_countries:pd.DataFrame = data_set_two_countries.T
    print('{}'.format(data_set_two_countries.head()))
    data_set_two_countries:pd.DataFrame = data_set_two_countries.loc['1800':'2040']
    # data_set_two_countries:pd.DataFrame = data_set_two_countries.reset_index(drop=True)
    print('{}'.format(data_set_two_countries.head()))
    data_set_two_countries.plot(y=two_countries)
    plt.title('Population projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.xticks(range(0, 300, 40))
    plt.show()

if __name__ == '__main__':
    main()
