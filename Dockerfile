FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate
RUN python manage.py 

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
