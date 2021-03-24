import subprocess
import os
import re

def domainValidator(candidate):
    pattern = "^((.*[a-z].*[a-z].*)[.]){2}"
    return re.search(pattern, candidate)

def validIPAddress_looseBinding(IP):
    patternIPv4 = "((([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9])).){3}(([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9]))"
    patternIPv6 = "([0-9a-fA-F]{1,4}[:]){7}[0-9a-fA-F]{1,4}"
    if re.search(patternIPv4, IP):
        return "IPv4"
    elif re.search(patternIPv6, IP):
        return "IPv6"
    return "Neither"

def traceroute(host):
    cmd = 'traceroute'
    temp = subprocess.Popen([cmd, host], stdout = subprocess.PIPE) 
    output = (str(temp.communicate()).split("\n"))[0].split("\\")
    return (output)

def DirectedAcyclicGraph_Traceroute(host):
    mapping = []
    database = {}
    for line in range(1, len(temp)):
        test = temp[line].split()
        ptr = 0
        domain = []
        ip = []
        time = 0
        while ptr < len(test):
            if domainValidator(test[ptr]) != None:
                domain.append(test[ptr])
            elif validIPAddress_looseBinding(test[ptr]) != "Neither":
                if test[ptr][0] == "(" and test[ptr][-1] == ")":
                    ip.append(test[ptr][1:-1])
                else:
                    ip.append(test[ptr])
            elif re.search("^[0-9]+[.][0-9]+$", str(test[ptr])):
                time += float(test[ptr])
            ptr += 1
        
        if domain != []:
            print("{}: domains and ips found were {}, with an average time of {}".format(line, list(zip(domain,ip)), time))
            for i in list(zip(domain, ip)):
                mapping.append([line, i, time])
        elif ip != []:
            print("{}: ips found were {}, with an average time of {}".format(line, ip, time))
            if len(ip) > 1:
                for i in ip:
                    mapping.append([line, i, time])
            else:
                mapping.append([line, ip, time])
    return mapping

### def generateDAG(arr): ### in progress
