# Overview

This project implements log analysis of a newspaper site for the Udacity Full Stack Developer Nano Degree Program. Data is stored in the newsdata.sql file. This project uses Python psycopg2 (Postgresql + Python) which is most popular Python adapater for connecting to Postgresql database. 

# Dependencies

* VirtualBox or VMWare (https://www.virtualbox.org/wiki/Downloads) or (https://my.vmware.com/web/vmware/downloads)
* Vagrant (https://www.vagrantup.com/downloads.html)
* PostgreSQL database with log data (https://wiki.postgresql.org/wiki/PostgreSQL_For_Development_With_Vagrant)
* Python (https://www.python.org/downloads/)

Above dependencies are provided as project prerequisites.

# Installation
* Download and install Python 
* Download and install vagrant
* Download the vagrant folder from Udacity vagrant installation page
* Naviage to the udacity vagrant folder and start vagrant using "vagrant up" command from the powershell/bash/terminal
* Login into Vagrant using "vagrant ssh" command
* navigate to folder vagrant folder "cd /vagrant"
* Navigate to python and run python using "python news_log.py: command

# Code Design

Project has one python source file `news_log.py`. It has 3 function which answers 3 different questions

 * show_popular_articles (1. What are the most popular three articles of all time?)
 * show_popular_authors (2. Who are the most popular article authors of all time?)
 * show_days_with_errors (3. On which days did more than 1% of requests lead to errors?)

Output is provided in `output.txt`

# Run

```bash
$ python news_log.py
```

# Author

* Samvid Kulkarni



