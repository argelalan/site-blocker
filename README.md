# Site-Blocker
Finding yourself getting distracted by those pesky social media notifications? This Python script can block access to any website for a given time period.

## How it Works:

### Host file and localhost
All operating systems have a **host** file which connects your computer's hostname to IP addresses. It contains a *localhost* address which allows for connections to be established with your computer. If a website's url were to be redirected to your localhost address, connection to any real site would be prevented. This is precisely how the script will block access to websites.

### _time_ and _datetime_ Modules
The _time_ and _datetime_ modules give Python several time-related functionalities. In our case they are used to temporarily suspend the execuation of the program and to set a period of time for the sites to be blocked, respectively. 

## How to Use:

### Mac/Linux Users
For the program to work, a cron job with root privileges will have to be set up that executes it.
1. Have Python 3 installed.
2. Go to your terminal and type in the following command: `sudo crontab -e`
3. Press 'i' to insert the following command:
`@reboot python3 ~/path_to_file/site_blocker/main.py` (Make sure the file path you use exists in your system)
4. Press 'esc' and enter ':wq' to save your command.
5. Restart your computer and enjoy the productivity boost.

#### Learn more about how to run cron jobs:
[‘crontab’ in Linux with Examples](https://crontab.guru)

### Windows Users
Instead of crontab, task schedueler will be used.
1. Have Python 3 installed.
2. Change the extension of the script from '.py' to '.pyw'.
3. Open 'Task Scheduler'.
4. Click on 'Create Task'. Use whatever name you'd like for the task and make sure the option 'Run with highest privileges' is chosen.
5. Go to the 'Triggers' tab. Click on the drop down for 'Begin the task:' and choose 'At startup'
6. Create a new action by goin to the 'Actions' bar, clicking 'New', and passing the path for the script (Make sure the file path you use exists in your system).
7. Go to the 'Conditions' tab and unselect that 'Power' options
8. Press 'OK' to schedule the script
9. Restart your computer and enjoy the productivity boost.z

## References & Citations:
* [Website Blocker Using Python](https://www.geeksforgeeks.org/website-blocker-using-python/)
* [datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)
* [time — Time access and conversions](https://docs.python.org/3/library/time.html)
