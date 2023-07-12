from load_csv import load
import pandas as pd
import numpy as np
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
    # two_countries:list = ['Sweden']
    # two_countries:list = ['Finland']
    data_set_two_countries:pd.DataFrame = data_set
    print('Columns: {}'.format(data_set_two_countries.index))
    # data_set_two_countries = data_set_two_countries.reset_index(drop=True, inplace=False)


    # df = pd.DataFrame(np.random.random_sample((5, 5)))
    # print(df.head())
    # df.plot(y=[0, 2, 4])
    # plt.show()


    # df = pd.DataFrame({
    #     'Name': ['John', 'Sammy', 'Joe'],
    #     'Age': [45, 38, 90]
    # })
    # df.plot(x="Name", y="Age", kind="line")
    # plt.show()
  


    data_set_two_countries:pd.DataFrame = data_set_two_countries.T[two_countries]
    # print(data_set_two_countries.head())
    data_set_two_countries:pd.DataFrame = data_set_two_countries.reset_index(drop=True)
    print(data_set_two_countries)
    # data_set_two_countries:pd.DataFrame = data_set_two_countries.set_index('country')
    plt.xticks(range(0, 300, 40))
    plt.yticks(range(0, 500, 50))
    for country in two_countries:
        plt.plot(data_set_two_countries.index, data_set_two_countries[country], label=country)
    # plt.plot(data_set_two_countries['Sweden'], label='B')
    plt.legend(title='Country')
    # plt.show()


    # print(data_set_two_countries.head())
    # data_set_two_countries.reset_index(inplace=True)
    # print(data_set_two_countries.columns)
    # print(data_set_two_countries[two_countries])
    # data_set_two_countries.plot(x='index', y='Finland')
    # plt.plot(data_set_two_countries.index, data_set_two_countries[two_countries])
    # plt.ylim(0, 300)
    plt.show()

if __name__ == '__main__':
    main()
