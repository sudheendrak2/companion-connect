# Companion Connect

Angular front end + FastAPI back end, with AI features (helper chatbot and an
issue-fixing bot). Demo project: use fake data only.

## Folder structure

```
companion-connect/
├── .github/
│   └── workflows/
│       └── ci.yml            # lint, test, build on every PR and push to main
├── frontend/                 # Angular app (ng new)
├── backend/                  # FastAPI service
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py           # API entry point (/health for now)
│   ├── tests/
│   │   └── test_health.py
│   ├── pytest.ini
│   ├── requirements.txt      # runtime dependencies
│   └── requirements-dev.txt  # test and lint tools
├── bot/                      # issue-fixing bot (later phase)
├── infra/                    # AWS deployment config (later phase)
├── docs/                     # architecture notes, eval results
├── .gitignore
└── README.md
```

## One-time setup

```bash
# 1. Git identity (once per machine)
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"

# 2. SSH key for GitHub (once per machine), then add the .pub key in GitHub > Settings > SSH keys
ssh-keygen -t ed25519 -C "you@example.com"

# 3. Create the repo on GitHub (empty), then:
cd companion-connect
git init -b main
git add .
git commit -m "chore: initial project scaffold"
git remote add origin git@github.com:<your-username>/companion-connect.git
git push -u origin main

# 4. Create the Angular app inside frontend/
ng new frontend --directory frontend --skip-git
```

## Run locally

```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload        # http://127.0.0.1:8000/docs
pytest -q
ruff check .

# Frontend
cd frontend
npm ci
npm start
```

## After the first push: protect main (GitHub > Settings > Branches)

- Require a pull request before merging
- Require status checks to pass: "Frontend (Angular)" and "Backend (FastAPI)"
- Block force pushes

Work on feature branches (for example `feat/profiles`) and merge through PRs.

## Next step

Add a deploy workflow (separate file) that runs only after merge to main and uses
GitHub OIDC to assume an AWS role, so no long-lived AWS keys are stored in GitHub.
