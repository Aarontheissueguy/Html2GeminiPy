import os
from os import walk
import os.path
from md2gemini import md2gemini

def convert_md_to_gemini():
    for file in os.listdir("output/markdown"):
        with open("output/markdown/" + str(file), "r") as f:
            gemini = md2gemini(f.read())
            f.close()

        f = open("output/gemini/" + str(file).replace(".md", ".gmi"), "w")
        f.write(gemini)
        f.close()
    for file in os.listdir("output/gemini"):
        processed = ""
        f = open("output/gemini/" + file, "r")
        for line in f.readlines():
            if line == "html\n":
                pass

            else:
                processed += line
        f.close()
        f = open("output/gemini/" + file, "w")
        f.write(processed)
        f.close()
    return "markdown was converted to gemini (2/3)"
