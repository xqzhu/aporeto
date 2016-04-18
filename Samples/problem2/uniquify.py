import sys
import re
import os


def Merge_Sort(inputfile, outputfile, appendix, minFileSize, showMessage):
    fileLength = os.path.getsize(inputfile)
    fr = open(inputfile, 'r')
    fo = open(outputfile, 'w')
    # If inputfile's size is less then minFileSize:
    # Then copy fr to fo while deleting duplicates at the same time
    if fileLength < minFileSize :
        #print fileLength
        if showMessage:
            print "Sort " + inputfile
        lines = fr.readlines()
        lines.sort()
        fo.write(lines[0])
        for i in range(1, len(lines)):
            if lines[i] == lines[i - 1]:
                continue
            fo.write(lines[i])
    else:
        if showMessage:
            print "Divide " + inputfile
        index = 0
        line = fr.readline()
        
        fSubInput1 = inputfile + str(appendix) + "f"
        fSubInput2 = inputfile + str(appendix) + "l"
        
        fr1 = open(fSubInput1, 'w')
        fr2 = open(fSubInput2, 'w')
        while line != '':
            if index % 2 == 0:
                fr1.write(line)
            else :
                fr2.write(line)
            line = fr.readline()
            index = index + 1
        fr1.close()
        fr2.close()
        fSubOutput1 = outputfile + str(appendix) + "f"
        fSubOutput2 = outputfile + str(appendix) + "l"
        Merge_Sort(fSubInput1, fSubOutput1, appendix + 1, minFileSize, showMessage)
        Merge_Sort(fSubInput2, fSubOutput2, appendix + 1, minFileSize, showMessage)
        fo1 = open(fSubOutput1, 'r')
        fo2 = open(fSubOutput2, 'r')
        line1 = fo1.readline()
        line2 = fo2.readline()
        former = line1[:]
        if line1 < line2:
            fo.write(line1)
            former = line1[:]
            line1 = fo1.readline()
        else:
            fo.write(line2)
            former = line2[:]
            line2 = fo2.readline()
        while line1 != '' and line2 != '':
            if line1 < line2:
                if line1 == former:
                    line1 = fo1.readline()
                    continue
                fo.write(line1)
                former = line1[:]
                line1 = fo1.readline()
            else:
                if line2 == former:
                    line2 = fo2.readline()
                    continue
                fo.write(line2)
                former = line2[:]
                line2 = fo2.readline()
        while line1 != '':
            if line1 == former:
                line1 = fo1.readline()
                continue
            fo.write(line1)
            former = line1[:]
            line1 = fo1.readline()
        while line2 != '':
            if line2 == former:
                line2 = fo2.readline()
            fo.write(line2)
            former = line2[:]
            line2 = fo2.readline()
        if showMessage:
            print "Merge as " + outputfile
        fo1.close()
        fo2.close()
        os.remove(fSubInput1)
        os.remove(fSubInput2)
        os.remove(fSubOutput1)
        os.remove(fSubOutput2)
    fr.close()
    fo.close()
    

arglist = sys.argv[:]
#print len(arglist)
if len(arglist) == 1:
    print "Missing parameter"
    print "Usage:"
    print "uniquify [--help|-h]"
    print "uniquify --file=<filename> --output=<output-filename> [-verbose]"
    sys.exit(0)

firstParameter = sys.argv[1]
if firstParameter == "--help" or firstParameter == "-h":
    print "Usage:"
    print "uniquify [--help|-h]"
    print "uniquify --file=<filename> --output=<output-filename> [-verbose]"
    sys.exit(0)

# Basic idea
# Divide the file into two files with almost equal length. Do this until the size of files are under a certain number

# Check if the input is correct
if len(arglist) == 3:
    inputFileExpression1 = arglist[1]
    inputFileExpression2 = arglist[2]
    
    judge1 = inputFileExpression1.startswith("--file=")
    judge2 = inputFileExpression2.startswith("--output=")
    
    if judge1 != True or judge2 != True:
        print "Usage:"
        print "uniquify [--help|-h]"
        print "uniquify --file=<filename> --output=<output-filename> [-verbose]"
        sys.exit(0)
        
    firstFileName = inputFileExpression1[7:]
    secondFileName = inputFileExpression2[9:]
    
    Merge_Sort(firstFileName, secondFileName, 0, 5, False)
    
    #print firstFileName, secondFileName
    
    sys.exit(0)


if len(arglist) == 4 and arglist[3] == "-verbose":
    inputFileExpression1 = arglist[1]
    inputFileExpression2 = arglist[2]
    
    judge1 = inputFileExpression1.startswith("--file=")
    judge2 = inputFileExpression2.startswith("--output=")
    
    if judge1 != True or judge2 != True:
        print "Usage:"
        print "uniquify [--help|-h]"
        print "uniquify --file=<filename> --output=<output-filename> [-verbose]"
        sys.exit(0)
        
    firstFileName = inputFileExpression1[7:]
    secondFileName = inputFileExpression2[9:]
    
    Merge_Sort(firstFileName, secondFileName, 0, 5, True)
    
    #print firstFileName, secondFileName
    
    sys.exit(0)






print "Error"
print "Usage:"
print "uniquify [--help|-h]"
print "uniquify --file=<filename> --output=<output-filename> [-verbose]"


