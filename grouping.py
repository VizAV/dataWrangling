import sys
from readwrite import read,write

def listElem(inpFile,groupCol):
    cols = list(inpFile.columns)
    cols.remove(groupCol)


    return inpFile.groupby(groupCol).agg({col: lambda x:list(x) for col in cols})

def firstElem(inpFile,groupCol):
    cols = list(inpFile.columns)
    cols.remove(groupCol)
    return inpFile.groupby(groupCol).agg({col: 'first' for col in cols})

def main():
    dictColType = {}

    # Get the file and the variables that needs filetering
    if sys.argv[1] is None:

        print('Enter the name of the file and make sure it is present in data folder..')
        filename = input()
    else:
        filename = sys.argv[1]

    inpFile = read(filename)

    for cols in inpFile.columns:
        dictColType[cols] = type(inpFile.loc[0, cols])

    print("select the column by which you want to filter")
    cols = inpFile.columns
    for i in range(len(cols)):
        print(i, ":", cols[i])

    groupCols = cols[int(input())]

    print("select the option which you want to select:")
    print("The remaining columns will undergro this operation")
    Options = ['list', 'first']
    for i in range(len(Options)):
        print(i + 1, ":", Options[i])

    groupOption = {1: listElem(inpFile, groupCols),
                   2: firstElem(inpFile,groupCols)
                    }
    groupindex = int(input())
    groupDF = groupOption[groupindex]
    write(groupDF)

if __name__=='__main__':
    main()