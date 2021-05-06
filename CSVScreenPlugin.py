import sys
import numpy
import random
import PyPluMA

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

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
      criteria = self.parameters['criteria']
      self.header = csvfile.readline().strip() # First line has the target column
      headercontents = self.header.split(',')
      tocheck = []
      if (column[0] == '\"'):  # Take out quotes
         column = column[1:len(column)-1]
      for i in range(len(headercontents)):
         if (headercontents[i] != '\"\"' and headercontents[i][0] == '\"'):
            headercontents[i] =headercontents[i][1:len(headercontents[i])-1]
         #if (headercontents[i][0] == 'V'):
         #   print(headercontents[i].startswith(column))
         #   print(headercontents[len(column)])
         #   print(is_number(headercontents[len(column)+1:]))
         if (headercontents[i] == column):
           print(headercontents[i]+"\n")
           tocheck.append(i)
         elif (headercontents[i].startswith(column) and   # For cases where you have more than one strain
               headercontents[i][len(column)] == '-' and
               is_number(headercontents[i][len(column)+1:])):
           print(headercontents[i]+"\n")
           tocheck.append(i)
      #if (headercontents.count(column) == 0):
      if (len(tocheck) == 0):
         PyPluMA.log("[CSVScreen] WARNING: TARGET COLUMN NOT FOUND")
      else:
         self.newlines = []
         for line in csvfile:
           line = line.strip()
           contents = line.split(',')
           if (criteria == "nonzero"):  # Only one has to be nonzero to keep it
              for targetindex in tocheck:
                if (not is_number(contents[targetindex])):
                    self.newlines.append(line)
                elif (float(contents[targetindex]) != 0):
                   self.newlines.append(line)
                   break
           else:  # All have to be zero to keep it
              isZero = True
              for targetindex in tocheck:
                if (not is_number(contents[targetindex])):
                   isZero = False
                   break
                elif (is_number(contents[targetindex]) and float(contents[targetindex]) != 0):
                   isZero = False
                   break
              if (isZero):
                 self.newlines.append(line)

       #else: # All have to be zero to keep it
       #targetindex = headercontents.index(column)
       #self.newlines = []
       #for line in csvfile:
       #  line = line.strip()
       #  contents = line.split(',')
       #  if (is_number(contents[targetindex]) and (criteria == "nonzero" and float(contents[targetindex]) != 0) or (criteria == "zero" and float(contents[targetindex]) == 0)):
       #     self.newlines.append(line)


   def output(self, filename):
      filestuff2 = open(filename, 'w')
      filestuff2.write(self.header+"\n")
      for i in range(len(self.newlines)):
         filestuff2.write(self.newlines[i])
         if (i != len(self.newlines)-1):
            filestuff2.write('\n')



