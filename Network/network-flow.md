# Network Security and Design

# BN304 – Project 2: VLAN Segmentation and Inter‑VLAN Routing for School SIDPS

Overview
For BN304 Project 2, we designed and deployed the network infrastructure for the School Intrusion Detection and Prevention System (SIDPS) using Cisco Packet Tracer. The goal was to implement secure network segmentation through VLANs and enable controlled communication between user groups. This design supports SIDPS by reducing unnecessary broadcast traffic, isolating sensitive staff systems, and preventing unauthorized lateral movement within the school network.

The network follows a hierarchical architecture consisting of two switches, one router, and four end‑user devices. Inter‑VLAN routing was implemented using a Router‑on‑a‑Stick configuration to provide efficient and scalable Layer 3 connectivity.

Tools and Technologies Used
Tool / Technology	Purpose
Cisco Packet Tracer	Network simulation and configuration
VLANs (802.1Q)	Logical segmentation of network traffic
Layer 2 Switches	VLAN assignment and intra‑VLAN forwarding
Router‑on‑a‑Stick	Inter‑VLAN routing using sub‑interfaces
Static IP Addressing	Device identification and gateway configuration
Ping / CLI Commands	Connectivity testing and verification


System Implementation
The network was implemented using a structured, multi‑layer design. Traffic is segmented into two VLANs, transported over trunk links, and routed through sub‑interfaces on the router. Access between VLANs is controlled and monitored to support SIDPS security requirements.

1. VLAN Segmentation
Two VLANs were created to separate student and staff traffic:

VLAN 10 – Students Network

VLAN 20 – Staff Network

Each switch port was configured as an access port and assigned to the appropriate VLAN. This segmentation:

Creates independent broadcast domains

Prevents unnecessary traffic flow between user groups

Enhances security by isolating staff systems from student devices

This forms the first layer of network‑level protection.

2. Trunking Configuration
A trunk link was configured between the switches and the router using IEEE 802.1Q encapsulation.

Key functions:

Carries multiple VLANs over a single physical interface

Preserves VLAN tagging end‑to‑end

Reduces the need for additional physical connections

The trunk ensures that VLAN information is maintained across all network devices.

3. Router‑on‑a‑Stick (Inter‑VLAN Routing)
Inter‑VLAN communication was enabled using router sub‑interfaces:

G0/0.10 → VLAN 10

G0/0.20 → VLAN 20

Each sub‑interface was configured with:

802.1Q encapsulation

A unique IP address acting as the default gateway for its VLAN

This routing method allows devices in different VLANs to communicate securely while maintaining logical separation.

4. IP Addressing Scheme
VLAN	Network Address	Subnet Mask	Default Gateway
10	192.168.10.0	255.255.255.0	192.168.10.1
20	192.168.20.0	255.255.255.0	192.168.20.1


Each PC was assigned a static IP address within its VLAN and configured to use the router’s sub‑interface as its gateway. This ensures proper routing and device identification.

5. Network Operation and Traffic Flow
Intra‑VLAN Communication  
Devices within the same VLAN communicate directly through Layer 2 switching.

Inter‑VLAN Communication  
Traffic between VLAN 10 and VLAN 20 is routed through the router’s sub‑interfaces.

Trunk Transport  
Tagged frames are carried across trunk links using 802.1Q encapsulation.

This layered structure ensures secure, efficient, and controlled communication across the school network.

6. Testing and Verification
The network configuration was validated using several CLI commands and connectivity tests:

show vlan brief to confirm VLAN creation and port assignments

show ip interface brief to verify router sub‑interface status

Ping tests to confirm:

Successful communication within the same VLAN

Successful inter‑VLAN communication via the router

All tests confirmed that VLAN segmentation and inter‑VLAN routing were functioning correctly.

7. Conclusion
The project successfully demonstrates a secure and scalable network design for SIDPS. By combining:

VLAN‑based segmentation

Trunking with 802.1Q

Router‑on‑a‑Stick inter‑VLAN routing

the system provides strong traffic isolation, controlled communication, and improved network security. This design aligns with SIDPS objectives by reducing attack surfaces and preventing unauthorized lateral movement within the school network.

8. Screenshots and Evidence
The following screenshots were captured as proof of configuration and functionality:

<video controls src="Cisco Network Simulation .mp4" title="Cisco Simulation"></video>



![VLAN](image.png)


![Router Interface](image-1.png)


![Ping Testing](image-2.png)


# SIDPS System Flow



![System WorkFlow](image-3.png)
