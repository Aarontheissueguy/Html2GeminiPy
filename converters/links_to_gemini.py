import os
from os import walk
import os.path

def convert_links_to_gemini(domain):

    for file in os.listdir("output/gemini"):
        processed = ""
        f = open("output/gemini/" + file, "r")
        for line in f.readlines():
            if ".html" in line and "http" not in line or domain in line:
                line = line.replace("html", "gmi")
                url = line.split(" ")[1]
                
                link = url.split("/")[-1]

                line = line.replace(str(url), str(link))

                processed += line

            else:
                processed += line
        f.close()
        f = open("output/gemini/" + file, "w")
        f.write(processed)
        f.close()

    return("links are converted to gemini (3/3)")
