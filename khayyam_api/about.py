from khayyam import JalaliDate

from khayyam_api._version import __version__
from khayyam_api.main import app

start = JalaliDate(1399, 2, 18)
today = JalaliDate.today()

live_since = (
    start.isoformat()
    + f" ({start.todate().isoformat()}): "
    + f"{(today - start).days} days ago!"
)


about_khayyam_api = {
    "name": "khayyam_api",
    "version": __version__,
    "description": "A dead simple Jalali API",
    "repo": "https://github.com/pmsoltani/khayyam_api",
    "live_since": live_since,
    "author": {
        "name": "Pooria Soltani",
        "contact": {"linkedin": "https://www.linkedin.com/in/pmsoltani"},
    },
    "how_to_use": app.docs_url,
    "routes": tuple(app.openapi()["paths"]),
    "license": "MIT",
    "notice": (
        "This API is hosted on a free server.",
        "It does not require authentication.",
        "Please do not send too many requests.",
    ),
}
