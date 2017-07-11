from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes

class DashboardPlugin(RelationBase):

    @hook('{requires:dashboard-plugin}-relation-joined')
    def joined(self):
        self.set_state('{relation_name}.available')

    @hook('{requires:dashboard-plugin}-relation-{departed,broken}')
    def broken(self):
        self.remove_state({relation_name}.available)
