# AI Image Generator Studio

Full stack AI project using:

- FastAPI
- React + Vite
- Stable Diffusion
- SQLite
- Docker

Features:

- Text to Image
- Negative prompt
- CFG / Steps control
- History
- Download
- Database
- Docker support

---

## Run without docker

Backend:

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend:

cd frontend
npm install
npm run dev

---

## Run with docker

docker-compose up --build

Frontend:
http://localhost:5173

Backend:
http://localhost:8000/docs

---

## Project Structure

backend/
frontend/
docker-compose.yml
.env
images/