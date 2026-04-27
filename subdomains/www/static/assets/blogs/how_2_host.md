This page is an entry into hosting a site, but by no means the pinnacle of design.

I have tried to do this write up a few times, but it often becomes a mess due to me trying to fit too many thoughts on the page. The problem is fit. Like in most situations, one size does not fit all and in an effort to give the different shoe sizes I lose the overall message. To keep this a bit more controlled this first document is arranged to show...

1. What is universal to all website hosting options
2. The options available for hosting
3. Links to more detailed documents on how to make a website based on each category

___

# What is universal to all website hosting options?
Whether you want to make it all from scratch or use a website builder, its probably helpful (or at least interesting) to understand what it takes to host a website. Below is a minimal set of items you would need

1. Having a URL
2. Having a URL that is properly setup in a DNS for routing HTTP requests
3. Having a backend server to respond to requests
4. Having the webpage content (html/css/js)

**Please read the full document before getting any of these. Once you know which hosting option you want then get them to avoid unncessary steps. For example, buying a URL from a registrar and then realizing later realizing it would have been easier to use a different one for your setup**

## URLs
Your URL is your address for the website. Technically you can use your exposed ip address, but that's psychotic.

## Nameservers
Some of the more technical among you might recognize this as the NS part of DNS. For those of you with a social life, DNS (Domain Name System) is what lets computers figure out the underlying ip address from a URL.

Some of the options we'll discuss set this up for you, others don't.

## Backend Server
All website need a backend. At the most simple you can use website builder to completely ignore setting one up yourself. At the most complex you can have the backend server be a program running on your water-cooled server rack. At the end of the day it just has to respond to HTTP

## Webpage Code
This is the real meat and potatoes. This is what people actually see when they get to your webpage. Web development is not like programming in a traditional sense, but there is a skill to making a website looks nice. That skill is something I do not have. Don't expect any tips about making things look nice in this tutorial, I'd lead you astray.

___


# What are the website hosting options?
Before selecting your website building options you should consider 3 topics
1. What content will this website have
2. How technical do I want to get
3. Cost

For content, the simplest you can have is a static site (just html/css/client-side js). As you need more interaction (blogs, comments, e-commerce, etc) you'll need to pay for tooling or setup the backend yourself so you can setup these more complex features.

How technical you want to get is important. I'm someone who finds hosting fun and interesting. I like the learning opportunities it provides me, but I spend a lot of time doing things that have nothing to do with the **content** of my site. Even if you can tackle the more technical hosting options do consider if you care enough to keep up with the maintenance.

Lastly, there is the consideration of money, the green, the cheddar cheese! Frankly, the only free options are limited and will have a non-custom URL. All the other options have variable cost you can tune to your needs. I recommend thinking about the effort you want to put in first. Somethings are worth the money to save your time.

| Hosting Option            | Content Type(s)                                       | How Technical is it? | Cost                                  |
| ------------------------- | ----------------------------------------------------- | -------------------: | ------------------------------------- |
| Site Builders             | Static and Dynamic (Dynamic acontent limited options) |             Not Very | Monthly Fee                           |
| Github Pages or Neocities | Static Only                                           |           Low/Medium | Free                                  |
| Cloud hosting             | All content                                           |          Medium/High | Variable Monthly Bill                 |
| Home Server               | All content                                           |                 High | Depends on how much you want to spend |
___
# The Deep Dives!

1. Site Builders
	1. I'm not making a blog about this. I haven't used once since I was in middle-school so what do I know.
2. [[how_2_static]]
3. [[how_2_cloud]]
4. [[how_2_home_server]]
