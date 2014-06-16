#!/usr/bin/env python

_contacts = {}

with open('contacts.txt') as _f:
	for _i in _f.readlines():
		_line = _i.strip().split()
		_contacts[_line[0]] = _line[1:]

print _contacts.keys()

while True:
	_search = raw_input("Search info:").strip()
	if len(_search) == 0:
		continue
	if _contacts.has_key(_search):
		print _search, _contacts[_search]	
	else:	# start to search the info fuzzy matching mode
		_info_counter = 0
		if len(_search) < 2:
			print "No valid info..."
			continue
		for _name,_value in _contacts.items():	# first layer loop
			if _name.count(_search) != 0:	# If name contains search, print user 
				
				_p = _name.find(_search)# High light search, create index position
				print _name[:_p] + "\033[32;1m%s\033[0m" % _search + _name[_p + len(_search):], '\t'.join(_value)

				_info_counter += 1
				continue		# if first loop cound user, STOP second loop, continue first loop!
			for _i in _value:		# second layer loop
				if _i.count(_search) != 0:
					print _name,'\t'.join(_value)
					_info_counter += 1
		if _info_counter == 0:
			print "No valid record..."
		else:
			print "Found %s records..." % _info_counter
