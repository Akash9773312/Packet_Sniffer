import argparse
import os

from core import PacketSniffer
from output import OutputToScreen

parser = argparse.ArgumentParser(description = "Network Packet Sniffer")
parser.add_argument(
    "-i", "--interface",
    type = str,
    default = None,
    help = "Interface from which Ethernet frame will be captured."
)

parser.add_argument(
    "-d", "--data", 
    action="store_true",
    help="Output Packet data during capture"
)

_args = parser.parse_args()

if os.getuid() != 0:
    raise SystemExit("Error:Pernmission denied. This application requires administrator priviledges to run.")

OutputToScreen(
    subject=(sniffer := PacketSniffer()), 
    display_data = _args.data 
)

try:
    for _ in sniffer.listen(_args.interface):
        pass
except KeyboardInterrupt:
    raise SystemExit("[!] Aborting packet capture.....") 