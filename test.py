#encoding: gb18030
import sys
reload(sys)
sys.setdefaultencoding( "gb18030" )

import urllib2
import urllib

url="http://weiban.mycourse.cn/pharos/usercourse/finish.do"

import xlrd
import xlwt
from datetime import date,datetime

workbook=xlrd.open_workbook('c.xls')
sheet_name=workbook.sheet_names()[1]
sheet=workbook.sheet_by_index(0)
for i in range(0,288):
	search=urllib.urlencode([
	#('birthday',sheet.cell(i,0).value),
	('tenantCode','61000007'),
	('userCourseId',sheet.cell(i,0).value)
	])
	req=urllib2.Request(url)
	fd=urllib2.urlopen(req,search).read()
	html=fd.decode('gb18030').encode('utf-8')