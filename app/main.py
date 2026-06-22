from app.auth import check_API 
from app.cache import get_screenshot, save_screenshot
from app.capture import take_screenshot
from fastapi import FastAPI, Response, Depends
from typing import Annotated

app = FastAPI()

@app.get("/screenshots")
async def screenshot_response(url: str, width: int, height: int, commons: Annotated[dict, Depends(check_API)]):

    key = f"{url}_{width}_{height}"

    key_controle = get_screenshot(key)

    if key_controle is None:
        screen_bytes = await take_screenshot(url, width, height)
        save_screenshot(key, screen_bytes)
        return Response(content=screen_bytes, media_type="image/png")    
    else:
        return Response(content=key_controle, media_type="image/png")    

