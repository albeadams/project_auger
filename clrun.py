import os
import re
from os.path import isfile, join
from os import listdir

import setup

DATADIR = os.path.join(os.getcwd(), 'data\\')
LOOKUPDIR = os.path.join(os.getcwd(), 'lookup\\')
LEARNERDICT = {}


def main():
  greeting()
  chosen_dataset = getdatasets_input()
  chosen_learners = getlearner_input()
  dataset, learners = parse_options(chosen_dataset, chosen_learners)
  print("\n  Chosen data set: ")
  print('    ' + dataset)
  print("\n  Chosen learners: ")
  print('    ' +str(learners))
  ra = setup.RunAuger(dataset, learners)
  ra.stage()

def greeting():
  print("""\n
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


def showdatasets():
  index = 1
  for csv in listdir(DATADIR):
    file, ext = os.path.splitext(os.getcwd() + csv)
    if ext == '.csv':
      print('    ' +str(index) + '. ' +csv)
      index = index + 1
  print()
  return index


def getdatasets_input():
  print("  Choose a dataset\n")
  total_datasets = showdatasets()
  while True:
    choice = input("  Enter a number: ")
    try:
      choice = int(choice)
      if choice > total_datasets or choice < 1:
        print("Number not in range, try again.")
      else:
        break
    except ValueError:
      print("Not a number, try again.")
  print("\n  You chose: " + get_dataset_name(choice) + "\n\n  Awesome choice!\n")
  return choice


def getlearner_input():
  while True:
    print("\n  Choose your learner(s)\n")
    total_learners = showlearners()
    choice = input("Use standard slicing notation, i.e. [:3], or comma-separated by number: ")
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
        print("No learners chosen")
    else:
      print('Non-integer value entered, try again.')


def showlearners():
  f = open(os.path.join(LOOKUPDIR, 'model_options.txt'), 'r')
  for index, model in enumerate(f):
    print('  '+str(index+1)+'. '+model, end='')
    LEARNERDICT[index+1] = model
  print('\n')
  return (index+1)


def get_dataset_name(numchosen):
  index = 1
  for csv in listdir(DATADIR):
    file, ext = os.path.splitext(os.getcwd() + csv)
    if ext == '.csv':
      if index == numchosen:
        return csv
      index = index + 1


def parse_options(dataset, run_learners):
  dataset = get_dataset_name(dataset)
  learners = [LEARNERDICT[l].replace('\n', '') for l in run_learners]
  return dataset, learners

if __name__ == '__main__':
  main()