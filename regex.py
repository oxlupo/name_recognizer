import re
import pandas as pd

emails_df = pd.read_csv("emails_100k.csv", date_parser=True)

email = list(emails_df["email"])

name = list(map(lambda x: x.split("@")[0], email))
clean_name = list(map(lambda x: re.sub(pattern=r"([0-9])",
                                       string=x,
                                       repl=""), name))
def split_by_dot(list_):
    final_list = []
    for element in list_:
        if element.split(".") >= 2 or element.split("-") >= 2:
            final_list.append(element)
    return final_list


