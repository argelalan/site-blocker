def unblock_sites(default_host, blocked_sites):
    """
    Remove domain names from host file
    """
    with open(default_host, 'r+') as host_file:
        hosts = host_file.readlines()
        host_file.seek(0)
        for host in hosts:
            if not any(site in host for site in blocked_sites):
                host_file.write(host)
        host_file.truncate()
    print('Fun time...')
