import pandas as pd


def convert(value):
    last_char:str = str(value[-1])
    if last_char == 'M':
        value:float = float(value[0:-1]) * 1000000
    elif last_char == 'k':
        value:float = float(value[0:-1]) * 1000
    elif last_char == 'B':
        value:float = float(value[0:-1]) * 1000000000
    else:
        value:float = float(value)
    return value


def convert_row(row:pd.Series):
    row = row.map(convert)
    return row


def load(path: str) -> pd.DataFrame:
    '''
    A function that takes a path as argument, writes the dimensions of the data set and returns it.
    '''
    try:
        data_set:pd.DataFrame = pd.read_csv(path, index_col=0)
        data_set = data_set.apply(convert_row)
        print('Loading dataset of dimensions {}'.format(data_set.shape))
    except Exception as e:
        print('{}: {}'.format(type(e).__name__, str(e)))
        data_set:pd.DataFrame = pd.DataFrame()
    return data_set
