"""
A programme to scan a document and retun values.
Version: 1
By: KMCD 13/11/2022
"""
import re

# -------------------------------------------------

my_hosts = []

# -------------------------------------------------
# Adding the dictionary so the Mac Address
# check and validate the type of device/Manufacturer
manufacturers = {
    "Ac8:4b:d6": "Dell Device",
    "A18:68:cb": "Hikvision Device",
    "Ac0:25:a5": "Dell Device",
    "Ab8:27:eb": "Raspberry Pi",
    "Aa4:4c:c8": "Dell Device",
    "Abc:5f:f4": "ASRock Device",
    }
# -------------------------------------------------

def parse_line(line,manufacturers):
    """
Using a function to read the DHCPD.LOG file
return results based on patterns found using regualr expressions.
By: KMCD 13/11/2022
"""
    # Find Mac Address (and hostname) in line with re.match
    # If Mac Address not found return none
    # Fine IP address with re.match
    # Look up manufacturer in Manufacturers dictionary
    # Retun list of [mac_address, ip, hostname, manufacturer]
    mac_pattern = ".* (\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2})"
    mac_match=re.match(mac_pattern,line)
    if mac_match == None: mac_address = ""
    else                : mac_address = mac_match[1]

    ip_pattern = ".* (192\\.168\\.\\d{1,3}\\.\\d{1,3})"
    ip_match = re.match(ip_pattern,line)
    if ip_match == None:
        ip_address = ""
    else: ip_address = ip_match[1]

    #Pattern is anything within brackets
    hostname_pattern = ".*(\\([^)]*\\))"
    hostname_match = re.match(hostname_pattern,line)
    if hostname_match == None:
        host_name = "Hostname not found"
    else:host_name = hostname_match[1]

    return [mac_address,ip_address, host_name]
# -------------------------------------------------

def get_manufacturer(manufacturers,mac_address):
    """
Return the manufacturer
from the manufacturers dictionary
By: KMCD 13/11/2022
"""
    short_mac_address=mac_address[:8]
    return manufacturers[short_mac_address]
# -------------------------------------------------

# executes the following code only if this file is..
# run as a script from the command line.
# Standalone script.
if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
    # Open the log file to read
    LOGFILENAME = "dhcpd.log"
    logfile = open(LOGFILENAME, "r")
    # Open a new file to write the output
    csvfile = open("nodes.csv", "w")
    # create an empty dictionary so it processes through mac addresses
    mac_addresses = {}
    # Iterate through every line of the log file
    for line in logfile:
        node_details = parse_line(line,manufacturers)
        if node_details[0] in mac_addresses:
            continue
        mac_addresses[node_details[0]]=""
        print(node_details)
        if "A" +node_details[0][:8] in manufacturers:
            manufacturer=manufacturers["A" +node_details[0][:8]]
        else:
            MANUFACTURER="unknown"
            print("mac_address not in manufacturers")
        #write to a file
        csvfile.write(node_details[0] +"," + node_details[1] +"," + node_details[2] +"," + manufacturer +"\n")
    logfile.close()
    csvfile.close()
else:
    print(f"This module is called {__name__} and is being called by another script")
