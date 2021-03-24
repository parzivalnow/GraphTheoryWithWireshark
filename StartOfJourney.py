#######################
# Reference Used
# https://incognitjoe.github.io/reading-pcap-with-scapy.html
#######################

# Identify the nodes and edges. Here we will store the protocols that are being used between the endpoints (for topological sorting/selection).
# This is a very easy script but will be expanded upon each and every day. 

!pip install scapy
from scapy.all import *

packets = rdpcap('/home/parzival/firstFile.pcapng')

whosTalkingToWho = {}

for packet in packets.sessions():
    src, dest = packet.split('>')
    srcDest = tuple([src.split()[1], dest])
    if srcDest not in whosTalkingToWho.keys():
        whosTalkingToWho[srcDest] = [src.split()[0]]
    elif src.split()[0] not in whosTalkingToWho[srcDest]:
        whosTalkingToWho[srcDest].append(src.split()[0])
        
for key, val in whosTalkingToWho.items():
    print(key)
    print(val)
    print("_______")
