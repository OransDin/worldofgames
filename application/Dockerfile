FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir flask
ENV FLASK_APP=main_score:app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]