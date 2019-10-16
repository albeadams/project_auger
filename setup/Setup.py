import setup

import os
import re
from os.path import isfile, join
from os import listdir

DATADIR = os.path.join(os.getcwd(), 'data\\')
LOOKUPDIR = os.path.join(os.getcwd(), 'lookup\\')

class Setup(object):

  def __init__(self):
    self.inp = setup.Input()
    self.learnerdict = {}

  def main(self):
    self.greeting()
    chosen_dataset = self.getdatasets_input()
    chosen_learners = self.getlearner_input()
    dataset, learners = self.parse_options(chosen_dataset, chosen_learners)
    self.inp.print_out("Chosen data set: ")
    self.inp.print_out(dataset, extraspace='    ')
    self.inp.print_out("Chosen learners: ")
    self.inp.print_out(str(learners), extraspace='    ')
    self.inp.print_out('At any time, type \'help\' to get help.')
    ra = setup.RunAuger(DATADIR, dataset, learners)
    ra.stage()


  def greeting(self):
    self.inp.print_out("""\n
      Welcome to Project Auger!\n
      Project Auguer is ML learning tool
      that allows you to select a dataset and ML model(s),
      mash them together, and spit out awesome results
      that will fundamentally alter the course of humanity.
      Or make your head spin enough that you go back and study art history.
      We all want to avoid art history, so PAY ATTENTION!!!

      Please select the dataset you wish to cram into our models.
      Note that any dataset you wish to use:
        a. must exist in the project_auger /data directory (no subdirs)
        b. must be a .csv file

      Without further ado, here are the datasets!!!\n""")


  def getdatasets_input(self):
    self.inp.print_out("Choose a dataset")
    total_datasets = self.showdatasets()
    while True:
      choice = self.inp.get_input("Enter a number: ")
      try:
        choice = int(choice)
        if choice > total_datasets or choice < 1:
          self.inp.print_out("Number not in range, try again.")
        else:
          break
      except ValueError:
        self.inp.print_out("Not a number, try again.")
    datasetname = self.get_dataset_name(choice)
    self.inp.print_out("You chose: " + datasetname + "\n\n  Awesome choice!\n")
    return choice


  def showdatasets(self):
    index = 1
    for csv in listdir(DATADIR):
      file, ext = os.path.splitext(os.getcwd() + csv)
      if ext == '.csv':
        self.inp.print_out(str(index) + '. ' +csv, extraspace='  ')
        index = index + 1
    self.inp.print_out('')
    return index-1


  def getlearner_input(self):
    while True:
      self.inp.print_out("Choose your learner(s)")
      total_learners = self.showlearners()
      choice = self.inp.get_input("Use standard slicing notation, i.e. [:3], or comma-separated by number: ")
      choice = choice.split(',')
      run_learners = []
      correct_nums = 1
      for num in choice:
        if re.search("\A\[",num) and re.search("\]\Z",num):
          num = num.split(':')
          start = num[0].replace('[', '')
          end = num[1].replace(']','')
          if start:
            try:
              start = int(start)
            except ValueError:
              correct_nums = 0
              break
            if start < 1:
              start = 1
          else:
            start = 1
          if end:
            try:
              end = int(end)
            except ValueError:
              correct_nums = 0
              break
            if end > total_learners:
              end = total_learners + 1
          else:
            end = total_learners + 1
          for eachnum in range(start, end):
            run_learners.append(eachnum)
        else:
          try:
            toenter = int(num)
          except ValueError:
            correct_nums = 0
            break
          if not toenter > total_learners:  
            run_learners.append(toenter)

      if(correct_nums):
        if run_learners:
          run_learners = list(dict.fromkeys(run_learners))
          return sorted(run_learners)
        else:
          self.inp.print_out("No learners chosen")
      else:
        self.inp.print_out('Non-integer value entered, try again.')


  def showlearners(self):
    f = open(os.path.join(LOOKUPDIR, 'model_options.txt'), 'r')
    for index, model in enumerate(f):
      self.inp.print_out(str(index+1)+'. '+model, end='')
      self.learnerdict[index+1] = model
    self.inp.print_out('\n')
    return (index+1)


  def get_dataset_name(self, numchosen):
    index = 1
    for csv in listdir(DATADIR):
      file, ext = os.path.splitext(os.getcwd() + csv)
      if ext == '.csv':
        if index == numchosen:
          return csv
        index = index + 1


  def parse_options(self, dataset, run_learners):
    dataset = self.get_dataset_name(dataset)
    learners = [self.learnerdict[l].replace('\n', '') for l in run_learners]
    return dataset, learners
