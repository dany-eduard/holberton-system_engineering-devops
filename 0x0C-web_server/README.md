# 0x0C. Web server

<h2>Concepts</h2>

<p>
<em>For this project, students are expected to look at these concepts:</em>
</p>

<ul>
    <li>
    <a href="/concepts/12">DNS</a>
    </li>
    <li>
    <a href="/concepts/17">Web Server</a>
    </li>
    <li>
    <a href="/concepts/43">CI/CD</a>
    </li>
    <li>
    <a href="/concepts/65">Docker</a>
    </li>
    <li>
    <a href="/concepts/68">Web stack debugging</a>
    </li>
    <li>
    <a href="/concepts/110">What is a Child Process?</a>
    </li>
    <li>
    <a href="/concepts/124">DevOps</a>
    </li>
    <li>
    <a href="/concepts/125">System Administration</a>
    </li>
    <li>
    <a href="/concepts/126">Site Reliability Engineering</a>
    </li>
</ul>

![image Web Server](https://user-images.githubusercontent.com/54107524/113698995-a4444680-969a-11eb-94dd-a4b0ea5a6ad3.png)

<p>In this project, some of the tasks will be graded on 2 aspects:</p>

<ol>
<li>Is your <code>web-01</code> server configured according to requirements</li>
<li>Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)</li>
</ol>

<p>For example, if I need to create a file <code>/tmp/test</code> containing the string <code>hello world</code> and modify the configuration of Nginx to listen on port <code>8080</code> instead of <code>80</code>, I can use <code>emacs</code> on my server to create the file and to modify the Nginx configuration file <code>/etc/nginx/sites-enabled/default</code>.</p>

<p>But my answer file would contain:</p>

<pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i &#39;s/80/8080/g&#39; /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>

<p>As you can tell, I am not using <code>emacs</code> to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an <a href="https://www.atlassian.com/incident-management/devops/sre" title="SRE" target="_blank">SRE</a>, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the <code>root</code> user, you do not need to use the <code>sudo</code> command.</p>

<p>A good Software Engineer is a <a href="https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb" title="lazy Software Engineer" target="_blank">lazy Software Engineer</a>.
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" alt="" style="" /></p>

<p>Tips: to test your answer Bash script, feel free to reproduce the checker environment: </p>

<ul>
<li>start an <code>ubuntu:16.04</code> Docker container</li>
<li>run your script on it</li>
<li>see how it behaves</li>
</ul>

<p>Check out the Docker concept page for more info about how to manipulate containers.</p>

<h2>Resources</h2>

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works" title="How the web works" target="_blank">How the web works</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Nginx" title="Nginx" target="_blank">Nginx</a> </li>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04" title="How to Configure Nginx" target="_blank">How to Configure Nginx</a></li>
<li><strong>Child process</strong> concept page</li>
<li><a href="https://landingi.com/help/root-domain-subdomain-differences/" title="Root and sub domain" target="_blank">Root and sub domain</a> </li>
<li><a href="https://www.tutorialspoint.com/http/http_methods.htm" title="HTTP requests" target="_blank">HTTP requests</a> </li>
<li><a href="https://moz.com/learn/seo/redirection" title="HTTP redirection" target="_blank">HTTP redirection</a> </li>
<li><a href="https://en.wikipedia.org/wiki/HTTP_404" title="Not found HTTP response code" target="_blank">Not found HTTP response code</a> </li>
<li><a href="https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/" title="Logs files on Linux" target="_blank">Logs files on Linux</a> </li>
</ul>

<p><strong>For reference:</strong></p>

<ul>
<li><a href="https://tools.ietf.org/html/rfc7231" title="RFC 7231 (HTTP/1.1)" target="_blank">RFC 7231 (HTTP/1.1)</a></li>
<li><a href="https://tools.ietf.org/html/rfc7540" title="RFC 7540 (HTTP/2)" target="_blank">RFC 7540 (HTTP/2)</a></li>
</ul>

<p><strong>Man or help</strong>: </p>

<ul>
<li><code>scp</code></li>
<li><code>curl</code></li>
</ul>

<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
<li>You can&rsquo;t use <code>systemctl</code> for restarting a process</li>
</ul>


## Tasks

### 0. Transfer a file to your server
Write a Bash script that transfers a file from our client to a server:

Requirements:

- Accepts 4 parameters
    1. The path to the file to be transferred
    2. The IP of the server we want to transfer the file to
    3. The username `scp` connects with
    4. The path to the SSH private key that scp uses
- Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`
- File: **[0-transfer_file](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0C-web_server/0-transfer_file)**

_*Example:*_

```sh
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```

In this example, I:

- remotely execute the `ls ~/` command via `ssh` to see what `~/` contains
- create a file named `some_page.html`
- execute my `0-transfer_file` script
- remotely execute the `ls ~/` command via ssh to see that the file `some_page.html` has been successfully transferred

That is one way of publishing your website pages to your server.

---
### 1. Install nginx web server
Readme:

[-y on apt-get command](https://askubuntu.com/questions/672892/what-does-y-mean-in-apt-get-y-install-command)

Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

- Install `nginx` on your web-01 server
- Nginx should be listening on port 80
- When querying Nginx at its root / with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Holberton School`
- As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- You can’t use `systemctl` for restarting nginx
- File: **[1-install_nginx_web_server](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0C-web_server/1-install_nginx_web_server)**


_*Server terminal::*_

```sh
root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Holberton School for the win!
root@sy-web-01$ 
```


_*Local terminal::*_

```sh
sylvain@ubuntu$ curl 34.198.248.145/
Holberton School for the win!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
```

In this example `34.198.248.145` is the IP of my web-01 server. If you want to query the Nginx that is locally installed on your server, you can use `curl 127.0.0.1`.

If things are not going as expected, make sure to check out Nginx logs, they can be found in `/var/log/`.

---
### 2. Setup a domain name
[.TECH Domains](https://get.tech/) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](https://intranet.hbtn.io/dashboards/my_tools). Feel free to drop a thank you tweet for [.TECH Domains](https://twitter.com/dottechdomains).

Provide the domain name in your answer file.

Requirement:

- provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
- configure your DNS records with an A entry so that your root domain points to your web-01 IP address **Warning: the propagation of your records can take time (~1-2 hours)**
- go to your profile and enter your domain in the Project website url field
- File: **[2-setup_a_domain_name](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0C-web_server/2-setup_a_domain_name)**

_*Example:*_

```sh
sylvain@ubuntu$ cat 2-setup_a_domain_name
holbertonschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig holbertonschool.tech

; <<>> DiG 9.10.6 <<>> holbertonschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;holbertonschool.tech.      IN  A

;; ANSWER SECTION:
holbertonschool.tech.   7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
```

When your domain name is setup, please verify the Registrar here: https://whois.whoisxmlapi.com/ and you must see in the JSON response: `"registrarName": "Dotserve Inc"`

---
### 3. Redirection
Readme:

- [Replace a line with multiple lines with sed](https://stackoverflow.com/questions/26041088/sed-replace-line-with-multiline-variable)

Configure your Nginx server so that `/redirect_me` is redirecting to another page.

Requirements:

- The redirection must be a “301 Moved Permanently”
- You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
- Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task
- File: **[3-redirection](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0C-web_server/3-redirection)**

_*Example:*_

```sh
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```

---
### 4. Not found page 404
Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

Requirements:

- The page must return an HTTP 404 error code
- The page must contain the string Ceci n'est pas une page
- Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task
- File: **[4-not_found_page_404](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0C-web_server/4-not_found_page_404)**

_*Example:*_

```sh
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
```

---
### 5. Design a beautiful 404 page
Some of my favorites:

[Digital Ocean](https://www.digitalocean.com/community/tutorials/holbertonschool)
[GitHub](https://github.com/holbertonschool/pagenotfound)
[Lego](https://www.lego.com/en-us/404)
[Blizzard](https://www.blizzard.com/es-es/)
[StickerMule](https://www.stickermule.com/404)

Get creative and impress us!

Note that if you decide to have your creative 404 page as the default one, make sure that it still contains the string Ceci n'est pas une page (otherwise the checker will fail your previous project).

Submit the URL of your 404 page in the field bellow.
- URL: **[]()**
- File: **[5-design_a_beautiful_404_page](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0C-web_server/5-design_a_beautiful_404_page)**

---
### 6. Install Nginx web server (w/ Puppet)
Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

Requirements:

- Nginx should be listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string Holberton School
- The redirection must be a “301 Moved Permanently”
- Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
- File: **[7-puppet_install_nginx_web_server.pp](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0C-web_server/7-puppet_install_nginx_web_server.pp)**

