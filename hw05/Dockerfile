# Dockerfile
FROM agrigorev/zoomcamp-model:2025
WORKDIR /code

COPY pipeline_v1.bin /code/pipeline_v1.bin

COPY app.py /code/app.py
COPY requirements.txt /code/requirements.txt

RUN python -m pip install --no-cache-dir -r /code/requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
