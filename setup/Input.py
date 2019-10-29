from learners.LinearModels import info

### This class is a wrapper around user input.
### It allows user to gain access to any help needed by typing 'help'.
### Input imports the info.py information from each group of learners,
### in addition to other types of information.

class Input(object):

  def __init__(self):
    pass

  def print_out(self, outstr=None, end=None, extraspace=None):
    space = '  '
    if not extraspace == None:
      space = space + extraspace
    print(space + outstr, end=end)

  def get_input(self, str='', yn=False, inpstr=None, errormsg=None):
    inpstr = '  '+inpstr
    if errormsg == None:
      errormsg = 'Wrong input'
    errormsg = '  '+errormsg
    while True:
      response = input(inpstr)
      if response.split(' ')[0] == 'help':
        self.help_me(response)
      else:
        if yn:
          if response != 'y' && response != 'n':
            print(errormsg)
          else:
            return response
        else:
          return response


  def help_me(self, response):
    if len(reponse.split(' ')) > 1:
      self.parse_help(response)

    print("""\n
      To get help on a specific model, type: help <model_name>
      Example:

        help LinearRegression

      To get help on a specific aspect of a model, type: help <model_name> <specifics>
      Choices are:

        help <model_name> --params
        help <model_name> --result
        help <model_name> --example
        help <model_name> --methods
        help <model_name> --notes

        Or, to get all of the above:

        help <model_name> --all

      To list all learners, type:

        help learners --list

      Other help functionality will be added in the future.\n""")
    while True:
      response = input("Enter help request, or type 'x' to continue: ")
      if response == 'x':
        return
      parse_help(response)


  def parse_help(self, response):
    #TODO: parse request and grab info from info.py or whereever
    pass