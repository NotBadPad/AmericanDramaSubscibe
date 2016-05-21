# -*- coding: utf-8 -*-
# coding=utf-8

import subscribeHandler as sub
import urllib2

def carwl():
	adList = sub.getSubscribe()
	for adInfo in adList:
		
		print adInfo


if __name__ == '__main__':
	carwl()