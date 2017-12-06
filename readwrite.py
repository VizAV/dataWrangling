import pandas as pd

def read(filename):
    # Get the filename


    # Check to catch exception if file is not present

    # Read the file
    inpFile = pd.read_csv('./data/'+filename+'.csv')

    return inpFile

def write(outputFile):
    print("Writing the file as treatedData.csv")
    outputFile.to_csv('./data/'+'treatedData'+'.csv')

def main():

    inpFile = read()
    write(inpFile)

if __name__=='__main__':
    main()