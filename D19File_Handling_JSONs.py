# JSON - JavaScript Object Notation (Stringified JS Object or Python Dictionary)
import json
me = '''{"name": "A", "bday": "March 3", "major": "CS"}'''
# loads method turns json into dictionary
me = json.loads(me)
print(me["name"])
# dumps turns dict back into json
me = json.dumps(me)
print(f"{str(type(me))} " + me)
# dump helps us save dict as json file on computer
me = json.loads(me)
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_who_is_jason.json", "w") as j:
    json.dump(me, j, ensure_ascii=False, indent=4)