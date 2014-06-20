#!/usr/bin/env python

#import PrettyTable
import itertools

_contacts = {}

with open('contacts.txt') as _f:
	for _i in _f.readlines():
		_line = _i.strip().split()
		_contacts[_line[0]] = _line[1:]

print _contacts.keys()

while True:
	search = raw_input("Search info:").strip()
	if len(search) == 0:
		continue
	if search == 'q':
		break
	if _contacts.has_key(search):	# start precise query
		print search, _contacts[search]	
	else:							# start fuzzy query
		info_counter = 0
		if len(search) < 2:
			print "No valid info..."
			continue
		for name,value in _contacts.items():	# first layer loop
			if name.count(search) != 0:		# If name contains search, print user 
				
				p = name.find(search)		# High light search, create index position
				print name[:p] + "\033[32;1m%s\033[0m" % search + name[p + len(search):] + '\t', '\t'.join(value)

				info_counter += 1
				continue		# if first loop cound user, STOP second loop, continue first loop!
			for i in value:		# second layer loop
				if i.count(search) != 0:
					line = name + '\t' + '\t'.join(value)	# find 'value' contains 'search', generate origin output
					lineSplit = line.split(search)			# we need highlight 'search', so we split the whole output
					#print lineSplit
					lineMeger = []				# create temp sequence
					for j in lineSplit:			# loop adding each part to the temp sequence
						#j = j.strip('\n')
						lineMeger.append(j)		# adding each part to temp sequence
						lineMeger.append("\033[32;1m%s\033[0m" % search)	# adding highlight part
					lineMeger.pop()				# removing the highlight at end of the temp sequence
					#print lineMeger
					lineFin = "".join(itertools.chain(*lineMeger))			# meger the sequence to a complete string
					print lineFin

					info_counter += 1
					break
		if info_counter == 0:
			print "No valid record..."
		else:
			print "Found %s records..." % info_counter
