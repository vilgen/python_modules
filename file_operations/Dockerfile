### SDIST Image Build
#FROM python:3.11-slim
#WORKDIR /app
#COPY . .
#RUN pip install --no-cache-dir -r requirements.txt
#CMD ["python", "file_main.py"]

### WHEEL Image Build
FROM python:3.11-slim
WORKDIR /app
COPY dist/file_operations-1.0.0-py3-none-any.whl .
RUN pip install --no-cache-dir file_operations-1.0.0-py3-none-any.whl
EXPOSE 8000
CMD ["my_project"]