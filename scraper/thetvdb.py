from urllib import quote_plus
import urllib2
import xml.dom.minidom as minidom

SHOW_URL = "http://www.thetvdb.com/api/GetSeries.php?seriesname=%s"

FIELDS = [
    "seriesid",
    "SeriesName",
    "banner",
    "Overview"
]

SHOWS = []

class Show(object):
    
    def __init__(self, (id, name, banner, overview)):
        self.id = id
        self.name = name
        self.banner = banner
        self.overview = overview

    # Is there a way to auto-generate genres?
    def insert(self, key, genre):
        return "insert into tvshows values(%d, %d, %s, %s, '', %s);" % (key, genre, self.name, self.banner, self.overview)



def getText(show, field):
    ns = show.getElementsByTagName(field)
    if len(ns) == 0:
        print "Improper tags for show ", field
        print show
        print field
        raise
    parent = ns[0]
    nodes = parent.childNodes
    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            return node.data

def parseXML(xml):
    doc = minidom.parse(xml)
    node = doc.documentElement
    series = doc.getElementsByTagName("Series")
    if len(series) == 0:
        return
    show = series[0]
    k = tuple([getText(show, f) for f in FIELDS])
    s = Show(k)
    return s

def test(show):
    xml = urllib2.urlopen(SHOW_URL % show)
    doc = minidom.parse(xml)
    node = doc.documentElement
    series = doc.getElementsByTagName("Series")
    print series
    if len(series) == 0:
        return
    show = series[0]
    print show
    for f in FIELDS:
        print getText(show, f)
    k = tuple([getText(show, f) for f in FIELDS])
    s = Show(k)
    print s.name
    return s

def parseFile(fname):
    shows = []
    f = open(fname, 'r')
    for line in f:
        shows.append(quote_plus(line.strip()))
    return shows

if  __name__ == "__main__": 
    shows = parseFile('shows.txt')
    exit
    for show in shows:
        try:
            xml = urllib2.urlopen(SHOW_URL % show)
            SHOWS.append(parseXML(xml))
        except:
            print "==> Problem with ", show
