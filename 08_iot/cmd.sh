# 1. edit crontab
sudo crontab -e


# 2. in the opened crontab input the following lines
0 */2 * * * sh [local_repository_path]/virus.sh
# then exit the editing environment by Crtl+X and then `Y`


# 3. restart the cron service to activiate the change
sudo service cron restart

# Appendix:
# a. check the log
sudo tail -f /var/log/syslog | grep CRON
# b. commonly used commands
cd
ls
pwd
history

# After addubg this, save the files and exit the text editor
# (If your using Nano press Ctrl + o, then press Enter to sace the file,)
# and exit using Ctrl + X)
