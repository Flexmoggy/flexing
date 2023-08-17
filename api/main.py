from fastapi import FastAPI
from routers import events
from fastapi.middleware.cors import CORSMiddleware
from routers import accounts, profiles, reviews, events

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])

app = FastAPI()
app.include_router(profiles.router)
app.include_router(events.router)


@app.get("/")
def root():
    return {"message": "We've hit the root path;)"}


app.include_router(accounts.router)
app.include_router(authenticator.router)

origins = [
    "http://localhost:3000",
    os.environ.get("CORS_HOST", None),
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00",
        }
    }
