# 0x0E web stack debugging #1

### Key Points

When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with 5 commands in a minute or less:

#### w
- shows server uptime which is the time during which the server has been continuously running
- shows which users are connected to the server
- load average will give you a good sense of the server health - (read more about load here and here)
#### history
- shows which commands were previously run by the user you are currently connected to
- you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
- where you might want to start your debugging work
#### top
- shows what is currently running on this server
- order results by CPU, memory utilization and catch the ones that are resource intensive
#### df
- shows disk utilization

#### netstat
- what port and IP your server is listening on
- what processes are using sockets
- try netstat -lpn on a Ubuntu machine


### Tasks

#### 0-nginx_likes_port_80:

Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

**Requirements:**

- Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
- Write a Bash script that configures a server to the above requirements


#### 1-debugging_made_short

Using what you did for task #0, make your fix short and sweet.

**Requirements**:

- Your Bash script must be 5 lines long or less
- There must be a new line at the end of the file
- You must respect usual Bash script requirements
- You cannot use ;
- You cannot use &&
- You cannot use wget
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
- service (init) must say that nginx is not running ← for real

