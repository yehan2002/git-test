#!/usr/local/bin/python
import os
print ("Content-type: text/html\n\n")
words = ["%s is crazy","%s is bad","%s is a brat","%s is stupid","%s is a dog","%s is unintelligent","%s is screwy","%s is idiotic","%s is dumb","%s is loony"]
wordlist = []
url = os.environ["REQUEST_URI"]
try:
    params = url.split('?')[1]
    params = params.split('&')
    for item in params:
        if "person" in item:
            params = item
            break
except:
    params = "person=sasen"
params = params.replace("person=","")
for item in words:
    wordlist.append(item%(params))
print'''<html >
<head>
  <meta charset="UTF-8">
  <title>stupid.com</title>
     
</head>
<body bgcolor="#FFF0F5">
<svg width="75%" height="500px" style="position: relative;left: 10%; up='10%'">
<g>
<rect x="5" y="5" width="99%" height="98%" style="fill:skyblue;stroke:pink;stroke-width:5;stroke-opacity:0.9"></rect>
<foreignObject x="10" y="10" width="89%" height="74%">
<body>
<marquee behavior="alternate" direction="up" height="444">
<marquee behavior="alternate">
<div style=" color: e6e6fa;"><h1 id="changeText"></h1></div>
<script type="text/javascript">'''
print "var text = %s"%(wordlist)
print '''
    var counter = 1;
    var elem = document.getElementById("changeText");
    elem.innerHTML = text[0]
    setInterval(change, 10000);
    function change() {
     elem.innerHTML = text[counter];
        counter++;
        if(counter >= text.length) { counter = 0; }
    }
</script>
</marquee></marquee>
</body>
</foreignObject>
</g>
  Sorry, your browser does not support inline SVG.  
</svg> 
<div style="text-align:center;">
<form>
Enter name :-<input type="text" name="person">
<input type="submit">
</form>
</body>
</html>'''