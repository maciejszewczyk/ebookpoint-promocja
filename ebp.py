#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import minidom

def downloadXML():
	import urllib

	XML_URL = 'http://ebookpoint.pl/plugins/new/xml/lista.cgi'
	dlFile = 'ebookpoint_ebooks.xml'

	opener = urllib.FancyURLopener()
	try:
		f = opener.open(XML_URL)
	except IOError:
		print 'Failed to open "%s"' % XML_URL
	else:
		print 'Downloading XML from %s' % XML_URL
		outputFile = open(dlFile, "wb")
		while True:
			data = f.read(8192)
			if not data:
				print 'Done'
				break
			print('.'),
			outputFile.write(data)
		f.close( )
		outputFile.close( )

def makeCSV():
	print 'Processing XML'
	input_file = open('ebookpoint_ebooks.xml')
	output_file = open('tmp_ebookpoint_ebooks.xml','w')
	#reDict = {'quot;': '', '"WAJLORD" ': '', ',#197;': 'A', ',#229;': 'a', '&': 'and', 'amp;': 'and', '#8211;': '-', '#8210;': '', '#8221;':'', '#8222;': ''}
	reDict = {';': '', '&': '', '"WAJLORD" ': ''}
	fo = input_file.read( )
	for k, v in reDict.items():
		fo = fo.replace(k,v)
	output_file.write(fo)
	output_file.close()

	xmldoc = minidom.parse('tmp_ebookpoint_ebooks.xml')
	dNodes = xmldoc.firstChild

	parent = dNodes.getElementsByTagName("item")
	csvFile = open('ebookpoint_ebooks.csv','w')
	#import codecs
	#csvFile = codecs.open('plik.csv', encoding='windows-1250', mode='w')

	header = u'Autor;Tytuł;Cena;Cena detaliczna;Zniżka;Oszczędzasz\n'
	header = header.encode('windows-1250')
	csvFile.write(header)
	
	for element in parent:
		typ = element.getAttribute('typ')
		status = element.getAttribute('status')
		if typ == '2' and status == '1': # typ: ebook i status: dostpepny
			discount = element.getAttribute('znizka')
			if discount != '0': # ebooki tylko ze znizka
				#author = element.getAttribute('autor')
				author = element.getAttribute('autor').encode('windows-1250', 'ignore')
				title = element.getAttribute('tytul').encode('windows-1250')
				bargain = element.getAttribute('cena').encode('windows-1250')
				price = element.getAttribute('cenadetaliczna')
				yousave = str(round(float(price),2)-round(float(bargain),2))
				if author == '':
					author = 'Praca zbiorowa'
				csvFile.write(author+';')
				csvFile.write(title+';')
				csvFile.write(bargain.replace('.', ',')+';')
				csvFile.write(price.replace('.', ',')+';')
				csvFile.write(discount+'%;')
				csvFile.write(yousave.replace('.', ',')+'\n')
	csvFile.close()
	print 'Done'

if __name__ == "__main__":
	downloadXML()
	makeCSV()