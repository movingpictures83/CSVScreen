import sys
import numpy
import random
import PyPluMA

class CSVScreenPlugin:
   def input(self, filename):
      self.txtfile = open(filename, 'r')
      self.parameters = dict()
      for line in self.txtfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      if len(PyPluMA.prefix()) != 0:
         self.parameters['csvfile'] = PyPluMA.prefix() + "/" + self.parameters['csvfile']

   def run(self):
      self.newlines = []
      column = self.parameters['column']
      csvfile = open(self.parameters['csvfile'], 'r')
      self.header = csvfile.readline().strip() # First line has the target column
      headercontents = self.header.split(',')
      if (headercontents.count(column) == 0):
         PyPluMA.log("[CSVScreen] WARNING: TARGET COLUMN NOT FOUND")
      else:
       targetindex = headercontents.index(column)
       self.newlines = []
       for line in csvfile:
         line = line.strip()
         contents = line.split(',')
         if (float(contents[targetindex]) != 0):
            self.newlines.append(line)


   def output(self, filename):
      filestuff2 = open(filename, 'w')
      filestuff2.write(self.header+"\n")
      for i in range(len(self.newlines)):
         filestuff2.write(self.newlines[i])
         if (i != len(self.newlines)-1):
            filestuff2.write('\n')



