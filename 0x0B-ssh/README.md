# 0x0B. SSH

### Learning Objectives

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash

### Requirements

- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing


## Files

**0-use_a_private_key** 

>>  a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

>> Requirements

- Only use ssh single-character flags
- You cannot use -l
- You do not need to handle the case of a private key protected by a passphrase

**1-create_ssh_key_pair**

>> a Bash script that creates an RSA key pair.

>> Requirements:

- Name of the created private key must be school
- Number of bits in the created key to be created 4096
- The created key must be protected by the passphrase betty

**2-ssh_config**

>> SSH client configuration

>> Requirements:

- Your SSH client configuration must be configured to use the private key ~/.ssh/school
- Your SSH client configuration must be configured to refuse to authenticate using a password


**0x0B-ssh**

>> The SSH public key
