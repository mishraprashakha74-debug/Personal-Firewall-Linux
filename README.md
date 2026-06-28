#  Personal Firewall Using Python

A Python-based Personal Firewall developed on **Kali Linux** using **iptables**. This project provides a simple command-line interface to block and unblock IP addresses and view existing firewall rules. It demonstrates the fundamentals of firewall management, Linux networking, and cybersecurity concepts.

---

##  Project Overview

A firewall is one of the most important components of network security. It monitors and controls incoming and outgoing network traffic based on predefined security rules.

This project implements a simple **Personal Firewall** using Python and Linux **iptables** commands. Users can interact with the firewall through a menu-driven interface to:

* Block IP addresses
* Unblock IP addresses
* Display current firewall rules

---

##  Objective

The objective of this project is to understand how firewall rules work in Linux by developing a Python application that interacts with the **iptables** firewall.

---

##  Features

* Block any IP address
* Unblock previously blocked IP addresses
* View current firewall rules
* Menu-driven interface
* Simple and lightweight implementation
* Runs on Kali Linux

---

##  Technologies Used

* Python 3
* Kali Linux
* iptables
* Linux Terminal

---

##  Prerequisites

Before running the project, ensure you have:

* Kali Linux
* Python 3
* sudo privileges
* iptables installed

Verify installation:

```bash
python3 --version
sudo iptables -L
```

---
##  How to Use

When the program starts, the following menu is displayed:

```text
===== PERSONAL FIREWALL =====

1. Block IP
2. Unblock IP
3. Show Rules
4. Exit
```

### Block an IP

Choose:

```text
1
```

Enter an IP address, for example:

```text
8.8.8.8
```

The program adds a firewall rule using iptables.

---

### Unblock an IP

Choose:

```text
2
```

Enter the IP address to remove the firewall rule.

---

### Show Current Rules

Choose:

```text
3
```

The application displays the current iptables firewall rules.

---

##  Learning Outcomes

Through this project, I learned:

* Python programming for cybersecurity
* Linux firewall management
* Using iptables commands
* IP address filtering
* Network security fundamentals
* Command-line application development

---

* Packet inspection and monitoring

---

