# Snort IDS Setup and Attack Simulation

# BN304 – Project 2: Intrusion Detection Using Snort in a Virtualized Environment

Step 1: Create Two Virtual Machines
Two virtual machines were created in Oracle VirtualBox to build a controlled IDS testing environment.

VM	Purpose
Ubuntu Server	Snort IDS machine
Kali Linux	Attacker machine


This setup allowed safe simulation of cyberattacks and real‑time intrusion detection using Snort.

Step 2: Configure VirtualBox Network
Both VMs were configured with:

Adapter 1: Internal Network (for VM‑to‑VM communication)

Adapter 2: NAT (optional, for internet access if required)

Internal networking ensures isolated communication between Ubuntu (Snort) and Kali (attacker), without exposing the environment externally.

Step 3: Start Ubuntu Server and Update System
After logging into Ubuntu Server, the system was updated:

Code
sudo apt update
sudo apt upgrade -y
The update completed successfully, confirming the machine was ready for Snort installation.

Step 4: Identify Network Interface
Snort requires the correct monitoring interface. The available interfaces were checked using:

Code
ip a
The VM displayed:

lo

enp0s3

enp0s8

The active internal network interface was enp0s8, so this interface was used for Snort monitoring.

Step 5: Install Snort
Snort was installed using:

Code
sudo apt install snort -y
During installation, the HOME_NET IP range and network interface were configured. After correcting the interface to enp0s8, Snort installed successfully.

Step 6: Verify Snort Installation
Snort was verified using:

Code
sudo snort -v
Snort successfully captured packets, confirming that the installation was working.

Step 7: Configure Snort
Open Snort Configuration File
Code
sudo nano /etc/snort/snort.conf
Using Ctrl + W, the local.rules section was located to ensure the file was included:

Code
include $RULE_PATH/local.rules
Add Custom Rule
Open the local rules file:

Code
sudo nano /etc/snort/rules/local.rules
Add ICMP detection rule:

Code
alert icmp any any -> any any (msg:"Ping Detected"; sid:1000001; rev:1;)
Save and exit.

Step 8: Start Snort in Alert Mode
Snort was started in console alert mode:

Code
sudo snort -A console -i enp0s8 -c /etc/snort/snort.conf
Snort began processing packets and monitoring traffic on the enp0s8 interface.

Step 9: Validate Snort Configuration
Code
sudo snort -T -c /etc/snort/snort.conf
The configuration test returned valid, confirming no syntax errors.

Step 10: Start Kali Linux
Kali Linux was started to simulate attacks.
Ubuntu’s IP address was confirmed as:

Code
10.0.3.15
Step 11: Ping Attack Simulation
Snort was restarted:

Code
sudo snort -A console -q -c /etc/snort/snort.conf -i enp0s8
From Kali:

Code
ping 10.0.3.15
Snort successfully detected ICMP packets and displayed Ping Detected alerts.

Step 12: Perform Nmap Scan
Snort was restarted in console mode:

Code
sudo snort -A console -i enp0s8 -c /etc/snort/snort.conf
From Kali:

Code
sudo nmap -sS 10.0.3.15
The SYN scan successfully reached the Ubuntu machine, confirming communication between both VMs.

Step 13: Add Nmap Detection Rule
Open local rules:

Code
sudo nano /etc/snort/rules/local.rules
Add custom SYN scan detection rule:

Code
alert tcp any any -> any 80 (flags:S; msg:"Possible Nmap SYN Scan Detected"; sid:1000002; rev:1;)
Test configuration:

Code
sudo snort -T -c /etc/snort/snort.conf
Restart Snort:

Code
sudo snort -A console -i enp0s8 -c /etc/snort/snort.conf
Run Nmap again from Kali:

Code
sudo nmap -sS 10.0.3.15
Snort successfully generated alerts for the SYN scan.

Conclusion
This project demonstrated the full installation, configuration, and testing of Snort IDS in a virtualized environment. Using Kali Linux to simulate ICMP and Nmap attacks, Snort successfully detected suspicious activity in real time. The practical exercise provided hands‑on experience with intrusion detection, rule creation, attack simulation, and network monitoring.