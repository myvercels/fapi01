# 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

# git remote set-url origin https://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@github.com/myvercels/fapi01/ 

from fastapi import FastAPI, Response
app = FastAPI()

@app.get("/hi/{name}/{value}")
def greet(name:str, value:str, response:Response):
    response.headers[name] = value
    return "Hello..."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("123:app", reload=True)