import pandas as pd
from dbMilvus import DbMilvus
from support_fun import make_emb
from tqdm import tqdm

db = DbMilvus("localhost", "19530")

df = pd.read_excel("dataset.xlsx")
data = []
for row in tqdm(df.values):
    data.append(
        {"id": int(row[0]), "type": row[2], "ask_vector": make_emb("passage: " + row[1]), "ask_solve": str(row[3])})

res = db.insert(
    collection_name="sibintek",
    data=data)
