FROM python:3.4.3

# Create app directory
RUN mkdir /code
WORKDIR /code

# Install app dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Bundle app source
COPY . /code/
# RUN mkdir -p ./Arquitran/static
# RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
