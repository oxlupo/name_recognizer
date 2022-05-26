import names_dataset

name = names_dataset.NameDataset()
first_name = name.first_names
last_name = name.last_names

last_name_list = []
first_name_list = []

for key, value in first_name.items():
    first_name_list.append([key, 0])


for key, value in last_name.items():
    first_name_list.append([key, 1])

train_list = first_name_list + last_name_list

