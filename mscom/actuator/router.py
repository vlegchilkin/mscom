from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log

router = APIRouter(prefix="/actuator")


@router.on_event("startup")
async def startup_event():
    log.info("Actuator startup completed")


@router.on_event("shutdown")
async def shutdown_event():
    log.info("Actuator shutdown completed")


@router.get("/")
async def root(request: Request):
    return JSONResponse(content={"owner": "Actuator"})


@router.get("/health")
async def root(request: Request):
    return JSONResponse(content={"owner": "Actuator", "resource": "health"})
