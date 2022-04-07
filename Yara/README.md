# YARA

> Shahrukh Tramboo | April 7th, 2022

--------------------------------------

**Introduction to Yara Rules**

Using a Yara rule is simple. Every yara command requires two arguments to be valid, these are:
1) The rule file we create
2) Name of file, directory, or process ID to use the rule for.

Every rule must have a name and condition.

```bash
yara myrule.yar somedirectory
```

yar file example:
```bash
rule examplerule {
	condition: true
}
```

The name of the rule in this snippet is <b>examplerule</b>, where we have one condition - in this case, the condition is <b>condition</b>.

Simply, the rule we have made checks to see if the file/directory/PID that we specify exists via <b>condition: true</b>. If the file does exist, we are given the output of <b>examplerule</b>

Let's give this a try on the file "some file" that we made in step one:
```bash
yara myfirstrule.yar somefile
```
