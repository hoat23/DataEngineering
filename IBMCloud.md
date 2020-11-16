# IBM CLOUD

## Access using IBM console

### Install CLI:
- Linux, in console execute this command:
```
curl -sL https://raw.githubusercontent.com/IBM-Cloud/ibm-cloud-developer-tools/master/linux-installer/idt-installer | bash
```
- Windows, in powershell execute this command:
```
[Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"; iex(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/IBM-Cloud/ibm-cloud-developer-tools/master/windows-installer/idt-win-installer.ps1')
```
### 

- Change to the directory where your code is located.
```
cd your_new_directory
```
## Usefull commands

#### Target to Cloud Foundry
```bash
user@cloudshell:~$ ibmcloud target --cf
Targeted Cloud Foundry (http://api.us-south.cf.cloud.ibm.com)
Targeted org user@gmail.com
Targeted space dev

API endpoint:    https://cloud.ibm.com
Region:          us-south
User:            user@gmail.com
Account:         User's Account (id_account)
Resource group:  No resource group targeted, use 'ibma target -g RESOURCE_GROUP'
CF API endpoint: https://api.us-south.cf.cloud.ibm.com (API version: 2.153.0)
Org:             user@gmail.com
Space:           dev
```

#### Show app's list
```bash
user@cloudshell:~$ ibmcloud cf apps
```
We can use a equivalent command:

```bash
user@cloudshell:~$ ibmcloud app list
```

## References
- http://cli.cloudfoundry.org/en-US/v6/
