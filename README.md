# Croston

## Development

> Make sure to have installed [Python 3.4](https://www.python.org/downloads/).

Clone this repository:

```sh
git clone https://github.com/mf222/croston.git
cd croston
```

Create [virtualenv](https://virtualenv.pypa.io/en/stable/):

```sh
# Install virtualenv
pip install -U virtualenv

# Create virtualenv (this directory is ignored by gitignore)
virtualenv --python=python3.4 virtualenv

# Activate
source ./virtualenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Desactive when development is finished
desactive
```

Create database:

```sh
python manage.py migrate
```

Run server at [`http://localhost:8000`](http://localhost:8000/):

```sh
python manage.py runserver
```
