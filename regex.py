import re
import pandas as pd
import names_dataset


def dataset_loader():

    name_dataset = names_dataset.NameDataset()
    first_name = name_dataset.first_names
    last_name = name_dataset.last_names

    first_name_list = [x for x in first_name.keys()]
    last_name_list  = [x for x in last_name.keys()]

    return first_name_list, last_name_list


def split_by_dot(list_):
    """split and merge the emails that have 2 condition "." or "-" """
    final_list = []
    for element in list_:
        if len(str(element).split(".")) >= 2 or len(str(element).split("-")) >= 2:
            final_list.append(element)
    return list(set(final_list))


emails_df = pd.read_csv("emails_100k.csv", date_parser=True)
email = list(emails_df["email"])
part_1 = list(map(lambda x: x.split("@")[0], email))
clean_name = list(map(lambda x: re.sub(pattern=r"([0-9])",
                                       string=x,
                                       repl=""), part_1))

name = split_by_dot(clean_name)
