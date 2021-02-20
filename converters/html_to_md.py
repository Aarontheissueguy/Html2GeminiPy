import os
from os import walk
import os.path
from markdownify import markdownify

def convert_html_to_md(HtmlList):
    for path in HtmlList:

        pathsplit = path.split("/")

        file = open(str(path), "r").read()
        html = markdownify(file, heading_style="ATX")
        f = open("output/markdown/" + str(pathsplit[-1]).replace(".html", ".md"), "w")
        f.write(html)
        f.close()



    return "html was converted to markdown (1/3)"
