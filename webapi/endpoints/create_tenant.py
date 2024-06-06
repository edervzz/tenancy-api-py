""" create tenant """
from flask import Blueprint
from webapi import PREFIX_VER_1

create_tenant = Blueprint("create_tenant", __name__)


@create_tenant.post(f"{PREFIX_VER_1}/tenants")
def __handler():
    """ index """
    return "tenant created"
