import uvicorn

from fastapi import FastAPI

from . import models
from .database import engine
from .routers import authentication, blog, user



app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)