"""_summary_
    """
from tenant_options import TenantOption


class Tenant:
    """_summary_
    """

    def __init__(self):
        self.id: int = 0
        self.identifier: str = ""
        self.name: str = ""
        self.is_active: bool = False
        self.tenant_options: list[TenantOption] = []
