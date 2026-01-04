
TL;DR
Javascript frameworks paint with a large brush. Often they provide way more features than you really need for your solution and introduce problems (namely that you have to program in JS). There are good JS tools, but in general I think its overrated. It has its uses though

___

When I first started programming I always liked HTML. You could literally write text in a file and rename it with .html and with no syntax that was a valid file that would open in browser. Blew my mind. I really went bonkers when I discovered html and could make things look nicer.

Obviously you can still do that, but now all the cool kids use JavaScript frameworks. Frankly, why shouldn't they? I mean, these frameworks let me reuse my html as components, make updates to my page without refreshing, and manage user state/session! 
1. HTML Re-Use
	1. easily the worst reason to use a JS Framework. server side templating can be done in any language, even the dreaded PHP. Yes there are JS libraries that let you do HTML re-use with server side rendering, but that doesn't count as a reason to use a JS framework because you created the problem to begin with by using a JS framework over templating!
2. Update to pages without refresh
	1. Look I get it. Refreshing the page is ugly, and even in small projects you might want some dynamic updates. There are other ways to do this, for example long before React and its ilk we had AJAX. AJAX nowadays would be pretty hardcore, I'm a fan of HTMX. obviously these are all JS options because JavaScript is the **correct** solution for this. JavaScript frameworks on the other hand are heavy handed if what your doing can be done in a small JS file
3. Manage State/Session
	1. Managing session can be done server side, and plenty of libraries in real programming languages have that built in and well maintained. With session tied to the user via things like Headers you can associate state in the backend if you really need. If you can do it in the backend why bother using a horrible language like JavaScript
 
There are obviously cases where using a big JS library make sense, its just a terrible default tool in most situations. If you think my above examples are terrible strawman arguments feel free to message me.

Static sites are king, JavaScript is flavoring that should be used sparingly. JavaScript is also a horrible language to work with.
