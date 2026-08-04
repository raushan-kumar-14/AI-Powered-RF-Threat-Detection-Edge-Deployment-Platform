from pathlib import Path

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

from backend.predictor import predict_image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RF Threat Detection API",
    version="1.0"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "RF Threat Detection API Running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    save_path = UPLOAD_DIR / file.filename

    with open(save_path, "wb") as f:
        f.write(await file.read())

    result = predict_image(save_path)

    return JSONResponse(result)