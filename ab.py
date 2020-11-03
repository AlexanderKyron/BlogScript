import sys, getopt, subprocess, pdb
from os import path
import os
match_string = "<!--ab-->"

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
        elif opt in ('e','--edit'):
            filename = fname(arg)
            os.system("vim ./blog/blogcontent/"+filename+".content.php")


def help():
    print(
        'Alex Kyron\'s Blogging script. \nNew Post\tab -n (--new) <name>\nEdit post\tab -e (--edit) <name>\nPublish post\tab -p <name>\n')
def new_post(arg):
    name = arg;
    filename = fname(name)
    f = open("./blog/blogcontent/" + filename + ".content.php", "w")
    f.write("## " + name)
    f.close()
    os.system("vim ./blog/blogcontent/"+filename+".content.php")
def publish(arg):
    name = arg;
    filename = fname(name)
    if path.exists("./blog/blogcontent/" + filename + ".content.php"):
        f = open("./blog/" + filename + ".php", "w");
        f.write(
            "<?php include('blogheader.php);\ninclude('./blogcontent/" + filename + ".content.php');\ninclude('blogfooter.php');?>")
        f.close();
        insert_string = """
                        <div id='left-content'>
                            <div class='entry'>
                                <div id = 'content'>
<?php include './blog/blogcontent/""" + filename + """.content.php';?>
                                    <br>
                                    <small>
                                    <?php
                                        $filename = './blog/""" + filename + """.php';
                                        if(file_exists($filename)) {
                                            echo date("F d Y H:i:s.", filectime($filename));
                                        }
                                    ?>
                                    </small>
                                </div>
                            </div>
                        </div>
                        """
        with open("./blog.php", 'r+') as fd:
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
            insert_string = """
                                                <li>
                                                        <?php
                                                            $filename = './blog/""" + filename + """.php';
                                                            if(file_exists($filename)) {
                                                                echo date("F d Y H:i:s.", filectime($filename));
                                                            }
                                                        ?>&ndash; <a href="blog/""" + filename + """.php">""" + name + """</a></li>
                                            """
        with open("./blog_index.php", 'r+') as fd:
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
    else:
        print("The blog post you are attempting to publish does not exist.")
        exit();

def fname(name):
    return name.replace(' ', '-').replace('\'','').replace('"','').lower()


if __name__ == "__main__":
    main(sys.argv[1:])
