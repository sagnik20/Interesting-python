from zipfile import ZipFile
name = ""
with ZipFile(name,'r')as zip:
    zip.printdir()
    zip.extractall() 
    print("Done!")