from pydantic import BaseModel

class ScreenshotRequest(BaseModel):
    url: str
    width: int = 1280 #default als res niet meegegeven is
    height: int = 720
