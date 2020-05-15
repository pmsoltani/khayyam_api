from khayyam import JalaliDate

import khayyam_api._info as info
from khayyam_api.main import app

launch_date_j = JalaliDate(1399, 2, 18)
launch_date_g = launch_date_j.todate()

about_khayyam_api = {
    "name": info.__project_name__,
    "version": info.__version__,
    "description": info.__description__,
    "repo": info.__repo__,
    "live_since": f"{launch_date_j.isoformat()} ({launch_date_g.isoformat()})",
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
