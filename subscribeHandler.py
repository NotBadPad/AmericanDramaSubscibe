# -*- coding: utf-8 -*-
# coding=utf-8

def getSubscribe():
	conf_file = open('config/subscribe.conf')
	adlist = []
	try:
		lines = conf_file.readlines()
		for x in lines:
			splitValue = x.split(",")
			adInfo = {
				"name":splitValue[0],
				"season":splitValue[1],
				"url":splitValue[2]
			}
			adlist.append(adInfo)
	except Exception, e:
		print e
	finally:
		conf_file.close()
	return adlist


if __name__ == '__main__':
	getSubscribe()