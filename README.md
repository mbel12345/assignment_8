# Project Setup

## Set up Repo
In Github:
Create new repo called assignment_8 and make sure it is public

In WSL/VS Code Terminal:
```bash
mkdir assignment_8
cd assignment_8/
git init
git branch -m main
git remote add origin git@github.com:mbel12345/assignment_8.git
vim README.md
git add . -v
git commit -m "Initial commit"
git push -u origin main
```

## Set up virtual environment
In WSL/VS Code Terminal:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run app as stand-alone Python app
In WSL/VS Code Terminal:
```bash
python3 main.py
```

In Browser, go to:
http://localhost:8000/

## Run test cases locally
In WSL/VS Code Terminal:
```bash
pytest
```

## Build image and start container
In WSL/VS Code Terminal:
```bash
docker rm -f /fastapi_calculator && docker compose up --build
```

In Browser, go to:
http://localhost:8000/


## Configure Github Actions
Github Actions will run on any pushes or pull requests. Only pull requests will result in the deployment step.
Pre-requisite: In Dockerhub, create an Access Token, then add it to Environment var "DOCKERHUB_PASSWORD" in GitHub. Add DOCKERHUB_USERNAME also.
