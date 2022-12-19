from fastapi import FastAPI
from core import settings
from core.router import set_routers
import uvicorn


app = FastAPI(title = "College FastApi")

@app.on_event("startup")
def startup():
    set_routers(app)

@app.on_event("shutdown")
def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT, host=settings.HOST, reload=True)