import csv
def handler():
  context.logger.info('This is an unstructured log')
  with open('test.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
      print ', '.join(row)