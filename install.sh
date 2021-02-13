#!/usr/bin/bash
# This code write by (ms.nope)
echo "        installing..."

git clone https://github.com/msprogrammer2938/webscan.git

cd webscan

bash install.sh

python3 scanweb.py
# scanweb
