from fastapi import FastAPI
import uvicorn

from receptionata import receptionata_router


app = FastAPI()
app.include_router(receptionata_router, prefix="/receptionata")


def main():
    uvicorn.run(
        app=app,
        loop="uvloop",
        port=8000,
        host="0.0.0.0",
    )


if __name__ == "__main__":
    main()
