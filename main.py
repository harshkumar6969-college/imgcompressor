import os
import shutil
from pathlib import Path
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles as stat
from fastapi.responses import FileResponse
from fastapi import UploadFile, File
from PIL import Image

app = FastAPI()
app.mount("/static/", stat(directory="Templates"), name="static")

filepath = "my_folder"
os.makedirs(filepath, exist_ok=True)
@app.get("/")
def home():
    return FileResponse("Templates/index.html")

@app.post("/upload")
async def handle_upload(file: UploadFile = File(...)):
    
    finalpath = os.path.join(filepath, file.filename)
    print(finalpath)
    print(file.file)
    with open(finalpath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer) 
        print("Done")
        
    def compressor():
        with Image.open(finalpath) as img:
            compath = os.path.join("Templates", "compressed.jpg")
            img.save(compath, optimize=True, quality=70)
            print(f"Image sucessfully saved to {compath}")
    compressor()

class NoCacheStaticFiles(stat):
    def file_response(self, *args, **kwargs):
        response = super().file_response(*args, **kwargs)
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response