from fastapi import FastAPI
from fa_college_app.routers import group, student


def set_routers(app :FastAPI):
    app.include_router(group.router, prefix="", tags=["groups"])