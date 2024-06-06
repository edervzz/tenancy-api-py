""" starting point """
import os
import mysql.connector

from flask import Flask

from webapi import Services
from webapi.endpoints.read_tenant import read_tenant
from webapi.endpoints.create_tenant import create_tenant
from webapi.endpoints.update_tenant import update_tenant

from toolkit.logger import LoggerBasic

# nueva aplicación Flask
app = Flask(__name__)


try:
    db_connection = mysql.connector.connect(
        host=os.environ["DB_SERVER"],
        user=os.environ["DB_USR"],
        password=os.environ["DB_PWD"])

    print(f"Database connection open: {db_connection.is_connected()}")

except mysql.connector.errors.DatabaseError as ex:
    print(ex)
    db_connection = None

# registro de servicios DI
services = Services(
    mysql=db_connection,
    logger=LoggerBasic()
)


# registro de endpoints
app.register_blueprint(create_tenant)
app.register_blueprint(read_tenant)
app.register_blueprint(update_tenant)


@app.get("/healt-check")
def health_check():
    """healt check endpoint"""
    return {"healt_check": "ok"}
