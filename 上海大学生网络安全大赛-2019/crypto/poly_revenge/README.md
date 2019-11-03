# poly_revenge

其实跟第一题一样，算出 key 之后就很好做了：

```python
#!/usr/bin/env sage

P=PolynomialRing(GF(2),'x')
F.<x> = GF(2)[]
base = x**255+ x**143+ x**47 + x**3 + 1
FF = GF(2**256)

r1 = 0x8eeb27d8c2776920bd4672bbcee6d1ebf357c81419e2c3e2073a1e241dbd
r2 = 0x8e4188999c007557e481d4dfcf51a8bb92a752ebac7015967f1133387c7c
c1 = 0x237b20405cf83f261749fba5507ed14cb566e3722a93308c7752297d92a8338c
c2 = 0x1f8fe9b5e32500c3d306924938d1f443b3718ec410c380944503311ff932f528

def getPoly(c):
	b = bin(c)[2:].zfill(256)[::-1]
	p = 0
	for i in range(256):
		if b[i] == '1':
			p += x**i
	return p

h1 = getPoly(c1)
h2 = getPoly(c2)

f1 = getPoly(r1)
f2 = getPoly(r2)

key_1 = (h1-h2)*inverse_mod((f1-f2),base)%base
key_2 = (h1-f1*key_1)%base
print 'key_1:', key_1
print 'key_2:', key_2

ciphertext1 = 0x1a99ff13954d42e6a21af67aa58e2df8b7bec68f499edf992c95b25326ed768c
ciphertext2 = 0x1e63622141285872093eda8da6c7a94ad7c50e695fdc6ed9bd8adaf4c6c40b14

ch1 = getPoly(ciphertext1)
ch2 = getPoly(ciphertext2)
plaintext1 = (ch1-key_2)*inverse_mod(key_1,base)%base
plaintext2 = (ch2-key_2)*inverse_mod(key_1,base)%base

def getNum(p):
	tmp = p.exponents()
	b = ''
	for i in range(256):
		if i in tmp:
			b += '1'
		else:
			b += '0'
	return hex(int(b[::-1], 2)).lstrip('0x').rstrip('L').zfill(64)

flag1 = getNum(plaintext1)
flag2 = getNum(plaintext2)
print flag1
print flag2
```

![](./1.png)
