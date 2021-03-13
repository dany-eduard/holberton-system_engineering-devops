# 0x09. Web infrastructure design

<h2>Resources</h2>

<p><a href="https://youtu.be/lQNEW76KdYg" target="_blank"><img src="https://user-images.githubusercontent.com/54107524/111018557-82032580-8387-11eb-944e-4b670ebf47bb.png" alt="" style="" /></a></p>

<ul>
<li><strong>Network basics</strong> concept page</li>
<li><strong>Server</strong> concept page</li>
<li><strong>Web server</strong> concept page</li>
<li><strong>DNS</strong> concept page</li>
<li><strong>Load balancer</strong> concept page</li>
<li><strong>Monitoring</strong> concept page</li>
<li><a href="https://searchsqlserver.techtarget.com/definition/database" title="What is a database" target="_blank">What is a database</a> </li>
<li><a href="https://www.youtube.com/watch?v=S97eKyv2b9M" title="What&#39;s the difference between a web server and an app server?" target="_blank">What&rsquo;s the difference between a web server and an app server?</a></li>
<li><a href="https://pressable.com/2019/10/11/what-are-dns-records-types-explained-2/" title="DNS record types" target="_blank">DNS record types</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Single_point_of_failure" title="Single point of failure" target="_blank">Single point of failure</a> </li>
<li><a href="https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header" title="How to avoid downtime when deploying new code" target="_blank">How to avoid downtime when deploying new code</a> </li>
<li><a href="https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712" title="High availability cluster (active-active/active-passive)" target="_blank">High availability cluster (active-active/active-passive)</a> </li>
<li><a href="https://www.instantssl.com/http-vs-https" title="What is HTTPS" target="_blank">What is HTTPS</a> </li>
<li><a href="https://www.webopedia.com/definitions/firewall/" title="What is a firewall" target="_blank">What is a firewall</a> </li>
</ul>

<h2 class="center">Tasks</h2>

<div class="panel-heading">
    <h3 class="panel-title">
      0. Simple web stack
    </h3>

<p>On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via <code>www.foobar.com</code>. Start your explanation by having a user wanting to access your website.</p>

<p>Requirements:</p>

<ul>
<li> You must use:

<ul>
<li>1 server</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 application files (your code base)</li>
<li>1 database (MySQL)</li>
<li>1 domain name <code>foobar.com</code> configured with a <code>www</code> record that points to your server IP <code>8.8.8.8</code></li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>What is a server</li>
<li>What is the role of the domain name</li>
<li>What type of DNS record <code>www</code> is in <code>www.foobar.com</code></li>
<li>What is the role of the web server</li>
<li>What is the role of the application server</li>
<li>What is the role of the database</li>
<li>What is the server using to communicate with the computer of the user requesting the website</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>SPOF</li>
<li>Downtime when maintenance needed (like deploying new code web server needs to be restarted)</li>
<li>Cannot scale if too much incoming traffic</li>
</ul></li>
</ul>

  </div>
  
<div>
    <h3 class="panel-title">
      1. Distributed web infrastructure
    </h3>

<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>2 servers</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 load-balancer (HAproxy)</li>
<li>1 set of application files (your code base)</li>
<li>1 database (MySQL)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>For every additional element, why you are adding it</li>
<li>What distribution algorithm your load balancer is configured with and how it works</li>
<li>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</li>
<li>How a database Primary-Replica (Master-Slave) cluster works</li>
<li>What is the difference between the Primary node and the Replica node in regard to the application</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>Where are SPOF</li>
<li>Security issues (no firewall, no HTTPS)</li>
<li>No monitoring</li>
</ul></li>
</ul>

  </div>

<div class="">
    <h3 class="panel-title">
      2. Secured and monitored web infrastructure
    </h3>

<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>3 firewalls </li>
<li>1 SSL certificate to serve <code>www.foobar.com</code> over HTTPS</li>
<li>3 monitoring clients (data collector for Sumologic or other monitoring services)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>For every additional element, why you are adding it</li>
<li>What are firewalls for</li>
<li>Why is the traffic served over HTTPS</li>
<li>What monitoring is used for</li>
<li>How the monitoring tool is collecting data</li>
<li>Explain what to do if you want to monitor your web server QPS</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>Why terminating SSL at the load balancer level is an issue</li>
<li>Why having only one MySQL server capable of accepting writes is an issue</li>
<li>Why having servers with all the same components (database, web server and application server) might be a problem</li>
</ul></li>
</ul>

  </div>
