import pytest
from app.capture import take_screenshot

@pytest.mark.asyncio

async def test_screenshot():
    url = "https://thomasmore.be/en"
    width = 1280
    heigth = 720

    result = await take_screenshot(url, width, heigth)

    assert result is not None

    assert isinstance(result, bytes)