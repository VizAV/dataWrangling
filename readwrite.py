import pandas as pd
def read():
    # Get the filename
    print('Enter the name of the file and make sure it is present in data folder..')
    filename = input()

    # Check to catch exception if file is not present

    # Read the file
    inpFile = pd.read_csv('./data/'+filename+'.csv')

    return inpFile

def write(filteredFile):
    filteredFile.to_csv('./data/'+'filteredData'+'.csv')

def main():

    inpFile = read()
    write(inpFile)



if __name__=='__main__':
    main()