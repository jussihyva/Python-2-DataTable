from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import sys

def parse_cmd_params(argv) ->tuple:
    if len(argv) >= 2:
        if str(argv[1]).upper() == '-T':
            trace:bool = True
            year:str = '1900'
            if len(argv) == 3:
                year:str = str(argv[2])
            else:
                year:str = '1900'
        else:
            year:str = str(argv[1])
            trace:bool = False
    else:
        trace:bool = False
        year:str = '1900'
    print(year)
    return (year, trace)


def main(argv):
    '''
A program that loads the files \
"income_per_person_gdppercapita_ppp_inflation_adjusted.csv" and \
"life_expectancy_years.csv", and displays the projection of life expectancy in \
relation to the gross national product of the year 1900 for each country.
    '''
    (year, trace) = parse_cmd_params(argv)
    income_per_person_gdppercapita_ppp_inflation_adjusted:str = 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    life_expectancy_years:str = 'life_expectancy_years.csv'
    df_income:pd.DataFrame = load(income_per_person_gdppercapita_ppp_inflation_adjusted)
    df_life_expectancy:pd.DataFrame = load(life_expectancy_years)
    s_income:pd.Series = pd.Series(df_income[year], name='income')
    s_life_expectancy:pd.Series = pd.Series(df_life_expectancy[year], name='life_expectancy')
    df_income_and_life_expectanc:pd.DataFrame = pd.DataFrame(s_life_expectancy)
    df_income_and_life_expectanc:pd.DataFrame = pd.merge(left=df_income_and_life_expectanc, right=s_income,  left_index=True, right_index=True, how='outer', sort=True)
    fig, ax = plt.subplots()
    ax.set_xscale(value='log')
    df_income_and_life_expectanc.dropna(inplace=True)
    df_income_and_life_expectanc = df_income_and_life_expectanc.astype({'income':int})
    ax.scatter(df_income_and_life_expectanc['income'], df_income_and_life_expectanc['life_expectancy'])
    formatter:EngFormatter = EngFormatter()
    ax.xaxis.set_major_formatter(formatter)
    ax.set_ylabel('Life Expectancy')
    ax.set_xlabel('Gross domestic product')
    ax.set_title(year)
    plt.show()


if __name__ == '__main__':
    print(main.__doc__)
    main(sys.argv)
