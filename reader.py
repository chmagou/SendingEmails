import csv
import os
import time

def file_is_empty(file):
    return  os.stat(file).st_size == 0

def readFile(file):
  t = time.process_time()
  listOfData = []
  with open(file, 'r') as csvFile:
      if file_is_empty(file):
          print("File is empty!")
      else:
          csvReader = csv.reader(csvFile)
          for row in csvReader:
              if not row:
                  continue
              else:
                  listOfData.append(row)
  finishTime = time.process_time() - t
  print("Reading file: "+ file + ", time elapsed: "+ str(finishTime))
  return listOfData

readFile("info_file.csv")