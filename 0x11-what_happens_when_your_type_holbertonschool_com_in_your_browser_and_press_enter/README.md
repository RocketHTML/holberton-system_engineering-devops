# 5 Things To Know About The Fullstack

Here's five basics every developer should know, as they developing those amazing, scalable web applications.

## 1. IP Address
Every device connected to the internet is identified by a unique IP address. One computer communicates with another by sending data in segments, known as frames, and attaching the IP address to the header of each frame. The receiving computer can then respond the sender by simply swapping the source and destination addresses.

![dataframe](https://github.com/RocketHTML/holberton-system_engineering-devops/blob/master/0x11-what_happens_when_your_type_holbertonschool_com_in_your_browser_and_press_enter/gifs/tcp_ip.gif)

A port number, segment number, and content block, are together known as a TCP Segment. So when you loaded this page, the blog, the gifs, and text, were all sent to your computer in segments, and then re-membered for your viewing pleasure, in a few milliseconds.

## 2. Internet
In order for you to have found this blog, your browser needed to find this server's IP address. So when you typed up the domain URL and pressed enter, your computer made a request to the world's public registry, in search for an IP address paired with that domain. 

This server's IP address is kept together with a domain name, on dedicated computers known as name servers. When your request located a name server, the name server responded with an IP address, and then your computer was able to find and recieve this blog on its own.

![dns lookup](https://github.com/RocketHTML/holberton-system_engineering-devops/blob/master/0x11-what_happens_when_your_type_holbertonschool_com_in_your_browser_and_press_enter/gifs/dns_lookup.gif)

After visiting this site once, your browser cached the IP address of the server, to save time on subsequent visits.

## 3. Load Balancer
This server is actually a proxy server, between you and the backend server that fulfilled your request.

The proxy server distributes the requests it recieves among multiple backend servers, because one server alone can only serve so many visitors at a time.

![proxy](https://github.com/RocketHTML/holberton-system_engineering-devops/blob/master/0x11-what_happens_when_your_type_holbertonschool_com_in_your_browser_and_press_enter/gifs/load_balance_V2.gif)

Funneling traffic through a proxy server lets us centralize our focus on security to the proxy, and then we simply cut off all direct communication between the outside world and our backend servers. 

So when you see the little green lock in your browser's URL bar for example, it's because the proxy server you're communicating with has SSL or TLS installed, so things like passwords can be encrypted before being sent to and from the proxy, thwarting someone who would intercept those frames from being able to read them.

## 4. Backend Server
If the proxy decides that your request is okay, then it forwards it to one of the backend servers. 

It's the backend servers' job to respond to the proxy with the requested content. To do this, each backend server consists of various internal virtual servers, which each handle some aspect of the request. 

a. The virtual web-server recieves the request first and decides what to do. If your request is for static files, like html, JavaScript, and CSS, then it'll return that data to the proxy in chunks, which will return it to you in chunks. 

b. The web-server will forward requests for dynamic content to the virtual application-server. For example, if the website shows your name and gravitar when you're logged in, then it's because the virtual application server altered the html file to have your name included on the page dynamically.

c. The virtual database-server will store data when it is required to. If you press "publish" on some forum websites, then your post will be sent in chunks to the proxy, and then to a backend server, making it's way from the web server, to the app server, and finally into the database. Likewise, when you make a request to view that post again later, the app server will retrieve it from the database, and send it to the web server, which sends it back to the proxy. 

(Backend servers are typically clones of each other, but some resources are unnecessary to clone many times. Databases for example have only a few clones as backup, and they stay in sync by sending messages to one another.)

![servers](https://github.com/RocketHTML/holberton-system_engineering-devops/blob/master/0x11-what_happens_when_your_type_holbertonschool_com_in_your_browser_and_press_enter/gifs/server_inside.gif)

## 5. Firewall
A firewall is a set of instructions we give to our computers, so that they treat different requests differently. We want to control how different requests are handled.

For example, if we only want secure https traffic on our website, then we'll instruct our proxy server to respond to an http request by redirecting it into an https request. 

Or if we want to ensure that our backend servers only respond to requests that have been channeled through the proxy, then we will instruct them to deny requests that come from any other IP address. Doing so will cause them to respond with a rejection message, rather than by fulfilling the request.

![firewall](https://github.com/RocketHTML/holberton-system_engineering-devops/blob/master/0x11-what_happens_when_your_type_holbertonschool_com_in_your_browser_and_press_enter/gifs/firewall_V3.gif)

In conclusion, when you type a URL into the browser and press enter, your computer begins to send and receive data frames, packets, to and from a target IP address. 

In the commercial world, that target IP address is usually a proxy server which will deliver the request to a backend server.

The backend server will process it and respond to the proxy, which which will respond to your computer, which will pieces it together and presents it to you. All in the blink of an eye.

## References

[How DNS Works](https://howdns.works/)

[Directory Service](https://en.wikIPedia.org/wiki/Directory_service)

[How nginx processes a request](http://nginx.org/en/docs/http/request_processing.html)

[How to Secure HAProxy with Let's Encrypt on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04)

[HTTP Basics](http://www.ntu.edu.sg/home/ehchua/programming/webprogramming/http_basics.html)

[How to set up a Firewall with UFW on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-16-04)

[CompTIA Network+ Certification - License to Tech: OSI and TCP/IP Model](https://www.youtube.com/watch?v=1uArp_bSvmA)

[Finger Pointer Icons by Mobiletuxedo](https://www.flaticon.com/authors/mobiletuxedo) 