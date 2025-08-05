from fastapi import FastAPI, Response
app = FastAPI()

@app.get("/hi/{name}/{value}")
def greet(name:str, value:str, response:Response):
    response.headers[name] = value
    return "Hello..."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("123:app", reload=True)