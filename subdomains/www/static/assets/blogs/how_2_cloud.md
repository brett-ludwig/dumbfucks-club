
The goal here is not to give you the exact cloud provider/stack you should use. This is more an intro to topics you'll need to be familiar with and links to better resources.

___

# Picking a Cloud Provider

You can go with one of the big 3: AWS, Azure, GCP

Their free tiers aren't as permissive these days, but you'll work with services that can give you real work experience. Even help get muscle memory for certifications.

Oracle has an **insane** free tier, but who knows how long that will last. It also isn't used often in my experience professionally.

Alternatively you can go for more fringe but value options such as:
* Netlify
* Vercel
* Vultr
* PikaPods

Make sure to take advantage of f
# Actual Setup

![[Cloud Hosting.png]]

Above you can see one of the most basic diagrams for how the traffic should flow for your application. **I'll give an example of how I used to host this website in GCP at the bottom of the article**. I keep the architecture vague because your needs may differ from mine.

## Application

Your application can be anything that responds to HTTP requests. Often this is a question of what you want the website able to do and what tools you already know. Some common backend frameworks are...

* Java
	* Spring-Boot
	* tomcat
* Python
	* Django
	* Fast API
* GoLang
	* Gin
	* The base HTTP module is pretty solid
	* Gorilla MUX
* Javascript
	* NodeJs
* Other (These are less useful professionally, but have cool programming ideas or I've heard good things about)
	* Elixir-lang
	* Ruby on Rails

Whatever code runs it, build it locally and get it deployed so that the webserver is responding to requests to its private ip address

## Load Balancer

Your application now runs on something (maybe a lambda or a VM). It has a private ip address though, computers outside the network cannot access it.

You either need a public IP address associated with your application or a load balancer. I show a load balancer because they are better for when you want to add things. You application might initially only be a Virtual Machine, but what if you want to change it in the future? Have a load balancer as a middle man is nice.

Either way you need something with a public IP address (be it the load balancer or the Application's Virtual Machine). At this point people should be able to access your website if they type the public IP address into the URL bar

## Name Server Setup 

If you bought your URL on something like route53 in AWS or a similar service for other cloud providers you get this setup for your. You just need to connect the url in the cloud console

If you bought through an external registrar like namecheap then you need to setup the nameserver on that website to point to your load balancer.

![[dumbfuck-dns.png]]

Here is a legit old photo of my nameserver on namecheap. At the top you see an A record with host @ and value blacked out. That value is the ip address of my. This makes it so

dumbfucks.club -> ip address

Note that this isn't www.dumbfucks.club A Records don't set that up. That is what the CNAME records are for. You can have multiple, but for now just setup the www. so at minimum you need

1 A Record pointing to your load balancer
1 CNAME associating www. with your base url

## Example

![[real-architecture.png]]

Above is how my website was hosted back when I was using GCP. 

I used the free tier Virtual Machine as a load balancer. NGINX was my reverse proxy, basically its making my own load balancer rather than using the actual cloud service.

I used free cloud functions for hosting the HTTP part of my website and a Spot VM for a more resource intensive part of my website that wasn't always on. I have since moved away from this setup since It was overly complicated. 

**If you are going to go cloud I think you should be comfortable with a bill. My setup became complicated because I was trying to play within the lines of the free tier too much. I chose to move to home hosting, but cloud may be the better fit for you**