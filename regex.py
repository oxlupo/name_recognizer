import re
import pandas as pd
from termcolor import colored

def dataset_loader():
    """load dataset for finding firstname and lastname """
    with open("names-databases/surnames/all.txt", 'r', encoding='utf-8') as file:
        dataset = file.read()
        surname = dataset.split("\n")
    with open("names-databases/first names/all.txt", 'r', encoding="utf-8") as file:
        dataset = file.read()
        first_name = dataset.split("\n")
    first_name = list(map(lambda x: x.lower(), first_name))
    surname= list(map(lambda x: x.lower(), surname))

    return list(set(first_name)), list(set(surname))


def split_by_dot(list_):
    """split and merge the emails that have 2 condition "." or "-" """
    final_list = []
    for element in list_:
        if len(str(element).split(".")) >= 2 or len(str(element).split("-")) >= 2:
            final_list.append(element)
    return list(set(final_list))


emails_df = pd.read_csv("emails_100k.csv", date_parser=True)
emails = list(emails_df["email"])
part_1 = list(map(lambda x: x.split("@")[0], emails))
clean_name = list(map(lambda x: re.sub(pattern=r"([0-9])",
                                       string=x,
                                       repl=""), part_1))

first_name, surname = dataset_loader()
for email in emails:
    part_1 = email.split("@")[0]
    clean_name = re.sub(pattern=r"([0-9])",
                        string=part_1,
                        repl="")
    search = re.search(string=clean_name, pattern=f"\b[a-z]\b")
    if clean_name.startswith("."):
        continue
    if "." in clean_name:
        split_name = clean_name.split(".")
    elif "-" in clean_name:
        split_name = clean_name.split("-")
    elif not search == None:
        continue
    else:
        continue
    for word in split_name:
        if word in surname:
            print(colored(f"the {word} surname was founded in >>>>>>>>>>>> {email}"))
