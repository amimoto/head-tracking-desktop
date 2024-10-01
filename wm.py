import socket
import struct
import pyvda

# Define the IP and port to listen on
UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 4242      # The port number OpenTrack sends data to

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}...")

# Get the list of available desktops
desktops = pyvda.get_virtual_desktops()

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    
    # Assume the data contains six floats (yaw, pitch, roll, and x, y, z positions)
    x, y, z, yaw, pitch, roll = struct.unpack('dddddd', data)

    if z > 50:
        continue

    target_desktop = 1
    if roll > 5:
        target_desktop = 3
    elif roll < -5:
        target_desktop = 2
    else:
        target_desktop = 1
    current_desktop = pyvda.VirtualDesktop.current()
    if current_desktop != target_desktop:
        pyvda.VirtualDesktop(target_desktop).go()

    # print("{yaw:10.04f} {pitch:10.04f} {roll:10.04f} {x:10.04f} {y:10.04f} {z:10.04f}".format(**rec))
