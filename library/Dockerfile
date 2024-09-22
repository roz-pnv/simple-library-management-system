FROM python:3

WORKDIR /library-management-system

COPY requirements.txt /library-management-system/
RUN pip install -r requirements.txt

COPY . /online-reservation-system/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
