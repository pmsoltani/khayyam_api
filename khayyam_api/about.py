from khayyam_api._version import __version__
from khayyam_api.main import app

about_khayyam_api = {
    "name": "khayyam_api",
    "version": __version__,
    "description": "A dead simple Jalali API",
    "repo": "https://github.com/pmsoltani/khayyam_api",
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
