# 👻 CASPER

For educational use only!

#### Simple C&C:
Connects back to command server where we are listning for incoming connections. The data between server and casper is encoded with base64 encoding using a key to obfuscate it a little bit. 

#### Commands:
    * shell cmd                   <sends shell command>
    * download url                <download and execute via shell>
    * schtasks create/delete/run  <create/delete/run schtasks tasks>
    * clone                       <clones myself to temp directory>
    * infect                      <adds itself to startup via registry>
    * screenshot                  <takes screenshot>
    * removal                     <remove myself>
    * quit                        <quit server>

#### Anti-VM and Anti-Sandbox:
* Lowest amount of total disk space accepted before executing
* Lowest amount of total memory/ram accepted before executing
* Go through all the running processes in attempt to find known processes
* Go through files in attempt to find known DLL files and drivers
* Go through max 20 network interfaces and match it against known MACs
* Check if a debugger is present with IsDebuggerPresent
* Check for user interaction before main code is executed
* Check for known hostnames
