import json

from minerals.models import Mineral


def parse_colum_names(data_list=[]):
    new_list = []
    if data_list:
        for data in data_list:
            d_list = {}
            for key, value in data.items():
                d_list[key.replace(' ', '_').lower()] = value
            new_list.append(d_list)
    return new_list


def load_data():
    try:
        with open('minerals.json', 'r') as file:
            data = json.load(file)
            minerals = parse_colum_names(data)
            for mineral in minerals:
                Mineral(**mineral).save()
        print("\n> Fixtures loaded successfully!\n")
    except FileNotFoundError:
        print('Error: Fixtures file does not exits!')
