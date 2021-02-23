# 0x07. Networking basics #0

<div>
<h2>Resources</h2>

<ul>
<li><a href="https://en.wikipedia.org/wiki/OSI_model" title="OSI model" target="_blank">OSI model</a> </li>
<li><a href="https://www.lifewire.com/lans-wans-and-other-area-networks-817376" title="Different types of network" target="_blank">Different types of network</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Local_area_network" title="LAN network" target="_blank">LAN network</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Wide_area_network" title="WAN network" target="_blank">WAN network</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Internet" title="Internet" target="_blank">Internet</a> </li>
<li><a href="https://whatismyipaddress.com/mac-address" title="MAC address" target="_blank">MAC address</a> </li>
<li><a href="https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/" title="What is an IP address" target="_blank">What is an IP address</a> </li>
<li><a href="https://www.iplocation.net/public-vs-private-ip-address" title="Private and public address" target="_blank">Private and public address</a> </li>
<li><a href="https://www.webopedia.com/insights/ipv6-ipv4-difference/" title="IPv4 and IPv6" target="_blank">IPv4 and IPv6</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Localhost" title="Localhost" target="_blank">Localhost</a> </li>
<li><a href="https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/" title="TCP and UDP" target="_blank">TCP and UDP</a> </li>
<li><a href="https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers" title="TCP/UDP ports List" target="_blank">TCP/UDP ports List</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Ping_%28networking_utility%29" title="What is ping /ICMP" target="_blank">What is ping /ICMP</a> </li>
<li><a href="https://wiki.bash-hackers.org/scripting/posparams" title="Positional parameters" target="_blank">Positional parameters</a> </li>
</ul>

<p><strong>Man or help</strong>:</p>

<ul>
<li><code>netstat</code></li>
<li><code>ping</code></li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All your Bash script files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>shellcheck</code> without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>
</div>

## Tasks

### 0. OSI model

OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![iso_model](https://user-images.githubusercontent.com/54107524/108866764-7e6b5280-75c2-11eb-82f1-57fbdf05a42c.png)

In this project we will mainly focus on:

- The Transport layer and especially TCP/UDP
- On the Network layer with IP and ICMP

The image bellow describes more concretely how you can relate to every level.

![iso_model2](https://user-images.githubusercontent.com/54107524/108866856-98a53080-75c2-11eb-9388-e4297dd7b121.png)

**Questions:**

What is the OSI model?

1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

1. Alphabetically
2. From the lowest to the highest level
3. Randomly

- File: **[0-OSI_model](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x07-networking_basics/0-OSI_model)**

---

### 1. Types of network

![image](https://user-images.githubusercontent.com/54107524/108867219-f9cd0400-75c2-11eb-99cf-e5687e964784.png)

LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

**Questions:**

What type of network a computer in local is connected to?

1. Internet
2. WAN
3. LAN

What type of network could connect an office in one building to another office in a building a few streets away?

1. Internet
2. WAN
3. LAN

What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?

1. Internet
2. WAN
3. LAN

- File: **[1-types_of_network](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x07-networking_basics/1-types_of_network)**

---

### 2. MAC and IP address

![image](https://user-images.githubusercontent.com/54107524/108867675-6ea03e00-75c3-11eb-89ae-4a231065b03f.png)

**Questions:**

What is a MAC address?

1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface

What is an IP address?

1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

- File: **[2-MAC_and_IP_address](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x07-networking_basics/2-MAC_and_IP_address)**

---

### 3. UDP y TCP

![image](https://user-images.githubusercontent.com/54107524/108868002-c6d74000-75c3-11eb-9753-2b198c2f8d3e.png)

Let’s fill the empty parts in the drawing above.

**Questions:**

- Which statement is correct for the TCP box:

1. `It is a protocol that is transferring data in a slow way but surely`
2. `It is a protocol that is transferring data in a fast way and might loss data along in the process`

- Which statement is correct for the UDP box:

1. `It is a protocol that is transferring data in a slow way but surely`
2. `It is a protocol that is transferring data in a fast way and might loss data along in the process`

- Which statement is correct for the TCP worker:

1. `Have you received boxes x, y, z?`
2. `May I increase the rate at which I am sending you boxes?`

- File: **[3-UDP_and_TCP](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x07-networking_basics/3-UDP_and_TCP)**

---

### 4. TCP and UDP ports

Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

- **22** for SSH
- **80** for HTTP
- **443** for HTTPS

Note that a specific [IP + port = socket](https://stackoverflow.com/questions/152457/what-is-the-difference-between-a-port-and-a-socket).

Write a Bash script that displays listening ports:

- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs
- File: **[4-TCP_and_UDP_ports](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x07-networking_basics/4-TCP_and_UDP_ports)**

**_Example:_**

```zsh
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
```

---

### 5. Is the host on the network

The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

- Accepts a string as an argument
- Displays `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
- Ping the IP 5 times

**_Example:_**

```zsh
sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$
```

It is interesting to look at the `time` value, which is the time that it took for the ICMP request to go to the `8.8.8.8` IP and come back to my host. The IP `8.8.8.8` is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the `ping` command to see what is going on!

- File: **[5-is_the_host_on_the_network](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x07-networking_basics/5-is_the_host_on_the_network)**

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
