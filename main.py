from fastapi import FastAPI
from pydantic import BaseModel

from dbMilvus import DbMilvus
from service import SibintekService


class QueryBody_sib(BaseModel):
    text: str


app = FastAPI()
db = DbMilvus("localhost", "19530")
sib = SibintekService(db)


@app.post("/query_sib")
async def query_sib(queryBody: QueryBody_sib):
    return {"answer": sib.ask(queryBody.text)}
