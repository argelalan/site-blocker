def block_sites(default_host, blocked_sites, redirect):
    """
    Redirect specified domain names to the localhost address in the
    system's host file.
    """
    print('Work time...')
    with open(default_host, 'r+') as host_file:
        hosts = host_file.read()
        for site in blocked_sites:
            if site not in hosts:
                host_file.write(f'{redirect} {site} \n')
