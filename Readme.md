# PostgreSQL Connection Example

This is a simple example of how to connect to a PostgreSQL database using environment variables and the `psycopg2` module in Python.

## Requirements

To run this code, you will need to have the following Python packages installed:

- psycopg2==2.9.9
- python-dotenv==1.0.1

You can install these packages by running:

```[python]
pip install -r requirements.txt
```

## Setting

Make sure to create a `.env` file in the root directory of your project and define the following environment variables:

```
DB_NAME=mydb
DB_USER=username
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

These environment variables will be used to establish the connection with the PostgreSQL database.

## Uso

Simply run the `main.py` script:

```
python main.py
```

If the connection is successful, you will see the message "Successful connection." Otherwise, an error message will be displayed with details about the connection problem.

## Thanks

This example uses the `psycopg2` module to interact with PostgreSQL and `python-dotenv` to load environment variables from a `.env` file.

## Grades

- Remember not to upload the `.env` file to public repositories, as it contains sensitive information such as passwords.
- If you need more information on how to use this example or configure your environment, please consult the official documentation for each module.
