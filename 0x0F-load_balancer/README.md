# 0x0F. Load balancer

![image](https://user-images.githubusercontent.com/54107524/114489800-5fa83600-9bd9-11eb-93ec-e8bbcad8649c.png)


<h2>Concepts</h2>

<p>
<em>For this project, students are expected to look at these concepts:</em>
</p>

<ul>
    <li>
    <a href="https://intranet.hbtn.io/concepts/46">Load balancer</a>
    </li>
    <li>
    <a href="https://intranet.hbtn.io/concepts/68">Web stack debugging</a>
    </li>
</ul>

<h2>Background Context</h2>

<p>You have been given 2 additional servers:</p>

<ul>
<li>gc-[STUDENT_ID]-`web-02`-XXXXXXXXXX</li>
<li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
</ul>

<p>Let&rsquo;s improve our web stack so that there is <a href="https://en.wikipedia.org/wiki/Redundancy_%28engineering%29" title="redundancy" target="_blank">redundancy</a> for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>

<p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts" title="Introduction to load-balancing and HAproxy" target="_blank">Introduction to load-balancing and HAproxy</a> </li>
<li><a href="https://www.techopedia.com/definition/27178/http-header" title="HTTP header" target="_blank">HTTP header</a> </li>
<li><a href="https://haproxy.debian.net/" title="Debian/Ubuntu HAProxy packages" target="_blank">Debian/Ubuntu HAProxy packages</a></li>
<li><a href="https://linoxide.com/setup-haproxy-ubuntu-16-04/" title="How to Setup HAProxy in Ubuntu 16.04" target="_blank">How to Setup HAProxy in Ubuntu 16.04</a></li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All your files should end with a new line</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>


## Tasks
### 0. Double the number of webservers
In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your [web server project](https://intranet.hbtn.io/projects/266), and they’ll now come in handy to easily configure `web-02`. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

- Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
  - The name of the custom HTTP header must be `X-Served-By`
  - The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
- [Ignore](https://github.com/koalaman/shellcheck/wiki/Ignore) [SC2154](https://github.com/koalaman/shellcheck/wiki/SC2154) for `shellcheck`
- File: **[0-custom_http_response_header](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-load_balancer/0-custom_http_response_header)**

_*Example:*_

```sh
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```

If your server’s hostnames are not properly configured ([STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.), follow this [tutorial](https://aws.amazon.com/es/premiumsupport/knowledge-center/linux-static-hostname/).

---
### 1. Install your load balancer
Install and configure HAproxy on your `lb-01` server.

Requirements:

- Configure HAproxy with version equal or greater than 1.5 so that it send traffic to `web-01` and `web-02`
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this [tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html).
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements
- File: **[1-install_load_balancer](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-load_balancer/1-install_load_balancer)**


_*Example:*_

```sh
sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes

sylvain@ubuntu$
```

---
### 2. Add a custom HTTP header with Puppet
Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

- The name of the custom HTTP header must be `X-Served-By`
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `2-puppet_custom_http_response_header.pp` so that it configures a brand new Ubuntu machine to the requirements asked in this task
- File: **[2-puppet_custom_http_response_header.pp](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-load_balancer/2-puppet_custom_http_response_header.pp)**


