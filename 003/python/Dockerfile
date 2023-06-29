FROM python

RUN mkdir /python
WORKDIR /python/

COPY main.py main.py
COPY requirements.txt requirements.txt
COPY data data

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]