FROM python:3.11.2-bullseye
WORKDIR /apps
# RUN pip install fastapi[all] uvicorn pydantic python-multipart "pydantic[email]"
RUN pip install --upgrade pip
RUN pip install requests
COPY examples ./examples
# CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]