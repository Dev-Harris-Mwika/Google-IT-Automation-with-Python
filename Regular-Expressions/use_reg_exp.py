import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result) 