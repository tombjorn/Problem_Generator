import random
import choices

# length of Problem dict
n = len(choices.ProbType)
# random value from Problem dict
r = random.randint(1, n)

# open with the interntion of writing
File_object = open("Problem_File.py", "w")

# write in problem
File_object.write('# {} \n'.format(choices.ProbType[r]))
File_object.write('{}'.format(choices.fileWriter(r)))

# oh malloc you
File_object.close()
