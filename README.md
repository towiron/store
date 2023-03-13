# The Store

The project for study Django.

#### Stack:

* [Python](https://www.python.org/downloads/)
* [PosgreSQL](https://www.postgresql.org/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:

    ```bash
    python3 -m venv ../venv
    source ../venv/bin/activate
    ```
2. Install packages:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
3. Run project dependencies, migrations, fill the database with the fixture data etc.:

    ```bash
    ./manage.py migrate
    ./manage.py loaddata products/fixtures/categories.json
    ./manage.py loaddata products/fixtures/goods.json
    ./manage.py runserver 
    ```


