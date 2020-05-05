from datetime import date
from typing import Iterable

from fastapi import FastAPI, HTTPException, Request
from khayyam import JalaliDate

from khayyam_api._version import __version__

app = FastAPI()

g_year_range = (1971, 2071)
j_year_range = (1351, 1451)


def arg_check(valid_args: tuple, iterable: Iterable) -> None:
    if any(arg not in valid_args for arg in iterable):
        raise HTTPException(status_code=404)


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
    return {
        "name": "khayyam_api",
        "version": __version__,
        "description": "A dead simple Jalali API",
        "author": "Pooria Soltani",
        "contact": {"linkedin": "https://www.linkedin.com/in/pmsoltani"},
        "how_to_use": "/docs",
        "license": "MIT",
        "notice": (
            "This API is hosted on a free server. "
            + "It does not require authentication. "
            + "Please do not send too many requests."
        ),
    }
