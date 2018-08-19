import json
import os

file = "/home/laval/Documents/InformationRetrival/Scarpy_project/IR_final/tutsplus/tutsplus/spiders/output/"

all_files = os.listdir(file)
fullData = []
i = 0
if len(all_files) > 0:
    for inputFileName in all_files:
        inputFile = open(file + inputFileName, "r+")
        corpusLines = inputFile.readlines()
        # print(corpusLines[0])
        jsonData = json.loads(corpusLines[0])
        fullData.append(jsonData)
        # fullData += corpusLines
        print(inputFileName)
        # i+=1
        # if i>2:
        #     break

f = open(file + "output-all.json", "w")
f.write(json.dumps(fullData))
print("completed")