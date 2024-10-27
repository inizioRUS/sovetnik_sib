import os
from tqdm import tqdm
from dbMilvus import DbMilvus
from support_fun import make_emb, getText

db = DbMilvus("localhost", "19530")
data = []
index = 0
for i in tqdm(os.listdir("docx_doc")):
    data.append(
        {"id": index, "filename": i, "guide_vector": make_emb("passage: " + getText("docx_doc/" + i))})
    index += 1

res = db.insert(
    collection_name="sibintek_guide",
    data=data)
