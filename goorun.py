from gooey.python_bindings.gooey_decorator import Gooey
from gooey.python_bindings.gooey_parser import GooeyParser

import argparse
import sys
import os

import learners

DATADIR = os.path.join(os.getcwd(), 'data\\')
data_files = []
data_parsers = []
cust_group = []

@Gooey(program_name="Project Auger",
		default_size=(650,500),
		return_to_config=False,
		sidebar_title='Datasets',
		header_bg_color='#931817',
		image_dir='lookup\\')
def main():
	parser = GooeyParser(description='ML Model Tester')

	#parser.add_argument("FileChooser", help="Choose data csv file", widget="FileChooser")
	subs = parser.add_subparsers(help='commands', dest='command')

	for ind, f in enumerate(os.listdir(DATADIR)):
		if os.path.splitext(f)[0] != 'instructions':
			models = open(os.path.join(os.getcwd(),'lookup\\model_options.txt'), 'r')
			data_files.append(os.path.splitext(f)[0])
			data_parsers.append(ind)
			data_parsers[ind] = subs.add_parser(data_files[ind])
			#data_parsers[ind].add_argument('Verbose',help='Turn verbose option on/off', widget='CheckBox')
			data_parsers[ind].add_argument(
					'--load',
					metavar='',
					help='Choose learners:',
					dest='',
					widget='Listbox',
					choices=list_savefiles(),
					nargs='+',)
			

	args = parser.parse_args()
	controller.test(args)
	

def list_savefiles():
	model = []
	f = open(os.path.join(os.getcwd(),'lookup\\model_options.txt'), 'r')
	for m in f:
		model.append(m.rstrip())
	return sorted(model, reverse=False)

if __name__ == '__main__':
	main()