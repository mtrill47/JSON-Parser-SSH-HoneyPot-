# JSON Parser

This script is designed to word best in a linux environment where it can be integrated with bash commands such as `uniq` and `sort`

The guide on how to setup up the Honey Pot can be found [here](https://scriptkiddiehub.com/2022/03/03/how-to-setup-an-ssh-honeypot/)

The video showing the results of the Honey Pot after 30 days can be found [here](https://youtu.be/I6Li7kIoX1Q)

## Usage

- `Usage: [parser.py](http://parser.py/) <category> ('usernames', 'passwords', 'IP')`

### Sorting Commands

- `python3 [parser.py](http://parser.py/) passwords | sort -n`
- `python3 [parser.py](http://parser.py/) passwords | sort -n | uniq -c`
- `python3 [parser.py](http://parser.py/) passwords | sort -n | uniq -c | sort -n`