FROM python:2.7-slim
COPY process.py /
WORKDIR /
ENTRYPOINT ["python", "-u", "process.py"]
