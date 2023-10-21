FROM python:3

WORKDIR /app
COPY . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "LAB1/manage.py", "runserver"]