from load_csv import load

input_data_list = [
    {'path': 'life_expectancy_years.csv', 'is_input_valid': True},
    {'path': 'load_csv.py', 'is_input_valid': False}
]

for input_data in input_data_list:
    path:str = input_data['path']
    print(load(path))
