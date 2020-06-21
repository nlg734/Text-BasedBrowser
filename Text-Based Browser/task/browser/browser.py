import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

init()


def check_link(webpage, fold):
    for file in os.listdir(os.fsencode(fold)):
        if os.fsdecode(file).startswith(webpage):
            return os.fsdecode(file)
    return webpage[::-1].find(".")


def remove_tags(text):
    parsed_text = []
    soup = BeautifulSoup(text, "html.parser")
    tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title']
    tagged = soup.find_all(tags)
    for tag in tagged:
        if tag.name == "a":
            parsed_text.append("<a>" + tag.get_text() + "\n")
        else:
            parsed_text.append(tag.get_text() + "\n")
    return parsed_text



def main(folder):
    history = []
    while True:
        link = input()
        if link == "exit":
            break
        if link == "back":
            if len(history) == 0:
                continue
            history.pop()
            with open(history.pop()) as url:
                print(url.read())
                continue
        status = check_link(link, folder)
        if status == -1:
            print("Error: Incorrect URL")
        elif isinstance(status, int):
            filepath = folder + "\\" + link[:status] + ".txt"
            url = open(filepath, "w")
            if link.lower().startswith("http"):
                page = requests.get(link)
            else:
                page = requests.get("https://" + link)
            for line in remove_tags(page.text):
                if "<a>" in line:
                    url.write(line)
                    line = line.strip("<a>")
                    print(Fore.BLUE + line)
                else:
                    url.write(line)
                    print(line)
            history.append(filepath)
            url.close()
        else:
            filepath = folder + "\\" + status + ".txt"
            url = open(filepath, "r")
            for line in url:
                if "<a>" in line:
                    line = line.strip("<a>")
                    print(Fore.BLUE + line)
                else:
                    print(line)
            url.close()
            history.append(filepath)


args = sys.argv
if len(args) != 2:
    print("Please give a directory.")
else:
    try:
        os.mkdir(args[1])
    except FileExistsError:
        pass
    main(args[1])
