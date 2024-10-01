iimport socket
import struct

# Define the IP and port to listen on
UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 4242      # The port number OpenTrack sends data to

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}...")

for j in range(10000):
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    
    # Assume the data contains six floats (yaw, pitch, roll, and x, y, z positions)
    rec = {}
    for i, label in enumerate(["x", "y", "z", "yaw", "pitch", "roll"]):
        rec[label] = struct.unpack('d', data[i*8:(i+1)*8])[0]

    print("{yaw:10.04f} {pitch:10.04f} {roll:10.04f} {x:10.04f} {y:10.04f} {z:10.04f}".format(**rec))
