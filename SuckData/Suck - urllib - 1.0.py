import urllib.request
import urllib.parse
import re

url = "https://luanmorenodba.com/2012/06/29/gerenciando-projetos-do-ssis-no-ssms-do-sql-server-2012/"
values = {"S":"basics","submit":"search"}

data = urllib.parse.urlencode(values)
data = data.encode("UTF-8")
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)

strdata = response.read()

#print(strdata)

paragraphs = re.findall(r'href="(.*?)">',str(strdata))

for eachP in paragraphs:
   print (eachP)



