import os
from datetime import datetime as dt

from config.server_environment import ANSIBLE_PATH


def create_path_if_not_exists(domain):
    ansible_path = ANSIBLE_PATH + 'ansible/'
    hosts_path = ansible_path + 'hosts/'
    domain_path = hosts_path + domain + '/'

    if not os.path.exists(ansible_path):
        os.mkdir(ansible_path)
    if not os.path.exists(hosts_path):
        os.mkdir(hosts_path)
    if not os.path.exists(domain_path):
        os.mkdir(domain_path)

    return domain_path


def hosts_to_file(hosts, domain, filename=None):
    if not hosts or not domain:
        return False

    if not filename:
        filename = dt.isoformat(dt.utcnow())

    path = create_path_if_not_exists(domain)

    file_path = path + filename
    os.remove(file_path)
    file = open(filename, 'w')

    if type(hosts) is list:
        for host in hosts:
            file.write('[' + host['name'] + ']')
            for ip in host['ips']:
                file.write(ip)

            file.write('\n')

    file.close()

    return file_path


