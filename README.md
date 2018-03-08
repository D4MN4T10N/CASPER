# 👻 CASPER

For educational use only!
```
Uses socket to connect back to our server that listens for incoming connections, the data is encoded with shitty base64 and a not so secret key since it's in the source code lulz.
```

#### Commands:
* Shell access
* Screenshot
* Download execute
* Persistence
* Clean

#### Anti-VM and Anti-Sandbox:
* Lowest amount of total disk space accepted before executing
* Lowest amount of total memory/ram accepted before executing
* Go through all the running processes in attempt to find known processes
* Go through files in attempt to find known DLL files and drivers
* Go through max 20 network interfaces and match it against known MACs
* Check if a debugger is present with IsDebuggerPresent
* Check for user interaction before main code is executed
* Check for known hostnames
