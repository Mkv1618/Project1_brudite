import yaml
import json

data=dict()

with open("exjson.json", "r") as f:
    data={'mails':json.load(f)}
    print(data)

with open("exyaml.yaml", "w") as f:
    yaml.dump(data, f)