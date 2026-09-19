# Network Sniffer & Traffic Analyzer

A Python-based network monitoring tool built with **Scapy** to capture, analyze, and log IPv4 network traffic in real time.

The tool extracts packet-level information such as IP addresses, protocols, ports, packet size, and basic traffic indicators, then stores the captured data in a timestamped CSV file for further analysis.

---

## 🔎 Overview

Network traffic analysis is an important part of security monitoring and incident investigation.

This project demonstrates practical experience with:

- Real-time packet capture
- Network traffic analysis
- TCP/UDP/ICMP identification
- IP and port extraction
- Packet size analysis
- Rule-based traffic indicators
- CSV-based security logging
- Python network security programming

---

## 🚀 Features

- **Real-Time Packet Capture**
  - Captures IPv4 packets using Scapy.

- **Protocol Identification**
  - Identifies TCP, UDP, ICMP, and other IP traffic.

- **IP Address Extraction**
  - Records source and destination IP addresses.

- **Port Analysis**
  - Extracts source and destination ports for TCP and UDP traffic.

- **Packet Size Analysis**
  - Records packet size and flags unusually large packets as a basic traffic indicator.

- **Traffic Indicators**
  - Identifies observed web traffic, ICMP traffic, and large packets using simple rule-based logic.

- **Automatic CSV Logging**
  - Saves captured packet information to a timestamped CSV file.

- **Terminal Monitoring**
  - Displays packet information in real time while capturing.

---

## 🛠️ Technologies Used

- Python
- Scapy
- CSV
- TCP/IP Networking

---

## 📊 Captured Data

Each captured packet can contain:

| Field | Description |
|---|---|
| Timestamp | Time when the packet was processed |
| Source IP | Source IPv4 address |
| Destination IP | Destination IPv4 address |
| Protocol | TCP, UDP, ICMP, or other |
| Source Port | Source port when available |
| Destination Port | Destination port when available |
| Packet Size | Packet size in bytes |
| Traffic Indicator | Basic rule-based traffic observation |

---

## 🔄 Processing Workflow

```text
Network Traffic
      ↓
Packet Capture
      ↓
IPv4 Detection
      ↓
Protocol Identification
      ↓
IP / Port Extraction
      ↓
Packet Size Analysis
      ↓
Traffic Indicator
      ↓
CSV Logging
      ↓
Terminal Output
```

---

### ⚙️ Installation

1. Clone the repository:

git clone https://github.com/Ms-Nasir/Network-Sniffer.git

2. Navigate to the project:

cd Network-Sniffer

3. Install the required dependency:

pip install scapy 

4. Or install from the requirements file:

pip install -r requirements.txt

---

### 🔐 Cybersecurity Applications

This project demonstrates concepts relevant to:

- Security monitoring
- Network traffic analysis
- SOC operations
- Incident investigation
- Network forensics
- Packet analysis
- Detection engineering fundamentals
- Cybersecurity automation

---

### 🎯 Learning Objectives

The project was developed to strengthen practical understanding of:

- Network packet structures
- TCP/IP communication
- Scapy packet manipulation
- Real-time traffic monitoring
- Network security analysis
- Security event logging
- Python automation

---

### 🔮 Future Enhancements

Potential improvements include:

- Advanced anomaly detection
- Packet filtering by protocol, IP, and port
- Network statistics and visualizations
- Detection of port scanning patterns
- Detection of repeated connection attempts
- DNS and HTTP analysis
- Alert severity classification
- PCAP export
- Web-based monitoring dashboard
- Integration with SIEM platforms

--- 

### ⚠️ Limitations

This project currently uses basic rule-based traffic indicators and should not be considered a full Intrusion Detection System (IDS).

The presence of TCP/UDP/ICMP traffic or commonly used ports does not by itself indicate malicious activity.

More advanced detection would require traffic correlation, behavioral analysis, signatures, or machine-learning techniques.

--- 

### ⚖️ Disclaimer

This project is intended for educational, cybersecurity research, and authorized network-monitoring purposes only.

Only capture and analyze traffic on networks where you have appropriate permission.

---

### 👩‍💻 Author

Ms. Nasir

Cybersecurity | SOC Operations | Network Security | Digital Forensics
