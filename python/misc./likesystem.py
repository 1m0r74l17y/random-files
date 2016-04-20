import urllib2
productionId = raw_input("what is the productionId?     ")

if productionId == "nilq":
    productionId = "15602"
likecount = input("How many likes do you want?")
for i in range(likecount):
    response = urllib2.urlopen('http://filmlinjen.dk/umbraco/surface/ProductionsSurface/IncrementLikes?productionId=' + productionId +  '&timestamp=635962278782832032')
    #html = response.read()
    #print str(i+1) + ' : ' + html
