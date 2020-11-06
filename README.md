# Alex Kyron's Blog Script
Python blog script inspired by Luke Smith's lb (https://github.com/LukeSmithxyz/lb)
# Example
My blog at https://alexkyron.xyz/blog.php runs on this script. Give it a look! The rolling blog page, blog index page, RSS feed and individual blog post pages are all generated/updated by this script. I blog on there by simply SSHing into the VPS and running this script.
## How do I set it up?

1. Change path variables to your equivalent directories as described in comments or create the folders

2. Add <!--ab--> (or change match_string to your own comment) where you want the rolling content inserted
in your rolling blog page, links inserted in the index page, and updates inserted in RSS

3. Modify insert_string in the publish() method to match your markup; by default this is my site's markup and
yours will not match. Also, when it creates a new file, it uses markdown for the heading, which you may not have
on your site. Change markdown to false in the global variables to make it spit out HTML instead.

Edit the RSS settings. Please don't leave my info in there.

4. Copy this script to the root of your site with your blog.php and blog_index.php pages
(can also be HTML if your edited strings have no php in them)

5. Run python3 ab.py -n <name> to create a blog post. It will save a content file in
/blog/blogcontent/<name>.php (with all spaces changed to hyphens, all quotes removed, all lowercase for easy
URLs).

6. When done editing the post, run python3 ab.py -p <name> to publish your post. This will add a section to your
rolling blog and a link to your index, and update your RSS feed automagically.

#  Configuration
Configuring this script is done through editing source code. The paths are all stored in clear variables at the top and 
there are booleans for disabling features.

## Why not just use lb?
This is python, easier to configure and modify to adapt to more complex sites, simpler and serves the same functionality.
It's also cross-platform, with the only dependency being Vim, as opposed to lb being a bash script requiring every GNU 
tool under the sun. If your website server runs on a Windows box, you're out of luck.

lb is an amazing tool and I think Luke Smith had the right idea while making it. As much as I disagree with his politics,
he is very talented. My site simply wasn't a good fit for the script and re-jigging it to do what I wanted proved more 
annoying than just writing a new one, and I figured it's a useful enough tool to keep supporting and make public.
