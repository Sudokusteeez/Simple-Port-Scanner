# Port Scanner

Introduction

The Port Scanner project is a Python script that allows you to scan for open ports on a given IP address. It helps identify potential security vulnerabilities or misconfigurations on your home or business network.

Languages & Programs Used

Python
Visual Studio Code (IDE)
Socket Library

Purpose

The main goal of this project was to ensure the security of my system and network. As I was setting up an FTP server and a VPS via SSH, I wanted to make sure that there were no data leaks or open ports that could be exploited by attackers.

Key Features

Simple and customizable port scanning functionality, enabling users to specify a range of ports to scan on a specific IP address.
Provides insights into the availability and openness of ports, helping to identify potential security vulnerabilities or misconfigurations.

How to Use

Clone the repository: git clone https://github.com/Sudokusteeez/PortScanner.git
Open the Python script using your favorite code editor (e.g., Visual Studio Code).
Modify the target IP address in the script ("10.0.0.206") to the IP address you want to scan.
Run the script, and it will scan ports from 0 to 500 (you can customize the range as needed) on the specified IP address.
The script will output whether each port is open or closed.

Skills Gained

Implementation of socket programming in Python for network communication.
Understanding and application of port scanning techniques to assess network security.
Device enumeration and network awareness to identify potential vulnerabilities.

Disclaimer

This project is intended for educational and testing purposes only. Scanning systems or networks without proper authorization is illegal and unethical. Always obtain permission before scanning any network that does not belong to you.

License
This project is licensed under the MIT License. Feel free to use and modify the code according to the terms of the license.
