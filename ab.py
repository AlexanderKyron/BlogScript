##############################
#  Alex Kyron's Blog Script  #
#  11/3/2020                 #
#  ver. 1.1                  #
#  License: MIT              #
#  github.com/AlexanderKyron #
##############################
#   How to Use
#
#       1. Change path variables to your equivalent directories as described in comments or create the folders
#
#       2. Add <!--ab--> (or change match_string to your own comment) where you want the rolling content inserted
#       in your rolling blog page, links inserted in the index page, and updates inserted in RSS
#
#       3. Modify insert_string in the publish() method to match your markup; by default this is my site's markup and
#       yours will not match. Also, when it creates a new file, it uses markdown for the heading, which you may not have
#       on your site. Change markdown to false in the global variables to make it spit out HTML instead.
#
#       Edit the RSS settings. Please don't leave my info in there.
#
#       4. Copy this script to the root of your site with your blog.php and blog_index.php pages
#       (can also be HTML if your edited strings have no php in them)
#
#       5. Run python3 ab.py -n <name> to create a blog post. It will save a content file in
#       /blog/blogcontent/<name>.php (with all spaces changed to hyphens, all quotes removed, all lowercase for easy
#       URLs).
#
#       6. When done editing the post, run python3 ab.py -p <name> to publish your post. This will add a section to your
#       rolling blog and a link to your index, and update your RSS feed automagically.

import getopt
import os
import sys
from os import path

# GENERAL VARS
# String to look for in files to insert the markup on the line after
match_string = "<!--ab-->"
# Relative path to folder where finished blog pages are stored, relative to root
blog_path = "./blog"
# Absolute path to folder where finished blog pages are stored
blog_absolute_path = "/blog"
# Relative path to blog content folder
blogcontent_path = "./blog/blogcontent"
# Path to blog content folder, relative to blog folder
blogcontent_path_rel = "./blogcontent"
# Relative path to blog index page
blog_index_page = "./blog_index.php"
# Relative path to rolling blog page
blog_rolling_page = "./blog.php"

# POST SETTINGS
markdown = True

# RSS SETTINGS
# base URL to append specific page links to, please don't leave my url here
url = "https://alexkyron.xyz/blog"
# author of posts, please don't leave my email here when you set this up for your site
author = "alex@alexkyron.xyz"
# path to RSS file
rss_path = "./rss.xml"

# PUBLISHING SETTINGS
rolling_blog_enabled = True
blog_index_enabled = True
rss_enabled = True


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:e:p:")
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit(0)
        elif opt in ("-n", "--new"):
            new_post(arg)
        elif opt in ("-p", "--publish"):
            publish(arg)
        elif opt in ('e', '--edit'):
            filename = fname(arg)
            os.system(f"vim {blogcontent_path}/{filename}.content.php")


def help():
    print(
        'Alex Kyron\'s Blogging script. \nNew Post\tab -n (--new) <name>\nEdit post\tab -e (--edit) <name>\nPublish '
        'post\tab -p <name>\n')


def new_post(arg):
    name = arg;
    filename = fname(name)
    f = open(f"{blogcontent_path}/{filename}.content.php", "w")
    if markdown:
        f.write(f"## [{name}]({blog_absolute_path}/{filename}.php)\n")
    else:
        f.write(f'<a href="{blog_absolute_path}/{filename}.php"><h2>{name}</h2></a>\n')
    f.close()
    os.system(f"vim {blogcontent_path}/{filename}content.php")


def publish(arg):
    name = arg;
    filename = fname(name)
    if path.exists(f"{blogcontent_path}/{filename}.content.php"):
        f = open(f"{blog_path}/{filename}.php", "w");
        # Post standalone page. Edit this for your site, or keep the template here.
        f.write(
            f"<?php include('blogheader.php');\ninclude('{blogcontent_path_rel}/{filename}.content.php');\ninclude('blogfooter.php');?>")
        f.close();
        # Blog markup insert. Edit this for your site.
        if rolling_blog_enabled:
            insert_string = f"""
                            <div id='left-content'>
                                <div class='entry'>
                                    <div id = 'content'>
<?php include '{blogcontent_path}/{filename}.content.php';?>
                                        <br>
                                        <small>
                                        <?php
                                            $filename = '""" + blog_path + filename + """.php';
                                            if(file_exists($filename)) {
                                                echo date("F d Y H:i:s.", filectime($filename));
                                            }
                                        ?>
                                        </small>
                                    </div>
                                </div>
                            </div>
                            """
            with open(blog_rolling_page, 'r+') as fd:
                contents = fd.readlines()
                if match_string in contents[-1]:
                    contents.append(insert_string)
                else:
                    for index, line in enumerate(contents):
                        if match_string in line and insert_string not in contents[index + 1]:
                            contents.insert(index + 1, insert_string)
                            break
                fd.seek(0)
                fd.writelines(contents)
            # Blog index link markup. Edit this for your site, or keep what's here.
        if blog_index_enabled:
            insert_string = """
                                                    <li>
                                                            <?php
                                                                $filename = '""" + blog_path + "/" + filename + """.php';
                                                                if(file_exists($filename)) {
                                                                    echo date("F d Y H:i:s.", filectime($filename));
                                                                }
                                                            ?>
                                                            &ndash; <a href=\"""" + blog_absolute_path + "/" + filename + """.php">""" + name + """</a>
                                                    </li>
                                                """
            with open(blog_index_page, 'r+') as fd:
                contents = fd.readlines()
                if match_string in contents[-1]:
                    contents.append(insert_string)
                else:
                    for index, line in enumerate(contents):
                        if match_string in line and insert_string not in contents[index + 1]:
                            contents.insert(index + 1, insert_string)
                            break
                fd.seek(0)
                fd.writelines(contents)
        if rss_enabled:
            rss_description = input("Enter the description for the RSS entry: ")
            rss_string = f"""
            <item>
                <title>{name}</title>
                <link>{url}/{fname}.php</link>
                <description>{rss_description}</description>
                <author>{author}</author>
            </item>
                """

            with open(rss_path, 'r+') as fd:
                contents = fd.readlines()
                if match_string in contents[-1]:
                    contents.append(rss_string)
                else:
                    for index, line in enumerate(contents):
                        if match_string in line and rss_string not in contents[index + 1]:
                            contents.insert(index + 1, rss_string)
                            break
                fd.seek(0)
                fd.writelines(contents)
    else:
        print("The blog post you are attempting to publish does not exist.")
        exit()


def fname(name):
    return name.replace(' ', '-').replace('\'', '').replace('"', '').lower()


if __name__ == "__main__":
    main(sys.argv[1:])
