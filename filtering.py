from readwrite import read,write



def greaterThan(inpFile,filterCol, filterValue):

    return inpFile[inpFile[filterCol]>filterValue]


def lesserThan(inpFile,filterCol, filterValue):
    return inpFile[inpFile[filterCol] < filterValue]


def equalTo(inpFile,filterCol, filterValue):
    return inpFile[inpFile[filterCol] == filterValue]


def notEqualto(inpFile,filterCol, filterValue):
    return inpFile[inpFile[filterCol] !=  filterValue]


def exists(inpFile,filterCol):
    return inpFile[inpFile[filterCol].notnull()]



def main():
    # Get the file and the variables that needs filetering
    inpFile = read()

    print("select the column by which you want to filter")
    cols = inpFile.columns
    for i in range(len(cols)):
        print(i,":", cols[i])

    filterCol = cols[int(input())]


    print ("Enter the value for filtering")
    filterValue = int(input())


    print("select the option which you want to select")
    Options = ['> (greater than)', '< (lesser than)', '= (equal to )','!= (not equal to )','exists']
    for i in range(len(Options)):
        print(i+1, ":", Options[i])

    filterOption = {1: greaterThan(inpFile, filterCol, filterValue),
                    2: lesserThan(inpFile, filterCol, filterValue),
                    3: equalTo(inpFile, filterCol, filterValue),
                    4: notEqualto(inpFile, filterCol, filterValue),
                    5: exists(inpFile, filterCol)
                    }
    filterindex = int(input())
    filteredDF = filterOption[filterindex]
    write(filteredDF)

if __name__=='__main__':
    main()
