import pandas as pd


pd.set_option('display.max_colwidth', None)

df = pd.read_csv(
    "valid.tsv",
    sep="\t",
    header=None
)

for i in range(10):
    print("Label:", df.iloc[i,1])
    print("Statement:", df.iloc[i,2])
    print("-" * 50)