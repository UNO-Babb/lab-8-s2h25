#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #header
  outFile.write("LastName, FirstName, StudentID, Major-Year\n")
  
  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    major = data[6]
    year = data[5]
    idNum = data[4]

    student_id = makeID(first, last, idNum)
    major_year = makeMajorYear(major,year)

    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)
    #print(student_id)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID( first, last, idNum):
  
  idLen = len(idNum)



  while len(last) < 5:
    last = last + "x"

  id = first[0] + last + idNum[idLen - 3: ]
  return id

def makeMajorYear(major, year):
    major_abbr = major[:3].capitalize()
    year = year.lower().capitalize()

    #If/elif
    if year == "Freshman":
       year_abbr = "FR"
    elif year == "Sophomore":
       year_abbr = "SO"
    elif year == "Junior":
       year_abbr = "JR"
    elif year == "Senior":
       year_abbr = "SR"
    else: 
       year_abbr = "??"   

    return major_abbr + "-" + year_abbr   
    
if __name__ == '__main__':
  main()
