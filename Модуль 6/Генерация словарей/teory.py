data = [
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'},
    {'id': 12, 'user': 'Anton'},
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'},
]

unique_data_dict = {i_dict['id']: i_dict for i_dict in data}
print(unique_data_dict.values())