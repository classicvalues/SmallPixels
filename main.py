from PIL import Image
from fastapi import FastAPI, responses, Header
from pydantic import BaseModel
from uuid import uuid4
from typing import Optional
from deta import Deta

class SetPixel(BaseModel):
    x: int
    y: int
    rgb: str ="00FF00"

class GetPixel(BaseModel):
    x: int
    y: int

deta = Deta("b0yzndy0_ryPgJTVp4Wt31uqNDFuCJomFp9CJdE1N")

db = deta.Base("tokens")


app = FastAPI()
def hextorgb(h):
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

im = Image.open('canvas.png')
img = im.load()

@app.get("/", response_class=responses.HTMLResponse)
async def home():
    return "<h1>Hi, go to /token to get your token.</h1>"

@app.get("/token")
async def token():
    token = uuid4()
    tokens = db.get("tokens")
    tokens.append(str(token))
    db.put(tokens, "tokens")
    return {"token": str(token)}

@app.post("/set_pixel")
async def setpixel(pixel: SetPixel, Authorization: Optional[str] = Header(None)):
    if Authorization is None:
        return {"message": "Please authorize with your Token."}
    if Authorization not in db.get("tokens"):
        return {"message": "Invalid token. Get one at /tokens or make sure that you entered the correct token."}
    if pixel.x > 380:
        return {"message": "Please ensure the X value is under 380."}
    elif pixel.y > 120:
        return {"message": "Please ensure the Y value is under 120."}
    elif pixel.x is None or pixel.y is None:
        return {"message": "Please set X and Y values."}
    
    img[pixel.x, pixel.y] = hextorgb(pixel.rgb)

    im.save('canvas.png')

    return {"message": f"Set pixel ({pixel.x}, {pixel.y}) to {pixel.rgb}."}

@app.get("/get_pixel")
async def get_pixel(pixel: GetPixel, Authorization: Optional[str] = Header(None)):
    if Authorization is None:
        return {"message": "Please authorize with your Token."}
    if Authorization not in db.get("tokens"):
        return {"message": "Invalid token. Get one at /tokens or make sure that you entered the correct token."}
    if pixel.x > 380:
        return {"message": "Please ensure the X value is under 380."}
    elif pixel.y > 120:
        return {"message": "Please ensure the Y value is under 120."}
    elif pixel.x is None or pixel.y is None:
        return {"message": "Please set X and Y values."}
    
    colortuple = im.getpixel((pixel.x, pixel.y))
    colorhex = "%02x%02x%02x" % colortuple
    return {"coordinates": f"({pixel.x}, {pixel.y})", "color": colorhex}

    


