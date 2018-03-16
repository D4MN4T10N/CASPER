# 👻 CASPER

For educational use only!

#### Installation:
    * pip install -r requirements.txt

#### Commands:
    * shell cmd                   <sends shell command>
    * download url                <download and execute via shell>
    * schtasks create/delete/run  <create/delete/run schtasks tasks>
    * intercept proxy/dns         <set a proxy or change dns server>
    * clone                       <clones myself to temp directory>
    * infect                      <adds itself to startup via registry>
    * screenshot                  <takes screenshot>
    * removal                     <remove myself>
    * quit                        <quit server>

#### C&C:
Test the connection against google server before we connects back to command server where we are listning for incoming connections. The data between server and CASPER is encoded with base64 using a key to obfuscate it a little bit.

The sample server can only handle one connection at the time, might make a multithreaded one in the future.

#### Evasion techniques:
* Lowest amount of total disk space accepted before executing
* Lowest amount of total memory/ram accepted before executing
* Go through all the running processes in attempt to find known processes
* Go through files in attempt to find known DLL files and drivers
* Go through max 20 network interfaces and match it against known MACs
* Check if a debugger is present with IsDebuggerPresent
* Check for user interaction before main code is executed
* Check for known hostnames

#### Add a function(s):
Navigate to \framework\ folder and edit includes.py to import your function, call the function(s) from control.py, make sure your function returns True or False in order to make the response to C&C server easier.

#### Known issues:
* Server only handles one connection at the same time
* When building you might get Access Denied errors depending on OS (Rebuild until success)
* When passing wrong or to many parameters, CASPER might disconnect and reconnect due to error/exception
