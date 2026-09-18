import scapy.all as scapy
import datetime
import os
import csv

# Default save location: Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Generate a timestamped CSV filename
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
default_filename = f"captured_packets_{timestamp}.csv"
save_path = os.path.join(desktop_path, default_filename)

# CSV headers
csv_headers = [
    "Timestamp",
    "Source IP",
    "Destination IP",
    "Protocol",
    "Source Port",
    "Destination Port",
    "Packet Size",
    "Traffic Indicator"
]

# Create CSV file with headers
with open(save_path, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)


def analyze_packet(packet):
    """Capture and analyze packets, then save results to CSV in real time."""

    try:
        if packet.haslayer(scapy.IP):

            src_ip = packet[scapy.IP].src
            dst_ip = packet[scapy.IP].dst
            packet_size = len(packet)

            protocol = "OTHER"
            src_port = None
            dst_port = None
            indicator = "Normal"

            # Identify protocol and ports
            if packet.haslayer(scapy.TCP):
                protocol = "TCP"
                src_port = packet[scapy.TCP].sport
                dst_port = packet[scapy.TCP].dport

                if dst_port in [80, 443]:
                    indicator = "Web traffic observed"

            elif packet.haslayer(scapy.UDP):
                protocol = "UDP"
                src_port = packet[scapy.UDP].sport
                dst_port = packet[scapy.UDP].dport

            elif packet.haslayer(scapy.ICMP):
                protocol = "ICMP"
                indicator = "ICMP traffic observed"

            # Basic packet-size indicator
            if packet_size > 1000:
                indicator = "Large packet observed"

            # Store packet information
            packet_info = [
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                src_ip,
                dst_ip,
                protocol,
                src_port,
                dst_port,
                packet_size,
                indicator
            ]

            # Append packet to CSV
            with open(
                save_path,
                mode="a",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                writer = csv.writer(file)
                writer.writerow(packet_info)

            # Display packet information
            print(
                f"[{packet_info[0]}] "
                f"{src_ip}:{src_port} -> {dst_ip}:{dst_port} | "
                f"Protocol: {protocol} | "
                f"Size: {packet_size} bytes | "
                f"{indicator}"
            )

    except Exception as e:
        print(f"Error analyzing packet: {e}")


# Start packet capture
print("🔍 Starting Network Sniffer...")
print(f"📁 Captured packets will be saved to: {save_path}")
print("⏹️ Press Ctrl+C to stop capturing.")

try:
    scapy.sniff(prn=analyze_packet, store=False)

except KeyboardInterrupt:
    print("\n⏹️ Stopping Network Sniffer...")
    print(f"✅ Captured packets saved to: {save_path}")
