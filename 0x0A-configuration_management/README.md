# 0x0A Configuration management

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management" title="Intro to Configuration Management" target="_blank">Intro to Configuration Management</a> </li>
<li><a href="https://puppet.com/docs/puppet/3.8/types/file.html" title="Puppet resource type: file" target="_blank">Puppet resource type: file</a> (<em>check &ldquo;Resource types&rdquo; for all manifest types in the left menu</em>)</li>
<li><a href="https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/" title="Puppet&#39;s Declarative Language: Modeling Instead of Scripting" target="_blank">Puppet&rsquo;s Declarative Language: Modeling Instead of Scripting</a></li>
<li><a href="http://puppet-lint.com/" title="Puppet lint" target="_blank">Puppet lint</a> </li>
<li><a href="https://github.com/voxpupuli/puppet-mode" title="Puppet emacs mode" target="_blank">Puppet emacs mode</a> </li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your Puppet manifests must pass <code>puppet-lint</code> version 2.1.1 without any errors</li>
<li>Your Puppet manifests must run without error</li>
<li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
<li>Your Puppet manifests files must end with the extension <code>.pp</code> </li>
</ul>

<h3>Install <code>puppet-lint</code></h3>

<pre><code>$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
</code></pre>


## Tasks

### 0. Create a file
Using Puppet, create a file in `/tmp`.

Requirements:

- File path is `/tmp/holberton`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`
- File: **[0-create_a_file.pp](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0A-configuration_management/0-create_a_file.pp)**

_*Example:*_

```sh
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.1.1
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[holberton]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/holberton
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/holberton
root@6712bef7a528:~# cat /tmp/holberton
I love Puppetroot@6712bef7a528:~#
```

---
### 1. Install a package
Using Puppet, install `puppet-lint`.

Requirements:

- Install `puppet-lint`
- Version must be 2.1.1
- File: **[1-install_a_package.pp](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0A-configuration_management/1-install_a_package.pp)**

_*Example:*_

```sh
root@d391259bf577:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.10 seconds
Notice: /Stage[main]/Main/Package[puppet-lint]/ensure: created
Notice: Finished catalog run in 2.83 seconds
root@d391259bf577:/# gem list

*** LOCAL GEMS ***

puppet-lint (2.1.1)
root@d391259bf577:/#
```

---
### 2. Execute a command
Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

- Must use the `exec` Puppet resource
- Must use `pkill`
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0A-configuration_management/)**

_*Example:*_

Terminal #0 - starting my process

```sh
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```

Terminal #1 - executing my manifest

```sh
oot@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 
```
Terminal #0 - process has been terminated

```sh
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```

---


⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
