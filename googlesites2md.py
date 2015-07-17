#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
USAGE

    googlesites2markdown <file>


DESCRIPTION

    Extract main content from a Google Sites (sites.google.com) page 
    and convert it to Markdown, e.g., for GitHub Wikis. 
    <file> is a file downloaded from Google Pages, e.g., using 
    'wget --mirror --convert-links --adjust-extension 
    --page-requisites --no-parent http://www.somesite.org'

DEPENDENCIES

    pandoc <http://johnmacfarlane.net/pandoc/>
"""
 
import subprocess
import sys
from lxml import html
 
if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h"]:
    print __doc__
    exit(1)

inf = open(sys.argv[1], "r")
htmlstring = inf.read()
inf.close()
tree = html.fromstring(htmlstring)
main = tree.xpath('//tbody')[0]
title = tree.xpath('//span[@id="sites-page-title"]')[0].text_content()
print title
shortstring = "<h1>" + title +"</h1>" + html.tostring(main) 
print shortstring

file_name = title.replace(" ", "_").replace("/", "_")
input_file = "/tmp/{}.html".format(file_name)
output_file = "{}.md".format(file_name)
 
with open(input_file, "w") as input_f:
    input_f.write(shortstring)
 
print "Converting web page…"
pandoc = subprocess.Popen(["pandoc", "--no-wrap",
                           input_file, "--output={}".format(output_file)])
pandoc.wait()

inf = open(output_file, "r")
mdstring = inf.read()
inf.close()

mdstring = mdstring.replace("\\","")
mdstring = mdstring.replace("Â","")
mdstring = mdstring.replace("<div>\n","")
mdstring = mdstring.replace("</div>\n","")
mdstring = mdstring.replace('<div style="text-align:left">',"")
mdstring = mdstring.replace('<div dir="ltr">',"")
mdstring = mdstring.replace('<div style="display:block;text-align:left">',"")
mdstring = mdstring.replace("\n\n","\n")
mdstring = mdstring.replace("\n\n","\n")

with open(output_file, "w") as output_f:
    output_f.write(mdstring)
