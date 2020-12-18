nGroups = 34 # number of experiment files to generate

with open('Results_js_620.txt', 'r') as gfile:
    # read the results file in javascript language.
    groupsData = gfile.readlines()


with open('experiment_take3.html', 'r') as bfile:
    # read the experiment html template
    baseData = bfile.readlines()

# for each group of tuples
for i in range(1,nGroups+1):
    # create a new experiment file and open it:
    with open(f'experiment{i}.html', 'w+') as efile:
        # print fuck you to the console
        print('creating new html experiment file..')
        # copy template html file to list of lines
        expData=baseData
        # find the appropriat lines in the results file that contain the tuples
        # of the current group and paste them in the appropriate lines of the
        # template:
        idx = 2 + (i-1)*26
        expData[25:49] = groupsData[idx:idx+24]
        # write the edited list of lines into the new file
        efile.writelines(expData)
