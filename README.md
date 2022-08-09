# IPer
Tool for generating a random 30% of IPs from a CIDR
# Usage:
```bash
python3 IPer.py -q [CIDR]
```
# Usage Example 1:
```bash
python3 IPer.py -q 10.10.10.0/24
```

# Usage Example 2:
```bash
sudo tee -a IP_RANGE_LIST.txt > /dev/null <<EOT
10.10.10.0/24
10.10.50.0/24
EOT
```                                            
```bash
for range in $(cat IP_RANGE_LIST.txt);do python IPer.py -q $range | tee -a thirtypercent.out;done
```

