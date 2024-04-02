# Dr-Crypto
Simple tool can encrypt and decrypt text files with advanced shifting makes hard to decrypt without this scrypt

## How to use?
- clone the repo
```
git clone https://github.com/mohammed-saleh2007/Dr-Crypto
```

- get the directory
```
cd Dr-Crypto
```

- run with python 
```
~$ python3 main.py
```
output:
```
Please specify either -e or -d option.
try flag -h to learn more
```

- you need to pass flags and argemnts
```
~$ python3 main.py --help
```
output:
```
usage: DR. Crypto
 [-h] [-i INPUT] [-e] [-d] [-o OUTPUT]

encrypt or decrypt any file you want

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        the file to encrypt/decrypt
  -e, --encrypt         Encrypt the file
  -d, --decrypt         Decrypt the file
  -o OUTPUT, --output OUTPUT
                        where is the output file
```

- to encrypt a file
```
python3 main.py -i /path/to/inputfile -e -o /path/to/outputfile
```
for example
```
~$ python3 main.py --input file.txt --encrypt --output encrypted.txt 
```
output:
```
Encrypting file: file.txt to encrypted.txt
file:  file.txt  Encrypted to:  encrypted.txt
```
the file content:
```
~$ cat file.txt
this is the file that we will encrypt to cypher text
then we will decrypt again and return the file to his original file
and we will sum the hash of the file
to be sure that is the right file and there is not any changs

code of no thing: 548654$#!@##$#%$^&*&(*)(_{}{:KJJGQWE**++/**/-*-=-
```
the result of encryption
```
~$ cat encrypted.txt
㒐⩀⬑㎩Ѐ⬑㎩Ѐ㒐⩀⟙Ѐ⢤⬑ⶐ⟙Ѐ㒐⩀Ⓛ㒐Ѐ㝑⟙Ѐ㝑⬑ⶐⶐЀ⟙⽄♉㋄㤱㄀㒐Ѐ㒐〡Ѐ♉㤱㄀⩀⟙㋄Ѐ㒐⟙㡀㒐d㒐⩀⟙⽄Ѐ㝑⟙Ѐ㝑⬑ⶐⶐЀ✐⟙♉㋄㤱㄀㒐ЀⓁ⥱Ⓛ⬑⽄ЀⓁ⽄✐Ѐ㋄⟙㒐㕹㋄⽄Ѐ㒐⩀⟙Ѐ⢤⬑ⶐ⟙Ѐ㒐〡Ѐ⩀⬑㎩Ѐ〡㋄⬑⥱⬑⽄ⓁⶐЀ⢤⬑ⶐ⟙dⓁ⽄✐Ѐ㝑⟙Ѐ㝑⬑ⶐⶐЀ㎩㕹⹩Ѐ㒐⩀⟙Ѐ⩀Ⓛ㎩⩀Ѐ〡⢤Ѐ㒐⩀⟙Ѐ⢤⬑ⶐ⟙d㒐〡Ѐ▄⟙Ѐ㎩㕹㋄⟙Ѐ㒐⩀Ⓛ㒐Ѐ⬑㎩Ѐ㒐⩀⟙Ѐ㋄⬑⥱⩀㒐Ѐ⢤⬑ⶐ⟙ЀⓁ⽄✐Ѐ㒐⩀⟙㋄⟙Ѐ⬑㎩Ѐ⽄〡㒐ЀⓁ⽄㤱Ѐ♉⩀Ⓛ⽄⥱㎩dd♉〡✐⟙Ѐ〡⢤Ѐ⽄〡Ѐ㒐⩀⬑⽄⥱തЀૹઐీ୤ૹઐԐӉсကӉӉԐӉՙԐ⊄֤֤ۤـۤڑـ⍁㬙㴉㬙തᗹᕤᕤᎱᦡᶑኙܹܹۤۤࢡۤۤࢡߩۤߩຉߩd㒐⩀⬑㎩Ѐ⬑㎩Ѐ㒐⩀⟙Ѐ⢤⬑ⶐ⟙Ѐ㒐⩀Ⓛ㒐Ѐ㝑⟙Ѐ㝑⬑ⶐⶐЀ⟙⽄♉㋄㤱㄀㒐Ѐ㒐〡Ѐ♉㤱㄀⩀⟙㋄Ѐ㒐⟙㡀㒐d㒐⩀⟙⽄Ѐ㝑⟙Ѐ㝑⬑ⶐⶐЀ✐⟙♉㋄㤱㄀㒐ЀⓁ⥱Ⓛ⬑⽄ЀⓁ⽄✐Ѐ㋄⟙㒐㕹㋄⽄Ѐ㒐⩀⟙Ѐ⢤⬑ⶐ⟙Ѐ㒐〡Ѐ⩀⬑㎩Ѐ〡㋄⬑⥱⬑⽄ⓁⶐЀ⢤⬑ⶐ⟙dⓁ⽄✐Ѐ㝑⟙Ѐ㝑⬑ⶐⶐЀ㎩㕹⹩Ѐ㒐⩀⟙Ѐ⩀Ⓛ㎩⩀Ѐ〡⢤Ѐ㒐⩀⟙Ѐ⢤⬑ⶐ⟙d㒐〡Ѐ▄⟙Ѐ㎩㕹㋄⟙Ѐ㒐⩀Ⓛ㒐Ѐ⬑㎩Ѐ㒐⩀⟙Ѐ㋄⬑⥱⩀㒐Ѐ⢤⬑ⶐ⟙ЀⓁ⽄✐Ѐ㒐⩀⟙㋄⟙Ѐ⬑㎩Ѐ⽄〡㒐ЀⓁ⽄㤱Ѐ♉⩀Ⓛ⽄⥱㎩dd♉〡✐⟙Ѐ〡⢤Ѐ⽄〡Ѐ㒐⩀⬑⽄⥱തЀૹઐీ୤ૹઐԐӉсကӉӉԐӉՙԐ⊄֤֤ۤـۤڑـ⍁㬙㴉㬙തᗹᕤᕤᎱᦡᶑኙܹܹۤۤࢡۤۤࢡߩۤߩຉߩd% 
```

- to decrypt a file
```
python3 main.py -i /path/to/inputfile -d -o /path/to/outputfile
```
for example:
```
~$ python3 main.py --input encrypted.txt --decrypt --output decrypted.txt
```
output:
```
Decrypting file: encrypted.txt to decrypted.txt
file:  encrypted.txt  Decrypted to:  decrypted.txt
```
the contenct of decrypted.txt:
```
~$ cat decrypted.txt
code of no thing: 548654$#!@##$#%$^&*&(*)(_{}{:KJJGQWE**++/**/-*-=-
this is the file that we will encrypt to cypher text
then we will decrypt again and return the file to his original file
and we will sum the hash of the file
to be sure that is the right file and there is not any changs

code of no thing: 548654$#!@##$#%$^&*&(*)(_{}{:KJJGQWE**++/**/-*-=-
```

## Notes:
- there is a chance to fail to encrypt some chracters and return back without any problems. **tested on arabic and make many problems**

- won't overwrite on the output file this will just add more to the file