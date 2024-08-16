FROM python:3.12.5-alpine3.20 AS builder

RUN apk add swig linux-headers alpine-sdk && wget http://abyz.me.uk/lg/lg.zip && unzip lg.zip && cd lg && make || true && make install || true

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

RUN pip uninstall -y setuptools pip
RUN rm -rf /usr/local/lib/python3.12/site-packages/__pycache__ /usr/local/lib/python3.12/site-packages/_distutils_hack/


FROM python:3.12.5-alpine3.20

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/lib/liblgpio* /usr/local/lib/

WORKDIR /app
COPY src ./

CMD ["python", "/app/main.py"]
