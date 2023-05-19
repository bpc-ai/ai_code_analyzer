import re
from configparser import ConfigParser

configure = ConfigParser()
configure.read('config.ini')

out_regex = configure.get('map', 'OUT')
inp_regex = configure.get('map', 'INP')
if_regex = configure.get('map', 'IF')
asg_regex = configure.get('map', 'ASG')
for_regex = configure.get('map', 'FOR')
brk_regex = configure.get('map', 'BRK')
cnt_regex = configure.get('map', 'CNT')
ret_regex = configure.get('map', 'RET')

regex_map = dict()
regex_map['OUT'] = re.compile(out_regex)
regex_map['INP'] = re.compile(inp_regex)
regex_map['IF'] = re.compile(if_regex)
regex_map['ASG'] = re.compile(asg_regex)
regex_map['FOR'] = re.compile(for_regex)
regex_map['BRK'] = re.compile(brk_regex)
regex_map['CNT'] = re.compile(cnt_regex)
regex_map['RET'] = re.compile(ret_regex)
