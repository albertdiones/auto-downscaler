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

outputDirectory = configs['ouput_dir']

print(f"Input Dir: {inputBaseDirectory}")
print(f"Output Dir: {outputDirectory}")

encodedCount=0

for directory, directoryConfig in configs['directories'].items():
    print(directory)
    #print(directoryConfig)

    for filePattern in directoryConfig['filename_patterns']:
        
        directoryFilePattern=f"{inputBaseDirectory}/{directory}/{filePattern}"
    
        for fileName in glob.glob(directoryFilePattern):
            print(f"Found file: {fileName}") 

            newBaseName = os.path.basename(fileName)

            newFileName=f"{outputDirectory}/{directory}/{newBaseName}"
            print(f"Encoding to {newFileName}")
            sleep(0.5);
