import re
import sys


class IpTools:
    def isIpv4(self, string):
        # Regex to match IPv4 address
        regex = r"^((([0-9])|([1-9][0-9])|(1[0-9]{2,2})|(2[0-4][0-9])|(25[0-5]))\.){3,3}(([0-9])|([1-9][0-9])|(1[0-9]{2,2})|(2[0-4][0-9])|(25[0-5]))$"
        if re.fullmatch(regex, string):
            return True
        return False

    def __in_range(self, string, start, end):
        if not self.isIpv4(string):
            return False

        # Check against valid byte range
        def ipBits(ipv4):
            output = ""
            for byte in ipv4.split("."):
                output += f"{int(byte):08b}"
            return int(output)

        startBits, endBits, stringBits = ipBits(start), ipBits(end), ipBits(string)
        return stringBits >= startBits and stringBits <= endBits

    def isPrivateIpv4(self, string):
        return (
            self.__in_range(string, "10.0.0.0", "10.255.255.255")
            or self.__in_range(string, "172.16.0.0", "172.31.255.255")
            or self.__in_range(string, "192.168.0.0", "192.168.255.255")
        )


ipTool = IpTools()

# Test isIpv4
isIpMap = dict()
isIpMap["0.0.0.0"] = True
isIpMap["10.1.75.32"] = True
isIpMap[""] = False
isIpMap["123.456.789.000"] = False
isIpMap["00.00.00.00"] = False
isIpMap["172.31.35.90"] = True
isIpMap["172.32.35.90"] = True
isIpMap["255.255.255.255"] = True
isIpMap["10.43.89.176"] = True
isIpMap["apple"] = False
isIpMap["192.168.1.254.3"] = False
isIpMap["192.168.1.254"] = True

for entry in isIpMap.keys():
    if ipTool.isIpv4(entry) != isIpMap[entry]:
        print(
            f"isIpv4({entry}) expected {isIpMap[entry]} but got output {ipTool.isIpv4(entry)}"
        )

# Test isPrivateIpv4
isIpMap["0.0.0.0"] = False
isIpMap["255.255.255.255"] = False
isIpMap["172.32.35.90"] = False

for entry in isIpMap.keys():
    if ipTool.isPrivateIpv4(entry) != isIpMap[entry]:
        print(
            f"isPrivateIpv4({entry}) expected {isIpMap[entry]} but got output {ipTool.isPrivateIpv4(entry)}"
        )

# Try reading user input for IP addresses
if len(sys.argv) > 1:
    inputs = sys.argv[1:]
else:
    inputs = input("Input comma-delimited list of strings to test:\n").split(",")
print(f"{len(inputs)} input(s): {inputs}")

for entry in inputs:
    if ipTool.isIpv4(entry):
        if ipTool.isPrivateIpv4(entry):
            print(f"{entry} is a private IPv4 address.")
        else:
            print(f"{entry} is a public IPv4 address.")
    else:
        print(f"{entry} is not an IP address.")
