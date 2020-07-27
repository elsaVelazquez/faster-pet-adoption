import os
'''
    For the given path, get the List of all files in the directory tree 
    Use this to mash all json files together in command line using jq
'''


# dirName = '../data/json_dump';



def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    print(allFiles)                
    return allFiles        
    
# dirName = '../data/json_dump';
    

 