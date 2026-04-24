# Port Scanner

A Python based network port scanner built using socket programming. 
Scans port ranges and identifies open ports on a target system.

## Features
- Takes target IP address as input
- Configurable timeout parameter
- Scans ports from 1 to 1024
- Identifies open and closed ports
- Banner grabbing — extracts service and version information 
  from open ports
- Stores and displays all open ports at end of scan

## How to Run
python port_scanner.py

When prompted:
- Enter target IP address or domain (e.g. 127.0.0.1 or scanme.nmap.org)
- Optional: configure timeout when creating scanner object

## Concepts Used
- Socket programming
- Object Oriented Programming
- Error handling
- Configurable parameters

## Disclaimer
This tool is intended for educational purposes only.
Only scan systems you own or have explicit permission to scan.
Unauthorized port scanning may be illegal in your jurisdiction.
