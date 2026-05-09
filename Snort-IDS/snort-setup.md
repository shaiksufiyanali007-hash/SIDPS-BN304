# Snort IDS Setup

## Objective
The purpose of Snort IDS was to monitor network traffic and detect suspicious activity within the SIDPS environment.

---

## Environment
- Ubuntu Virtual Machine
- Kali Linux (Attack Simulation)

---

## Installation Commands

```bash
sudo apt update
sudo apt install snort -y

## Network Interface Identification 
ip a

## Custom Rule was Added for detecting Anomalies
alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001;)

## Running Snort
alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001;)

## Attack Simulation was performed in Kali with help of nmap
nmap -sS <target-ip>

