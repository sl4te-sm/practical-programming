import re


class IpTools:
    def isIpv4(self, input):
        # Regex to match IPv4 address
        regex = r"^((([0-9])|([1-9][0-9])|(1[0-9]{2,2})|(2[0-4][0-9])|(25[0-5]))\.){3,3}(([0-9])|([1-9][0-9])|(1[0-9]{2,2})|(2[0-4][0-9])|(25[0-5]))$"
        if re.fullmatch(regex, input):
            return True
        return False


ipTool = IpTools()

# Test isIpv4
isIpMap = dict()
isIpMap["0.0.0.0"] = True
isIpMap[""] = False
isIpMap["123.456.789.000"] = False
isIpMap["00.00.00.00"] = False
isIpMap["255.255.255.255"] = True
isIpMap["10.43.89.176"] = True
isIpMap["apple"] = False
isIpMap["192.168.1.254.3"] = False

for entry in isIpMap.keys():
    if ipTool.isIpv4(entry) != isIpMap[entry]:
        print(
            f"{entry} expected {isIpMap[entry]} but got output {ipTool.isIpv4(entry)}"
        )
