# Alex Kyron's Blog Script
Python blog script inspired by Luke Smith's lb (https://github.com/LukeSmithxyz/lb)
## Why not just use lb?
Well, a few reasons.

1. I didn't find it particularly elegant to go through and modify.

My website has some specific needs with how I format the blog pages, especially with the rolling blog page; this is because it has a consistent theme in which entries are separated into boxes.
The way the site works uses a lot of PHP includes and a decent amount of extra markup on blog insertion. It also uses markdown for formatting blogs. For these reasons, rather than try to modify his bash script, I decided to write a much simpler program.

It also makes it more helpful for people trying to set up their own blogs; if your site supports PHP as mine does, then all you have to do to make this script fit perfectly is adjust the markup in the insert_text variables.

Rather than mess about with lb, I found it easier to just write myself an alternative that is custom fit to the way my site works.


2. I don't like Luke Smith.

This is really petty, but hopefully understandable. I enjoy his content and a lot of his philosophy, however, I cannot get behind reactionary politics, and it feels awkward to use his script and shout him out on my website for it. It'd feel wrong to use his tools and not give credit, and it also feels wrong to associate myself with his name.


3. I like Python better than shell scripting for this stuff.

While bash is certainly fully capable for what this does, lb feels like it's doing a lot more than it needs to, and reading its source feels awkward as it is calling upon so many different tools. While it's efficient and understandable to do so, this just felt more fitting to the task.


4. I wanted to.

I don't have ANY of my python projects on my Github, so it seemed like a good opportunity just to get something done and throw it up on here.
## How do I set it up?
1. Place the script in the root of your website.
2. Make files blog.php, blog_index.php and populate them with all your page boilerplate and whatnot, then include the comment <!--ab--> where the inserted content should go upon publishing a page
3. Make a /blog and a /blog/blogcontent directory
4. Run the script with -n to create a blog post, then -p to publish it
5. ???
6. Profit
