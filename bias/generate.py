# generate.py

"""
Takes: IF and OF and produces bias.py
"""

import json

B_PATH = 'bias.py'
BT_PATH = 'bias-template.py'
IF_PATH = 'IF_PIXEL2.json'
AF_PATH = 'AF.json'

with open(BT_PATH, mode="r", encoding='utf-8') as BT_FP:
    bt = BT_FP.readlines()

with open(IF_PATH, mode="r", encoding='utf-8') as IF_FP:
    IF = json.load(IF_FP)
    print('##################################')
    print('IF: {}'.format(IF['if']))

with open(AF_PATH, mode="r", encoding='utf-8') as AF_FP:
    AF = json.load(AF_FP)
    print('AF: {}'.format(AF['af']))
    print('##################################')

with open(B_PATH, mode="w", encoding='utf-8') as B_FP:
    for line in bt:
        # NOTE: IF
        if line.startswith('lmin'):
            line = 'lmin = "\\x{}"\n'.format(IF['lmin'])
            print(line)
        elif line.startswith('lmax'):
            line = 'lmax = "\\x{}"\n'.format(IF['lmax'])
            print(line)
        elif line.startswith('btadd_le'):
            btadd_le = '"'
            for i in [15, 12, 9, 6, 3, 0]:
                btadd_le += '\\x{}'.format(IF['btadd'][i:i+2])
            btadd_le += '"\n'
            line = 'btadd_le = {}'.format(btadd_le)
            print(line)
        elif line.startswith('btname'):
            line = 'btname = "{}\\x00"\n'.format(IF['btname'])
            print(line)
        elif line.startswith('lmpver'):
            line = 'lmpver = {}\n'.format(IF['lmpver'])
            print(line)
        elif line.startswith('companyid'):
            line = 'companyid = {}\n'.format(IF['companyid'])
            print(line)
        elif line.startswith('subversion'):
            line = 'subversion = {}\n'.format(IF['subversion'])
            print(line)
        elif line.startswith('lmpfp0'):
            lmpfp0 = 'b"'
            line = 'lmpfp0 = {}\n'.format(IF['lmpfp0'])
            for i in [0, 2, 4, 6, 8, 10, 12, 14]:
                lmpfp0 += '\\x{}'.format(IF['lmpfp0'][i:i+2])
            lmpfp0 += '"\n'
            line = 'lmpfp0 = {}'.format(lmpfp0)
            print(line)
        elif line.startswith('lmpfp1'):
            lmpfp1 = 'b"'
            line = 'lmpfp1 = {}\n'.format(IF['lmpfp1'])
            for i in [0, 2, 4, 6, 8, 10, 12, 14]:
                lmpfp1 += '\\x{}'.format(IF['lmpfp1'][i:i+2])
            lmpfp1 += '"\n'
            line = 'lmpfp1 = {}'.format(lmpfp1)
            print(line)
        elif line.startswith('lmpfp2'):
            lmpfp2 = 'b"'
            line = 'lmpfp2 = {}\n'.format(IF['lmpfp2'])
            for i in [0, 2, 4, 6, 8, 10, 12, 14]:
                lmpfp2 += '\\x{}'.format(IF['lmpfp2'][i:i+2])
            lmpfp2 += '"\n'
            line = 'lmpfp2 = {}'.format(lmpfp2)
            print(line)
        elif line.startswith('iocaps'):
            line = 'iocaps = "\\x{}"\n'.format(IF['iocaps'])
            print(line)
        elif line.startswith('authreq'):
            line = 'authreq = "\\x{}"\n'.format(IF['authreq'])
            print(line)
        elif line.startswith('oobdata'):
            line = 'oobdata = {}\n'.format(IF['oobdata'])
            print(line)
        elif line.startswith('deviceclass'):
            deviceclass = 'b"'
            line = 'deviceclass = {}\n'.format(IF['deviceclass'])
            for i in [0, 2, 4]:
                deviceclass += '\\x{}'.format(IF['deviceclass'][i:i+2])
            deviceclass += '"\n'
            line = 'deviceclass = {}'.format(deviceclass)
            print(line)
        # NOTE: AF
        elif line.startswith('internalblue.interface'):
            line  = 'internalblue.interface = internalblue.device_list()'
            line += '[0][{}]\n'.format(AF['hci'])
            print(line)
        elif line.startswith('addrlmin'):
            line = 'addrlmin = {}\n'.format(AF['addrlmin'])
            print(line)
        elif line.startswith('addrlmax'):
            line = 'addrlmax = {}\n'.format(AF['addrlmax'])
            print(line)
        elif line.startswith('addrbtname'):
            line = 'addrbtname = {}\n'.format(AF['addrbtname'])
            print(line)
        elif line.startswith('addrcompanyid'):
            line = 'addrcompanyid = {}\n'.format(AF['addrcompanyid'])
            print(line)
        elif line.startswith('addrsubversion'):
            line = 'addrsubversion = {}\n'.format(AF['addrsubversion'])
            print(line)
        elif line.startswith('addrlmpfp0'):
            line = 'addrlmpfp0 = {}\n'.format(AF['addrlmpfp0'])
            print(line)
        elif line.startswith('addrlmpfp1'):
            line = 'addrlmpfp1 = {}\n'.format(AF['addrlmpfp1'])
            print(line)
        elif line.startswith('addrlmpfp2'):
            line = 'addrlmpfp2 = {}\n'.format(AF['addrlmpfp2'])
            print(line)
        elif line.startswith('addrcapsauth'):
            line = 'addrcapsauth = {}\n'.format(AF['addrcapsauth'])
            print(line)
        elif line.startswith('addroobdata'):
            line = 'addroobdata = {}\n'.format(AF['addroobdata'])
            print(line)
        elif line.startswith('addrdeviceclass'):
            line = 'addrdeviceclass = {}\n'.format(AF['addrdeviceclass'])
            print(line)
        elif line.startswith('addrcode1'):
            line = 'addrcode1 = {}\n'.format(AF['addrcode1'])
            print(line)
        elif line.startswith('addrpatch1'):
            line = 'addrpatch1 = {}\n'.format(AF['addrpatch1'])
            print(line)
        elif line.startswith('addrpatch2'):
            line = 'addrpatch2 = {}\n'.format(AF['addrpatch2'])
            print(line)
        elif line.startswith('addrpatch3'):
            line = 'addrpatch3 = {}\n'.format(AF['addrpatch3'])
            print(line)

        B_FP.write(line)


# print(bt)

