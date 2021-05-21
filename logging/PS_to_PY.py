from contextlib import redirect_stdout
import subprocess
import re
from io import StringIO
p = subprocess.check_output("PowerShell.exe -Executionpolicy byPass -File C:\\Users\\srijitha.s\\Downloads\\logging\\sample.ps1")
file = StringIO(p.decode())
content=file.read()
#print(content)

regex = r'ProcessID\s+:\s+(\d+)[\r\n]*Name\s+:\s+(\w.+)[\r\n]*WS\s+:\s+(\d+)[\r\n]*CommandLine\s+:\s(.+)?'
results = re.findall(regex,content)
dic={}
s=0

for i in results:
    if i[3]!='\r':
        match='.+'+i[1].strip('\r')
        s=re.search(match,i[3].strip('\r'),re.IGNORECASE).group(0)
    dic[i[0]]=list(i[1:3])
    dic[i[0]].append(s)

print(dic)
print(len(dic))








