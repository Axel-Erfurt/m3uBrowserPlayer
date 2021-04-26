#!/usr/bin/python3
# -*- coding: utf-8 -*-

### Credits: https://github.com/video-dev/hls.js/
import sys
import webbrowser

result = []
mytv_list = []
m3u_file = sys.argv[1]
mytv_webfile = "m3uTV.html"
mytv_text = open(m3u_file, 'r').read().splitlines()



for x in range(len(mytv_text)-1):
    line = mytv_text[x]
    nextline = mytv_text[x+1]
    if line.startswith("#EXTINF") and not "********" in line:
        if 'tvg-name="' in line:
            name = line.partition('tvg-name="')[2].partition('"')[0]
        elif 'tvg-name=' in line:
            name = line.partition('tvg-name=')[2].partition(' tvg')[0]
        else:
            name = line.rpartition(',')[2]
        mytv_list.append(f'{name},{nextline}')



def getValues():
    for line in mytv_list:
        textline = line.split(",")
        if len(textline) > 1:
            name = textline[0]
            url = textline[1]
            result.append(f"<li><a class='chlist' href='{url}'>{name}</a></li>") 

        
    return('\n'.join(result))
    

result = getValues()

### html
html_top = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Movie Player</title>
    <script type="text/javascript" src="list.min.js"></script>
    <script type="text/javascript" src="jquery-1.10.1.js"></script>
     <script type="text/javascript" src="hls.js"></script>
    <link rel="stylesheet" href="player.css" media="all">
    <script src="player.js" async></script>
  </head>
  <body>
    <div id="videodiv">
             <video autoplay controls='none' id='myvideo' preload='none' tabindex='0'>
        <source id="primarysrc" src='none' type="application/x-mpegURL"/></video>
        </div>
  <div id="tvlist">
     <input class="customSearch search" type="search" placeholder="suchen ..." />
<br>
<ul id='playlist' class='list'>
"""

html_bottom = """</ul>
    </div>
  </body>
</html>
"""
html_code = html_top
html_code += result
html_code += html_bottom

    
with open(mytv_webfile, 'w', encoding='utf8') as f:
    f.write(html_code)
    f.close()
    
webbrowser.open(mytv_webfile, 2)
