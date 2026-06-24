# Screenshot API

API om screenshots te nemen van websites. Gebouwd met FastAPI, Playwright en Redis.

## Wat heb je nodig

- Docker & Docker Compose
- Een `.env` bestand (zie hieronder)

## Setup

Maak een `.env` bestand aan in de root van het project:

```
API_KEYS=jouw-sleutel
REDIS_URL=redis://localhost:6379
CACHE_TTL=300
```

## Opstarten

```bash
docker compose up --build
```

De API draait dan op `http://localhost:8000`.

## Screenshot nemen

`GET /screenshots` met deze query parameters:

- `url` — de URL van de website
- `width` — breedte van de viewport (in pixels)
- `height` — hoogte van de viewport (in pixels)

Voeg ook je API key toe als header:

```
X-API-Key: jouw-sleutel
```

Voorbeeld:

```bash
curl "http://localhost:8000/screenshots?url=https://thomasmore.be/en&width=1280&height=720" \
  -H "X-API-Key: jouw-sleutel" \
  --output screenshot.png
```

## API testen via de browser

```
http://localhost:8000/docs
```

## Tests runnen

```bash
pytest
```
