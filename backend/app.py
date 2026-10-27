"""The backend web server.

Run it with:   uvicorn app:app --reload   (from inside the backend/ folder)
Then open:     http://127.0.0.1:8000/search?city=Lisboa&max_price=300000&min_rooms=2
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from providers import MockProvider

app = FastAPI(title="House Hunting API")

# Allow the frontend (a different web page) to call this API.
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET"])

provider = MockProvider()  # swap for IdealistaProvider() later


@app.get("/search")
def search(city: str, max_price: int = 10_000_000, min_rooms: int = 0):
    results = provider.search(city, max_price, min_rooms)
    return {"count": len(results), "results": results}
