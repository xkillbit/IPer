# IPer
Tool for generating a random 30% of IPs from a CIDR
# Usage:
```bash
python3 IPer.py -q [CIDR]
```
# Usage Example 1 - SINGLE CIDR:
```bash
python3 IPer.py -q 10.10.10.0/24
```
# Usage Example 2 - LIST OF CIDRS:
```bash
IPer.py -q 10.10.10.0/24,192.168.1.0/24,10.0.0.0/16
```
# Usage Example 3 - LINE SEPARATED CIDR LIST FROM FILE:                                          
```bash
for range in $(cat IP_RANGE_LIST.txt);do python IPer.py -q $range | tee -a thirtypercent.out;done
```

