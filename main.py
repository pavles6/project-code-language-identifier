import os
import json

fileCount = 0
extensions = []
calculations = {}
results = {}
variants = None

with open(os.path.dirname(os.path.realpath(__file__)) + '/variants.json') as result:
    variants = json.load(result)

for variant in variants:
    calculations[variant] = 0

for path, dirs, files in os.walk(os.getcwd()):
    for item in files:
        extensions.append(os.path.splitext(item)[1])

for ext in extensions:
    for variant in variants:
        for extensionVariant in variants[variant]:
            if(ext == extensionVariant):
                calculations[variant] += 1

for key in calculations:
    fileCount += calculations[key]

for key in list(calculations):
    if(calculations[key] > 0):
        results[key] = "%.2f" % (calculations[key] / fileCount * 100)
    if(calculations[key] == 0):
        del calculations[key]

# registeredFiles - Total file count
# calculations - Number of files
# percentages - Percentage of specific language code scanned
output = {
    "registeredFiles": fileCount,
    "calculations": calculations,
    "percentages": results
}

with open(os.getcwd() + "/project-code-language-identifier.json", "w") as output_file:
    json.dump(output, output_file)
