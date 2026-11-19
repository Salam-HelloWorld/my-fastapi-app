# Simple Backend Example

A minimal FastAPI backend with **no database** — data is kept in memory and resets when the server restarts.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Then open:

- **Swagger UI:** http://127.0.0.1:8000/docs (try every endpoint from the browser)
- **ReDoc:** http://127.0.0.1:8000/redoc
- **OpenAPI schema:** http://127.0.0.1:8000/openapi.json

## Endpoints

| Method | Path          | Description        |
|--------|---------------|--------------------|
| GET    | `/`           | Welcome message    |
| GET    | `/health`     | Health check       |
| GET    | `/items`      | List items         |
| GET    | `/items/{id}` | Get one item       |
| POST   | `/items`      | Create an item     |
| PATCH  | `/items/{id}` | Partially update   |
| DELETE | `/items/{id}` | Delete an item     |

Example:

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Book", "price": 12.5}'
```

## Test

```bash
pytest
```
