from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()

#python起動コマンド：uvicorn main:app --host 0.0.0.0 --port 8000 --reload

@app.post("/")
def root():
    return {"hello beatmate_python"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081, log_level="debug")