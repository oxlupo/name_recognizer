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
    surname = list(map(lambda x: x.lower(), surname))

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

with open("general_list.txt", 'r') as file:
    general_list = file.read()
    general_list = general_list.split(f"\n")


def name_finder(email_list):
    for email in email_list:
        part = email.split("@")[0]
        clean_name = re.sub(pattern=r"([0-9])",
                            string=part,
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
        last_name = split_name[1]
        first_name = split_name[0]
        if len(last_name) in range(3, 150):
            if len(first_name) in range(3, 150):
                if not last_name in general_list:
                    print(colored(f"the {last_name} was found in {email}", "green"))
                    print(colored(f"the {first_name} was found in {email}", "yellow"))
            elif not len(first_name) in range(3, 150):
                if not last_name in general_list:
                    print(colored(f"the {last_name} was found in {email}", "red"))
        else:
            continue


