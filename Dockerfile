FROM python:alpine
WORKDIR /app
COPY scores.txt /app/
COPY main_score.py /app/
COPY utils.py /app/
RUN pip install --no-cache-dir flask
ENV FLASK_APP=main_score:app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]