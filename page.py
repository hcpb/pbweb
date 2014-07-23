#!/usr/bin/env python
 
import cgi
import os, random

form = cgi.FieldStorage()
 
dur = form.getvalue('duration')
if dur == None: dur = '10'
tempdur = dur
lastnew = form.getvalue('lastnew')

# pick a random file from the display directory...
files = os.listdir('images')
files.sort()
bg = files[random.randint(0,len(files)-1)]

# display the newest file, if there is a new one...
if lastnew == None:
    lastnew = files[-1]
else:
    if not(lastnew == files[-1]):
            bg = files[-1]
            lastnew = bg
            tempdur = 25

print """Content-type: text/html


<html>
<head>
<title>Test URL Encoding</title>
<meta name="mobile-web-app-capable" content="yes">
<META http-equiv="refresh" content="{};URL=page.py?duration={};lastnew={}">""".format(tempdur, dur, lastnew)

print '''<style>
  body {height:100%; overflow-y:hidden;}

  .with-bg-size
  {'''
print '''    background-image: url('http://10.81.16.110:8000/images/{}');'''.format(bg)
print '''    width: 100%;
    height: 100%;
    background-position: center;
    background-size: cover;
  }
</style>

</head>
<body>'''

print """
<div class="with-bg-size" style="position:fixed; top:0px; left:0px; z-index:900;
width:100%; overflow-y:hidden; overflow-x:hidden; margin:auto;"></div>
</body>
</html>""".format(bg)

