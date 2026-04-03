from fastapi import FastAPI
from app.db.session import DataBase
from app.routes import auth

app = FastAPI(title="TradeAI")

app.include_router(auth.router)

@app.on_event("startup")
async def startup():
    await DataBase.connect()

@app.on_event("shutdown")
async def shutdown():
    await DataBase.disconnect()

@app.get("/")
def root():
    return {"msg" : "API Running 🚀"}



 