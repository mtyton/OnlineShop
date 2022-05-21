FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /website
WORKDIR /website
COPY requirements.txt /website/
RUN pip install -r requirements.txt
COPY . /website/
CMD python3.10 shop/manage.py migrate && python3.10 shop/manage.py runserver 0.0.0.0:8000
