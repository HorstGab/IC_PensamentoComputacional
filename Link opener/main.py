import sys
import os
import re

file_links_to_open = open('links.txt', 'r');

def main():

	for line in file_links_to_open:
		print 'Trying to open ' + line;
		os.system("start \"\" " + line);
	pass

if __name__ == '__main__':
	main();
	pass