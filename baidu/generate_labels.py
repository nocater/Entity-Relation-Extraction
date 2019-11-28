import pandas as pd
"""
Generate labels.file
"""

dataset = 'baidu_95'
df = pd.read_csv(f'./{dataset}.csv', header=None, names=["labels", "item"], dtype=str)

all_labels = set()
predicate_list = df.labels.apply(lambda x: x.split())
[all_labels.update(x) for x in predicate_list]

with open('./category.labels', 'w') as f:
    f.write(repr(list(all_labels)))