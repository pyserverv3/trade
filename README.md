# Lutan Trading Academy — Flask starter

## Run in VS Code / PowerShell

```powershell
cd lutan_flask
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Main routes

- `/` — Lutan landing page
- `/learn` — beginner trading blueprint
- `/signals` — signal examples
- `/events` — events
- `/events/<id>` — event details
- `/admin/events` — event management
- `/admin/events/new` — create event
- `/admin/events/<id>/edit` — edit event

## Important

This is a clean base. To preserve your existing Flask database, authentication, routes, and templates exactly, replace/merge these files with your current project rather than deleting the current project.
