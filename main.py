import os
import yaml
import json

configPath = os.path.dirname(os.path.realpath(__file__)) + '/config/'
fileCount = 0
extensions = []
calculations = {}
results = {}
excludes = []
variants = None

with open(configPath + 'excludes.yml') as result:
    excludes = yaml.load(result, Loader=yaml.SafeLoader)

with open(configPath + 'variants.yml') as result:
    variants = yaml.load(result, Loader=yaml.SafeLoader)

for variant in variants:
    calculations[variant] = 0

for path, dirs, files in os.walk(os.getcwd()):
    dirs[:] = [d for d in dirs if d not in excludes]
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

# registeredFiles - Total count of scanned files
# calculations - Number of files with specific code language
# percentages - Percentage of specific language code scanned
output = {
    "registeredFiles": fileCount,
    "calculations": calculations,
    "percentages": results
}

with open(os.getcwd() + "/project-code-language-identifier.json", "w") as output_file:
    json.dump(output, output_file)
