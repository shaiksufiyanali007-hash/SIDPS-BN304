SIDPS‑BN304 Network Security and Design – Project Documentation
This repository contains the design, configuration, and verification of a secure school network built using Cisco Packet Tracer. The project demonstrates VLAN‑based segmentation, trunking, and inter‑VLAN routing using a Router‑on‑a‑Stick architecture, reflecting real‑world enterprise network design principles.

1. Introduction
The network is designed using a hierarchical architecture consisting of:

Four end‑user PCs

Two Layer 2 switches

One router

The objective is to implement secure network segmentation using VLANs and enable controlled communication between them through inter‑VLAN routing.

2. Network Design Overview
The network is divided into two logical VLANs:

VLAN	Purpose	Devices
VLAN 10	Students Network	PC0, PC1 (via Switch0)
VLAN 20	Staff Network	PC2, PC3 (via Switch1)


VLANs improve security, reduce broadcast traffic, and enhance manageability. Switches handle Layer 2 forwarding, while the router provides Layer 3 routing between VLANs.

3. VLAN Configuration
Two VLANs were created on both switches:

VLAN 10 for student devices

VLAN 20 for staff devices

Each switch port was configured as an access port and assigned to the appropriate VLAN. This ensures traffic isolation and creates separate broadcast domains.

4. Trunking Configuration
A trunk link was configured between:

Switch0 ↔ Switch1

Switch1 ↔ Router (G0/0)

The trunk uses IEEE 802.1Q encapsulation to carry multiple VLANs over a single physical interface. This maintains VLAN separation across devices and reduces the need for additional physical links.

5. Router‑on‑a‑Stick Configuration
Inter‑VLAN routing is implemented using router sub‑interfaces:

G0/0.10 → VLAN 10

G0/0.20 → VLAN 20

Each sub‑interface is configured with:

802.1Q encapsulation

A unique IP address serving as the default gateway for its VLAN

This method provides scalable and cost‑effective routing without requiring multiple physical router interfaces.

6. IP Addressing Scheme
VLAN	Network Address	Subnet Mask	Default Gateway
10	192.168.10.0	255.255.255.0	192.168.10.1
20	192.168.20.0	255.255.255.0	192.168.20.1


Each PC was assigned a static IP address within its VLAN and configured to use the router’s sub‑interface as its default gateway.

7. Network Operation and Traffic Flow
Intra‑VLAN Communication  
Devices within the same VLAN communicate directly through Layer 2 switching.

Inter‑VLAN Communication  
Traffic between VLAN 10 and VLAN 20 is routed through the router’s sub‑interfaces.

Trunk Transport  
VLAN‑tagged frames are carried across trunk links using 802.1Q encapsulation.

This structure ensures secure, controlled, and efficient communication across the network.

8. Testing and Verification
Verification steps included:

show vlan brief to confirm VLAN creation and port assignments

show ip interface brief to verify router sub‑interface status

Ping tests for:

Successful communication within the same VLAN

Successful inter‑VLAN communication via the router

All tests confirmed that VLAN segmentation and inter‑VLAN routing were correctly implemented.

9. Screenshots and Evidence
The following screenshots were captured as proof of configuration and functionality:

<video controls src="Cisco Network Simulation .mp4" title="Cisco Simulation"></video>



![VLAN](image.png)


![Router Interface](image-1.png)


![Ping Testing](image-2.png)


# SIDPS System Flow



![System WorkFlow](image-3.png)
