import sys
import os

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here

def check_link(link, dir):
    for file in os.listdir(os.fsencode(dir)):
        if os.fsdecode(file).startswith(link):
            return os.fsdecode(file)
    return link[::-1].find(".")

args = sys.argv
if len(args) != 2:
    print("Please give a directory.")
else:
    try:
        os.mkdir(args[1])
    except FileExistsError:
        pass
    dir = args[1]
    while True:
        link = input()
        if link == "exit":
            break
        status = check_link(link, dir)
        if status == -1:
            print("Error: Incorrect URL")
        elif isinstance(status, int):
            filepath = dir + "\\" + link[:status] + ".txt"
            url = open(filepath, "w")
            if link == "bloomberg.com":
                url.write(bloomberg_com)
                print(bloomberg_com)
            elif link == "nytimes.com":
                url.write(nytimes_com)
                print(nytimes_com)
            else:
                print("Error: Incorrect URL")
                # url.write("The link " + link + " exists")
                # print("The link " + link + " exists")
            url.close()
        else:
            url = open((dir + "\\" + status), "r")
            print(url.read())
            url.close()
