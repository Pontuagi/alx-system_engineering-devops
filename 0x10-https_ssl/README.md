# 0x10. HTTPS SSL

## Learning Objectives

- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means\

#### man or help:
- awk
- dig

## Task files:

#### **0-world_wide_web**

- a Bash script that will display information about subdomains

**Requirements:**

- Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
- Add the subdomain lb-01 to your domain, point it to your lb-01 IP
- Add the subdomain web-01 to your domain, point it to your web-01 IP
- Add the subdomain web-02 to your domain, point it to your web-02 IP
- Your Bash script must accept 2 arguments:
	1. domain:
	- type: string
	- what: domain name to audit
	- mandatory: yes
	2. subdomain:
	- type: string
	- what: specific subdomain to audit
	- mandatory: no
- Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
- When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
- When passing domain and subdomain parameters, display information for the specified subdomain
- Ignore shellcheck case SC2086
- Must use:
	- awk
	- at least one Bash function
-You do not need to handle edge cases such as:
	- Empty parameters
	- Nonexistent domain names
	- Nonexistent subdomains


#### **1-haproxy_ssl_termination**

- Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

**Requirements**
- HAproxy must be listening on port TCP 443
- HAproxy must be accepting SSL traffic
- HAproxy must serve encrypted traffic that will return the / of your web server
- When querying the root of your domain name, the page returned must contain Holberton School
- Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)

The file 1-haproxy_ssl_termination must be your HAproxy configuration file
