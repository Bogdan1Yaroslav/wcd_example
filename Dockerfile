FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY . .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]