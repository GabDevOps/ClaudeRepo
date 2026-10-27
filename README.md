# ClaudeRepo – House Hunting App (learning project)

A small learning project to practise Git, GitHub and branches.

## What the app does
1. **Frontend** – a web page where you enter what you are looking for
   (city, max price, minimum rooms...).
2. **Backend** – receives those search parameters, asks a property
   provider (idealista) for matching houses, and returns the results.

Later the backend will also evaluate finances, mortgage costs, etc.

## Project layout
```
ClaudeRepo/
├── README.md      ← this file
├── backend/       ← Python server (added on branch feature/backend)
└── frontend/      ← web page (added on branch feature/frontend)
```

## How to run it
1. **Backend** (in one terminal):
   ```
   cd backend
   pip install -r requirements.txt
   uvicorn app:app --reload
   ```
2. **Frontend** (in a second terminal):
   ```
   cd frontend
   python -m http.server 5500
   ```
3. Open http://127.0.0.1:5500 and search for e.g. *Lisboa*.

## About idealista
idealista does not allow scraping its website. It offers an official API
(https://developers.idealista.com) that requires an API key.
Until we have a key, the backend uses a **mock provider** with sample data.
