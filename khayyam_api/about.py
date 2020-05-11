from khayyam import JalaliDate

import khayyam_api._info as info
from khayyam_api.main import app

start = JalaliDate(1399, 2, 18)
today = JalaliDate.today()

live_since = (
    start.isoformat()
    + f" ({start.todate().isoformat()}): "
    + f"{(today - start).days} days ago!"
)


about_khayyam_api = {
    "name": info.__project_name__,
    "version": info.__version__,
    "description": info.__description__,
    "repo": info.__repo__,
    "live_since": live_since,
    "author": {
        "name": info.__author__,
        "contact": {"email": info.__email__, "linkedin": info.__linkedin__},
    },
    "how_to_use": app.docs_url,
    "routes": tuple(app.openapi()["paths"]),
    "license": info.__license__,
    "notice": (
        "This API is hosted on a free server.",
        "It does not require authentication.",
        "Please do not send too many requests.",
    ),
}
