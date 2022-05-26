import names_dataset
import pandas as pd
import logging
from simpletransformers.classification import ClassificationModel, ClassificationArgs

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)
name = names_dataset.NameDataset()


first_name = name.first_names
last_name = name.last_names

last_name_list = []
first_name_list = []

for key, value in first_name.items():
    first_name_list.append([key, 0])


for key, value in last_name.items():
    first_name_list.append([key, 1])

train_data = first_name_list[:len(first_name_list)//2] + last_name_list[:len(last_name_list)//2]
train_df = pd.DataFrame(train_data)
train_df.columns = ["text", "labels"]

eval_data = first_name_list[len(first_name_list)//2:] + last_name_list[len(last_name_list)//2:]
eval_df = pd.DataFrame(eval_data)
eval_df.columns = ["text", "labels"]

model_args = ClassificationArgs(num_train_epochs=10)
