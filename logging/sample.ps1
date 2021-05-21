Get-Process

$host.UI.RawUI.BufferSize = New-Object System.Management.Automation.Host.Size(1000,100)
$processInfo=Get-WmiObject WIN32_PROCESS | Sort-Object -Property ws -Descending | Select-Object -first 10 ProcessID,Name,WS,CommandLine
echo $processInfo