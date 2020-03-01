from ansible import context
from ansible.cli import CLI
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

from src.classes.ansible.host import Host
from src.classes.ansible.playbook import Playbook
from src.classes.mongo_engine import MongoEngine

from src.utils.hosts_to_file import hosts_to_file

from config.server_environment import ANSIBLE_PATH


class AnsibleEngine:
    def __init__(self):
        self.path = ANSIBLE_PATH

    def run_playbook(self, host, pb, passwords={}):
        if not host or not pb:
            return False

        # Check if hosts exists
        hosts = []
        if type(host) is list:
            for h in host:
                current = Host().find(criteria={'name': h})
                if current.data:
                    hosts.append({
                        'name': current.data['name'],
                        'ips': current.data['ips']
                    })
        else:
            current = Host().find(criteria={'name': host})
            if current.data:
                hosts.append({
                    'name': current.data['name'],
                    'ips': current.data['ips']
                })

        if len(hosts) == 0:
            return False

        hosts_file = hosts_to_file(
            hosts=hosts,
            domain=MongoEngine().get_collection_name()  # aka the domain
        )

        # Check if playbook exists
        playbook = None
        current = Playbook().find(criteria={'name': pb})
        if current.data:
            playbook = current.data['playbook']

        if not playbook:
            return False

        # Ansible stuff
        loader = DataLoader()
        context.CLIARGS = dict(
            tags={},
            listtags=False,
            listtasks=False,
            listhosts=False,
            syntax=False,
            connection='ssh',
            module_path=None,
            forks=10,
            private_key_file=None,
            ssh_common_args=None,
            ssh_extra_args=None,
            sftp_extra_args=None,
            scp_extra_args=None,
            become_method='sudo',
            become_user='root',
            verbosity=True,
            check=False,
            start_at_task=None
        )

        inventory = InventoryManager(
            loader=loader,
            sources=(hosts_file,)
        )

        variable_manager = VariableManager(
            loader=loader,
            inventory=inventory,
            version_info=CLI.version_info(gitinfo=False)
        )

        pbex = PlaybookExecutor(
            playbooks=[playbook],
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            passwords=passwords
        )

        results = pbex.run()
        print("results", results)
