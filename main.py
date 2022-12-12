from fastapi import FastAPI

from modules.user import user_router

app = FastAPI()

app.include_router(user_router.router)


@app.get("/")
async def root():
    return "Hello You!"
