# WiFiPassRecovery
WiFi Password Recovery tool written in Python3

## Installation:
Clone the repository -
```
$ git clone https://github.com/priyamharsh14/WiFiPassRecovery.git
```
Change the directory -
```
$ cd WiFiPassRecovery
\WiFiPassRecovery\$
```

## Usage:
Type this to view the help menu -
```
\WiFiPassRecovery\$ python WPR.py --help

██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║█████╗  ██║
██║███╗██║██║██╔══╝  ██║
╚███╔███╔╝██║██║     ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝

        ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
        ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
        ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
        ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

                ██████╗ ███████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗
                ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝
                ██████╔╝█████╗  ██║     ██║   ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝
                ██╔══██╗██╔══╝  ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝
                ██║  ██║███████╗╚██████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║   ██║
                ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝


Author: Priyam Harsh
Usage: WPR.py [options] filename

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -o OUTFILENAME, --output=OUTFILENAME
                        Output File Name
```

To view password of any specified Access Point -
```
\WiFiPassRecovery\$ python WPR.py
```
and choose your desired Acess Point to view its password.


To export all the Access Points with its password -
```
\WiFiPassRecovery\$ python WPR.py -o <Output File Name>
```
