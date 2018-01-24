
def readFile(fileName):
    newFile= open ('dataProcessed.txt','w') 
    
    # We need to add header before details inserted to the file
    newFile.write('Name|Middle|DOB|SSN|Filepath\n')
    with open (fileName) as files:
        lines = files.readlines()
        SplitLines(lines,newFile)
    
def SplitLines(lines,newFile): 
    words=[]
    
    for line in lines:
        words = line.rstrip().split("\\")
        eachLine=line
        if len(words)>6:    
            processingData(words[6],newFile, eachLine)
      
#this will received 6th position i.e.Namrata,Dhuru 11-02-1990 xxx-xx-xxxx
def processingData(data,newFile,eachLine):
    
    name=[]
    dob=[]
    ssn=[]
    middle=[]
    dataFields= data.split(" ")
    #dataFields are Namrata,Dhuru,11-02-1990, xxx-xx-xxxx
    if len(dataFields)>2:
        name = dataFields[0] 
        dob= dataFields[-2]
        ssn=dataFields[-1]
        line=eachLine
        if len(dataFields)>3:
            middle=dataFields[1]
        else:
            middle=''
        DataLine= '|'.join([name ,middle,dob,ssn,eachLine])
     
        
        newFile.write(DataLine + '\n')
    else:
        print("Not valid")