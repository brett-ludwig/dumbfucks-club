FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN apt-get install
RUN pip install fastapi[standard]
RUN pip install starlette
RUN pip install requests
RUN pip install uvicorn


EXPOSE 8000

CMD ["uvicorn", "app:app", "--reload", "--port", "8000", "--host", "0.0.0.0", "--proxy-headers", "--forwarded-allow-ips", "10.0.1.2"]
# CMD ["fastapi", "run", "app.py", "--port", "8000"]
