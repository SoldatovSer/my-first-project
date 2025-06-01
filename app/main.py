from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is custom message!"}
