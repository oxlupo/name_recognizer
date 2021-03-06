from termcolor import colored
from tqdm import tqdm
import re
import pandas as pd


def dataset_loader():
    """load dataset for finding firstname and lastname """
    with open("names-databases/surnames/us.txt", 'r', encoding='utf-8') as file:
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
    general_list = list(set(general_list.split(f"\n")))


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


def surname_finder(email_dict, surname):
    """ find surname that one part """
    final_list = []
    split_email = email_dict["email"].split("@")[0]

    for word in surname:
        if len(word) in range(4, 150):
            if not word in general_list:
                if word == split_email:
                    email_dict["surname"] = word
                    email_dict["status"] = True

                    return email_dict

    return final_list


first_name, last_name = dataset_loader()
last_name.pop(0)
limit_email = emails[:5000]
def find_general(false_list):
    """ this function return email that have general :return """
    general_emails = []
    for email in false_list:
        email_split = email.split("@")[0]
        email_split = re.sub(pattern="[0-9]", string=email_split, repl="")

        if email_split in general_list:
            general_emails.append(email)
        parts = ""
        if "." in email_split:
            parts = email_split.split(".")
        elif "-" in email_split:
            parts = email_split.split("-")
        elif "_" in email_split:
            parts = email_split.split("_")
        else:
            continue
        for part in parts:
            if part in general_list:
                general_emails.append(email)

    with open("general_emails.txt", "w") as file:
        for general in general_emails:
            file.write(general + "\n")
    return general_emails

def email_validation

def total_finder(emails):
    """find all firstname if exist and surname if exists in a json file"""
    false_email = []
    count = 0
    true_emails = []
    with_out_general = []
    general_emails = find_general(false_list=limit_email)
    for element in emails:
        if not element in general_emails:
            with_out_general.append(element)
    for email in tqdm(with_out_general, total=len(with_out_general)):

        email_dict = name_finder(email)
        if email_dict["status"] == False:
            surname = surname_finder(email_dict=email_dict, surname=last_name)
            if not surname == []:
                print(colored(surname, "yellow"))
                count += 1
                true_emails.append(email)
            else:
                false_email.append(email_dict["email"])
        else:
            print(colored(name_finder(email), "green"))
            count += 1
            true_emails.append(email)

    true_file = open("true_email.txt", "w")
    for element in true_emails:
        true_file.write(element + "\n")

    general_emails = find_general(false_list=false_email)
    total_pattern = general_emails + true_emails
    with open("with_out_pattern.txt", "w") as pattern:

        for email in limit_email:
            if not email in total_pattern:
                pattern.write(email + "\n")

# total_finder()
em = "20220114180306.06e71602b7@dpdk-ubuntu.dpdklab.iol.unh.edu"
s = re.sub(pattern="[0-9]", string=em, repl="")
