from fastapi import FastAPI, UploadFile

app = FastAPI(
    title="CNAB Processing API",
    description="API for CNAB file processing and bank remittance validation.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "CNAB Processing API is running"}

@app.post("/upload-cnab")
async def upload_cnab(file: UploadFile):
    content = await file.read()

    return {
        "filename": file.filename,
        "size": len(content),
        "message": "CNAB file received successfully"
    }