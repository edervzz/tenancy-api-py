""" create tenant """
from flask import Blueprint
from webapi import PREFIX_VER_1

update_tenant = Blueprint("update_tenant", __name__)


@update_tenant.put(f"{PREFIX_VER_1}/tenants")
def __handler():
    """ index """
    return "tenant updated"
