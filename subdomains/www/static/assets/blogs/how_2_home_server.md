Unlike [[how_2_cloud]] or [[how_2_static]] I intend to be pretty in depth here. I will be covering specifically how to setup a home server like mine. At times I will point out alternatives to what I use, but I will always provide the exact item I use and why. With that said, lets begin :)

## Why a Home Server?
An important question. Why do all this when I can just use the cloud, is money really the big factor here?

Honestly not really for me. Its a nice benefit that my costs are fixed now compared to monthly in the cloud, but I don't care that much about that. For me its the following
1. Learning
	1. I set it up myself, I understand it better.
	2. I get to learn about things I wouldn't normally expose myself to if I could just use cloud services for all my problems
2. Upgrades
	1. In the cloud scaling is easy in a sense, but certain things like upgrading storage can become cumbersome in the cloud
3. Direct access
	1. I don't have to do everything over SSH.
4. Flexibility
	1. My home server isn't just for my website. I have it connected to my TV to enable streaming games via Steam and streaming things I don't have available on my TV
## Selecting your server

First and foremost you need a computer, truly any computer. An old laptop for example. Ideally something you aren't using so it can stay always on and running. If you just want to dip your toes in you can use your personal computer, but I prefer to keep it separated.

If you don't have an old computer **BUY USED!!!!!** I got my server for $100 on ebay and its amazing value. Some people use things like raspberry pis for home servers, but its not as upgradable. I can buy new ram, CPU, SSDs for my computer with a lot more leeway than something like a raspberry pi.

## Setup Docker
This is technically optional, but really it isn't.

If you want to host multiple things Its genuinely a must, but even if you just have the website containerization is great. It will make your code much easier to debug (replicate bugs more easily) and deploy. Plus its portable, you can work on the code from your personal machine and then push code to git and pull it on the server. A real workflow!

you can see the Dockerfile I use for this website [here](https://github.com/brett-ludwig/dumbfucks-club/blob/main/subdomains/www/Dockerfile)

Set yours up and get your docker deployed locally (you should be able to access the website in the browser via localhost:\<port\> on your server at this point)

## Connect your URL to Cloudflare Nameservers
Before we can setup our tunnels to connect us to the internet we need a URL in cloudflare. You can buy the URL direct in cloudflare and this will be automatic.

If you buy from an external registrar still make a cloudflare account and go to the domains section. From here you can have Cloudflare attempt to scan for your DNS records automatically and connect it to their Nameservers

## Setup Cloudflare Tunnels
So this is secret sauce. A fair question to have about a home server hosting a website is "Hey, isn't that really insecure to open your network like that?". By golly gee you are right!

Especially when you don't know what you're doing this is not smart. People have bots that will try to hack your site no matter how insignificant. For example, here is a German bot that tried to use a React vuln to run code remotely on my server. (My website doesn't even use React, these bots just attempt known vulns blindly on URLs)
![[security-example.png]]

As you can see, I use Cloudflare. Cloudflare is industry standard, has a fantastic free tier, and comes out the box able to block known threats like in the image above.

Additionally it has a service called [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/). These allow you to run the tunnel program on your server **without exposing your public IP address**. Cloudflare acts as a gatekeeper. As shown above it will do some basic security checks and gives you insight into how many requests come to your site and from where.

Using the cloudflare tunnel cli tool on your homeserver connect it to your cloudflare account. This should result in you having a Connector
![[cloudflare_tunnel_1.png]]
Click the 3 dots on your connector and lets add a route that points to your locally hosted application
![[cloudflare_tunnel_2.png]]
Notice how I use localhost for my service destination. At no point do we expose a public IP address. If you run a dig+trace command on dumbfucks.club you'll only get the ip address of cloudflare (and if you get around it please let me know so I can shore up security lol).

This isn't bullet proof security, but it has kept me safe so far (at least as far as I am aware).

## Use your website

At this point you should be live. Have fun!
