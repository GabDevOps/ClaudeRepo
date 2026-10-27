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

## About idealista
idealista does not allow scraping its website. It offers an official API
(https://developers.idealista.com) that requires an API key.
Until we have a key, the backend uses a **mock provider** with sample data.
