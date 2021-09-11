import os
import rcon

def run(command):
    with rcon.Client(os.getenv('RCON_IP'), int(os.getenv('RCON_PORT')), passwd=os.getenv('RCON_PASS')) as client:
        response = client.run(command)
    return response