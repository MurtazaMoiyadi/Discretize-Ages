"""
Program Description: Takes an existing comma-delimited data file
containing an age attribute and creates a new comma-delimited data file
in which each age value is replaced with the letter code for its bin.
"""

infile_name = input('name of input file: ')
split = infile_name.split('.')
split[0] = split[0] + '_disc'
outfile_name =  '.'.join(split)

infile = open(infile_name, 'r')
outfile = open(outfile_name, 'w')

for line in infile:
    line = line[:-1]
    fields = line.split(',')
    age = int(fields[-1])

    if age < 12:
        fields[-1] = 'C'
    elif age > 12 and age < 20:
        fields[-1] = 'T'
    elif age > 19 and age < 36:
        fields[-1] = 'E'
    elif age > 35 and age < 61:
        fields[-1] = 'A'
    else:
        fields[-1] = 'S'

    transformed = ','.join(fields)
    print(transformed, file=outfile)

infile.close()
outfile.close()
