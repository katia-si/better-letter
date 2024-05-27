FROM

COPY requirements.txt /requirements.txt
COPY

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .

CMD uvicorn mlops.fast:app --host 0.0.0.0 --port $PORT
