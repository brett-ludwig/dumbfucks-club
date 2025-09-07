FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN apt-get install
RUN pip install -r requirements.txt


EXPOSE 8000

# uvicorn app:app --reload --port 8000 --host localhost
CMD ["uvicorn", "app.main:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]
# CMD ["fastapi", "run", "app.py", "--port", "8000"]
