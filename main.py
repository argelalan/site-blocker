import time
from datetime import datetime as dt
from block_sites import block_sites as bs
from unblock_sites import unblock_sites as us

# Stores website domain names for the program to block.
sites_to_block = [
    'www.twitter.com', 'twitter.com',
    'www.facebook.com', 'facebook.com',
    'www.instagram.com', 'instagram.com',
    'www.tiktok.com', 'tiktok.com'
]

localhost = '127.0.0.1'
# For Windows system, create a copy of the host file,
# located here: C:\Windows\System32\drivers\etc
# Add the path for the host file copy.
hosts_path = '/etc/hosts'


def site_blocker(start_hour, end_hour):
    """
    Block sites for a specified time.
    After the specified time, unblock the sites.
    """
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < \
                dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                              end_hour):
            bs(hosts_path, sites_to_block, localhost)
        else:
            us(hosts_path, sites_to_block)
        time.sleep(3)


if __name__ == '__main__':
    site_blocker(11, 18)  # Specify a time period in military time
