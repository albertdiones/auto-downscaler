import os
import re
from time import sleep
import yaml
import glob

with open("config.yml", "r") as stream:
    try:
        configs = yaml.safe_load(stream)
    except yaml.YAMLError as exception:
        print(exception)

quality = configs['quality']

inputBaseDirectory=configs['input_base_dir']

outputBaseDirectory = configs['ouput_dir']

handbrakePathname = configs['handbrakecli_pathname'];

eParameter = f"{configs['handbrakecli_extra_parameters']}" if configs.get('handbrakecli_extra_parameters') != None else '';

print(f"Input Dir: {inputBaseDirectory}")
print(f"Output Dir: {outputBaseDirectory}")

if not os.path.isdir(outputBaseDirectory):
    os.makedirs(outputBaseDirectory)

encodedCount=0

commands=[]

for directory, directoryConfig in configs['directories'].items():
    print(directory)
    #print(directoryConfig)
    outpuDirectory =f"{outputBaseDirectory}/{directory}";

    if not os.path.isdir(outpuDirectory):
        os.makedirs(outpuDirectory);    

    for filePattern in directoryConfig['filename_patterns']:
        
        directoryFilePattern=f"{inputBaseDirectory}/{directory}/{filePattern}"
    
        for fileName in glob.glob(directoryFilePattern):
            #print(f"Found file: {fileName}") 

            newBaseName = os.path.basename(fileName)

            newFileName=f"{outpuDirectory}/{newBaseName}"
            #print(f"Encoding to {newFileName}")

            if os.path.isfile(newFileName):
                continue

            command = f"{handbrakePathname} -i \"{fileName}\" -o \"{newFileName}\" -q{str(quality)} {eParameter}"

            commands.append(command)


for command in commands:
    print(command)

if input("Do you want to run these commands? (yes/n)")[0].lower() !='yes':
    print("You have cancelled the commands")

for command in commands:
    os.system(command)
