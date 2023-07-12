from load_csv import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

def convert(value):
    m = re.match('^([\d\.]+)M$', str(value))
    if not m is None:
        value:float = float(m.group(1)) * 1000000
    else:
        m = re.match('^([\d\.]+)k$', str(value))
        if not m is None:
            value:float = float(m.group(1)) * 1000
    print('value: {}'.format(str(value)))
    return value

def convert_row(row:pd.Series):
    row = row.map(convert)
    print('ROW: {}'.format(str(row)))
    return row

def main():
    '''
    A program that calls the load function from the first exercise, loads the file population_total.csv, and displays the country information of your campus versus other country of your choice
    '''
    path:str = 'population_total.csv'
    data_set:pd.DataFrame = load(path)
    # data_set.reset_index(inplace=True)
    print(data_set.head())
    data_set = data_set.apply(convert_row)
    print(data_set.dtypes)
    two_countries:list = ['Finland', 'Sweden']
    # two_countries:list = ['Sweden']
    # two_countries:list = ['Finland']
    data_set_two_countries:pd.DataFrame = data_set.loc[two_countries]
    print(data_set_two_countries.dtypes)
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
  


    # data_set_two_countries:pd.DataFrame = data_set_two_countries.T[two_countries]
    print(data_set_two_countries.head())
    # data_set_two_countries:pd.DataFrame = data_set_two_countries.reset_index(drop=True)
    data_set_two_countries:pd.DataFrame = data_set_two_countries.T
    data_set_two_countries['Sweden'] = data_set_two_countries['Sweden'].astype(float)
    print(data_set_two_countries.head())
    # pd.to_numeric(data_set_two_countries['Sweden'])
    print(data_set_two_countries.dtypes)
    # data_set_two_countries:pd.DataFrame = data_set_two_countries.set_index('country')
    plt.xticks(range(0, 300, 40))
    plt.yticks(range(0, 500, 50))
    for i in range(len(two_countries)):
        country:str = two_countries[i]
        print(country)
        # plt.plot(data_set_two_countries[country], label=country)

    # data_set_two_countries:pd.DataFrame = pd.DataFrame({0: [8000000000, 815, 831, 847, 863],
    #                                                     1: [2.5, 2.49, 2.48, 2.47, 2.46]})


    data_set_two_countries:pd.DataFrame = data_set_two_countries.reset_index()
    print(data_set_two_countries.head())
    print(data_set_two_countries.dtypes)
    print(type(data_set_two_countries))
    sns.lineplot(data=data_set_two_countries, x='index', y='Sweden')
    sns.lineplot(data=data_set_two_countries, x='index', y='Finland')
    # sns.lineplot(data=data_set_two_countries[two_countries])
    # data_set_two_countries.plot()
    # plt.legend(title='Country')
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
