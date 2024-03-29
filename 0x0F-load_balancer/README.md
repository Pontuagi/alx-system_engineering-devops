# 0x0F. Load balancer

### Background

This directory contain Bash scripts to automate work
The scripts are designed to configure a brand new Ubuntu server to match task requirements

### Task Files

######**0-custom_http_response_header**######

**___Requirements___**:

- Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
	- The name of the custom HTTP header must be X-Served-By
	- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write '0-custom_http_response_header' so that it configures a brand new Ubuntu machine to the requirements asked in this task
	- Ignore SC2154 for shellcheck

######**1-install_load_balancer**######

**___Requirements___**:

- Install and configure HAproxy on your lb-01 server.

- Requirements:

	- Configure HAproxy so that it send traffic to web-01 and web-02
	- Distribute requests using a roundrobin algorithm
	- Make sure that HAproxy can be managed via an init script
	- Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow this tutorial.
	- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

