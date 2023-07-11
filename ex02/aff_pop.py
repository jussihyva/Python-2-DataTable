from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main():
    '''
    A program that calls the load function from the first exercise, loads the file population_total.csv, and displays the country information of your campus versus other country of your choice
    '''
    path:str = 'population_total.csv'
    data_set:pd.DataFrame = load(path)
    # data_set.reset_index(inplace=True)
    print(data_set.head())
    two_countries:list = ['Finland', 'Sweden']
    # two_countries:list = ['country', 'France', 'Sweden']
    data_set_two_countries:pd.DataFrame = data_set.loc[two_countries].T
    data_set_two_countries = data_set_two_countries.reset_index(drop=True, inplace=False)
    print(data_set_two_countries.head())
    print(data_set_two_countries.columns)
    data_set_two_countries.plot(y=two_countries)
    plt.xticks(range(0, 300, 40))
    plt.yticks(range(0, 100, 50))
    plt.ylim(0, 300)
    plt.show()

if __name__ == '__main__':
    main()
