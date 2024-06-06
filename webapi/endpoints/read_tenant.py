""" create tenant """
from flask import Blueprint
from webapi import PREFIX_VER_1

read_tenant = Blueprint("read_tenant", __name__)


@read_tenant.get(f"{PREFIX_VER_1}/tenants")
def __handler():
    """ index """
    return {"data": "my tenant info"}
