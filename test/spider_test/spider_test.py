# -*- coding: utf-8 -*-
from pyquery import PyQuery as py
import urllib2, os

url_pref = 'http://www.qisuu.com'
html = urllib2.urlopen('http://www.qisuu.com/').read()
jq = py(html)
# f = open('html/qisusu.html','wb')
# f.write(jq.outer_html().encode('utf-8'))
# f.close()
tag_a_obj = jq('.nav')('a')
del tag_a_obj[0]
for tag_a in tag_a_obj:
    if not os.path.exists('data/' + tag_a.text.encode('utf-8')):
        os.makedirs('data/' + tag_a.text.encode('utf-8'))
    url = url_pref + tag_a.get('href')
    jq_child = py(url)
    child_a_obj = jq_child('.dph')('a')
    for child_a in child_a_obj:
        child_url = child_a.get('href')
        target = py(url_pref + child_url)
        download_url = target('.downButton')[1].get('href')
        os.chdir('data/' + tag_a.text.encode('utf-8'))
        os
