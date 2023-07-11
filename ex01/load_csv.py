import pandas as pd

def load(path: str) -> pd.DataFrame:
    '''
    A function that takes a path as argument, writes the dimensions of the data set and returns it.
    '''
    try:
        data_set:pd.DataFrame = pd.read_csv(path, index_col=0)
        print('Loading dataset of dimensions {}'.format(data_set.shape))
    except Exception as e:
        print('{}: {}'.format(type(e).__name__, str(e)))
        data_set:pd.DataFrame = pd.DataFrame()
    return data_set
