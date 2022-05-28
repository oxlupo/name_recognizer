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


def name_finder(email):
    """the main function that found surname and firstname and save it in a dict"""

    email_dict = {"email": "",
                      "status": "",
                      "firstname": "",
                      "surname": ""
                      }

    part = email.split("@")[0]

    clean_name = re.sub(pattern=r"([0-9])",
                        string=part,
                        repl="")
    email_dict["email"] = email
    if clean_name.startswith("."):
        email_dict["status"] = False
        return email_dict

    if "." in clean_name:
        split_name = clean_name.split(".")
    elif "-" in clean_name:
        split_name = clean_name.split("-")
    else:
        email_dict["status"] = False
        return email_dict

    last_name = split_name[1]
    first_name = split_name[0]
    if len(last_name) in range(3, 150):
        if len(first_name) in range(3, 150):
            if not last_name in general_list:

                email_dict["status"] = True
                email_dict["firstname"] = first_name
                email_dict["surname"] = last_name

        elif not len(first_name) in range(3, 150):
            if not last_name in general_list:
                email_dict["status"] = True
                email_dict["surname"] = last_name

    else:
        email_dict["status"] = False

    return email_dict

for email in emails:
    email_dict = name_finder(email)
    if email_dict["status"] == False:
        print(colored(name_finder(email), "red"))
    else:
        print(colored(name_finder(email), "green"))
