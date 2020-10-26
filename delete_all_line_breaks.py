filename = input('Input your filename: ') # .txt
file = open(filename, 'r')
output_file = open(filename+'_out', 'w')
lines = file.readlines()

for line in lines:
    line=line.replace('\n', ' ')
    output_file.write(line)
