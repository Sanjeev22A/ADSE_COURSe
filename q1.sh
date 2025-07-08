#!/bin/bash

echo "======================================="
echo "        SYSTEM INFO SCRIPT"
echo "======================================="

echo -e "\n[1] Date and Time:"
date

echo -e "\n[2] Uptime:"
uptime

echo -e "\n[3] Current User:"
whoami

echo -e "\n[4] Hostname:"
hostname

echo -e "\n[5] OS Details:"
uname -a
cat /etc/os-release

echo -e "\n[6] Kernel Version:"
uname -r

echo -e "\n[7] Architecture:"
uname -m

echo -e "\n[8] Logged in Users:"
who

echo -e "\n[9] Last Boot Time:"
who -b

echo -e "\n[10] CPU Info:"
lscpu | grep -E "Model name|Socket|Thread|Core|MHz"

echo -e "\n[11] Memory Info:"
free -h

echo -e "\n[12] Swap Info:"
swapon --show

echo -e "\n[13] Disk Usage:"
df -h

echo -e "\n[14] Mounted File Systems:"
mount | column -t | head -n 10

echo -e "\n[15] Block Devices:"
lsblk

echo -e "\n[16] PCI Devices:"
lspci | head -n 10

echo -e "\n[17] USB Devices:"
lsusb

echo -e "\n[18] Network Interfaces:"
ip -br addr

echo -e "\n[19] IP Routing Table:"
ip route

echo -e "\n[20] DNS Info:"
cat /etc/resolv.conf

echo -e "\n[21] Firewall Status:"
sudo ufw status 2>/dev/null || echo "ufw not installed"

echo -e "\n[22] SELinux Status (if applicable):"
getenforce 2>/dev/null || echo "SELinux not installed or disabled"

echo -e "\n[23] Environment Variables (short list):"
echo "PATH=$PATH"
echo "HOME=$HOME"
echo "SHELL=$SHELL"
echo "USER=$USER"
echo "LANG=$LANG"

echo -e "\n[24] Full Environment Variables:"
printenv | sort | head -n 10

echo -e "\n[25] Bash Shell Version:"
bash --version | head -n 1

echo -e "\n[26] Bash Configuration Files:"
ls -al ~/.bash*

echo -e "\n[27] Processes Running (top 5 by memory):"
ps aux --sort=-%mem | head -n 6

echo -e "\n[28] Disk Partitions:"
cat /proc/partitions

echo -e "\n[29] Kernel Modules:"
lsmod | head -n 10

echo -e "\n[30] Scheduled Cron Jobs (Current User):"
crontab -l 2>/dev/null || echo "No cron jobs found"

echo -e "\n[31] System Services (first 10):"
systemctl list-units --type=service --state=running | head -n 10

echo -e "\n[32] Open Ports (requires sudo):"
sudo netstat -tulnp | head -n 10

echo -e "\n[33] Systemd Version:"
systemctl --version | head -n 1

echo -e "\n[34] Java Info:"
java -version 2>&1 | head -n 1

echo -e "\n[35] Python Info:"
python3 --version 2>/dev/null || echo "Python3 not installed"

echo -e "\n[36] GCC Info:"
gcc --version | head -n 1

echo -e "\n[37] Top 10 Large Files in Home Directory:"
find ~ -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n 10

echo -e "\n[38] Temp Directory Size:"
du -sh /tmp

echo -e "\n[39] Number of Installed Packages:"
dpkg -l | wc -l 2>/dev/null || rpm -qa | wc -l

echo -e "\n[40] Recent Logins:"
last -n 5

echo -e "\n[41] Reboot History:"
last reboot | head -n 5

echo -e "\n[42] System Log (last 5 lines):"
journalctl -xe --no-pager | tail -n 5

echo -e "\n[43] Kernel Parameters:"
sysctl -a | head -n 10

echo -e "\n[44] File Limits:"
ulimit -a

echo -e "\n[45] Current Working Directory:"
pwd

echo -e "\n[46] Bash Aliases:"
alias | head -n 10

echo -e "\n[47] SSH Status:"
systemctl status ssh | head -n 5

echo -e "\n[48] Active Users Count:"
who | wc -l

echo -e "\n[49] Default Target:"
systemctl get-default

echo -e "\n[50] Files in /etc (first 10):"
ls -lh /etc | head -n 10

echo -e "\n--- END OF SYSTEM INFO SCRIPT ---"

