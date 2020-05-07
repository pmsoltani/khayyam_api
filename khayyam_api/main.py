from datetime import date
from typing import Iterable

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from khayyam import JalaliDate

from config import CORS_ORIGINS


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

g_year_range = (1971, 2071)
j_year_range = (1351, 1451)


def arg_check(valid_args: tuple, iterable: Iterable) -> None:
    if any(arg not in valid_args for arg in iterable):
        raise HTTPException(status_code=404)


@app.get("/")
async def root(request: Request):
    return RedirectResponse(app.url_path_for("about"))


@app.get("/today")
async def today(request: Request):
    arg_check((), request.query_params.keys())

    j = JalaliDate.today()
    g = j.todate()
    return {
        "g": {"y": g.year, "m": g.month, "d": g.day},
        "j": {"y": j.year, "m": j.month, "d": j.day},
    }


@app.get("/g2j")
async def g2j(y: int, m: int, d: int, request: Request):
    arg_check(("y", "m", "d"), request.query_params.keys())

    if y not in range(*g_year_range):
        raise HTTPException(status_code=404)

    try:
        g = date(year=y, month=m, day=d)
        j = JalaliDate(g)
        return {
            "j": {"y": j.year, "m": j.month, "d": j.day},
        }
    except Exception:
        raise HTTPException(status_code=404)


@app.get("/j2g")
async def j2g(y: int, m: int, d: int, request: Request):
    arg_check(("y", "m", "d"), request.query_params.keys())

    if y not in range(*j_year_range):
        raise HTTPException(status_code=404)

    try:
        j = JalaliDate(year=y, month=m, day=d)
        g = j.todate()
        return {
            "g": {"y": g.year, "m": g.month, "d": g.day},
        }
    except Exception:
        raise HTTPException(status_code=404)


@app.get("/about")
async def about(request: Request):
    arg_check((), request.query_params.keys())
    from khayyam_api.about import about_khayyam_api

    return about_khayyam_api
