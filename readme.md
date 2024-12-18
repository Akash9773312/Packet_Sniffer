# Python 3 Network Packet Sniffer

![Python Version](https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=for-the-badge&logo=linux)

A Network Packet Sniffer developed in Python 3. Packets are disassembled
as they arrive at a given network interface controller and their information
is displayed on the screen.

## Running the Application
### I. Development Mode
Simply clone this repository with `git clone`, install the dependencies and execute the 
`sniffer.py` file.
```
user@host:~$ git clone https://github.com/Akash9773312/Packet_Sniffer.git
user@host:~$ cd Packet_Sniffer
user@host:~/packet-sniffer$ pip install -r requirements.txt <--or--> poetry install
user@host:~/packet-sniffer$ sudo python3 packet_sniffer/sniffer.py
```

*The `sudo` command is required due to the use of `socket.SOCK_RAW`,
which needs administrative privileges to run on GNU/Linux. Notice
that the existence of dependencies may require the execution of the interpreter contained in
the virtual environment in which the dependencies have been installed (if you use one),
instead of just using the system interpreter.*

### II. (Optional) Build the binary
Use the `build.py` file to compile your own binary with the `PyInstaller` package. You just need to install all dependencies and build. 
Dependency management works with both [Poetry](https://python-poetry.org/) (recommended) and [Virtualenv](https://virtualenv.pypa.io/en/latest/). 
```
<-- Install dependencies as shown above in Step I -->
user@host:~/packet-sniffer$ python3 build.py
```

## Usage
```
sniffer.py [-h] [-i INTERFACE] [-d]

Network Packet Sniffer

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Interface from which packets will be captured (monitors
                        all available interfaces by default).
  -d, --data            Output packet data during capture.
```

## Legal Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

Developers assume **no liability** and are not
responsible for misuses or damages caused by any code contained
in this repository in any event that, accidentally or otherwise, it comes to
be utilized by a threat agent or unauthorized entity as a means to compromise
the security, privacy, confidentiality, integrity, and/or availability of
systems and their associated resources. In this context the term "compromise" is
henceforth understood as the leverage of exploitation of known or unknown vulnerabilities
present in said systems, including, but not limited to, the implementation of
security controls, human- or electronically-enabled.

The use of this code is **only** endorsed by the developers in those
circumstances directly related to **educational environments** or
**authorized penetration testing engagements** whose declared purpose is that
of finding and mitigating vulnerabilities in systems, limiting their exposure
to compromises and exploits employed by malicious agents as defined in their
respective threat models.
