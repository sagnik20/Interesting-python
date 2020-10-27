# Ask user to input the file name, it is a .txt file
filename = input('Input your filename: ')
# open the inputed file with parameter 'r' means read only
file = open(filename, 'r')
# create new file with name same with inputed file name but added '_out'
# parameter 'w' means write and will create new file when doesn't exist
output_file = open(filename+'_out', 'w')
# read each lines in the inputed file, store in the list data type
lines = file.readlines()

# loop every elemen in the list lines
# then replace '\n' with ' ' (space)
# last write it into the output file
for line in lines:
    line=line.replace('\n', ' ')
    output_file.write(line)
