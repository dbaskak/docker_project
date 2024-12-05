FROM python:3.10

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001git push -u origin main

CMD ["python", "app.py"]