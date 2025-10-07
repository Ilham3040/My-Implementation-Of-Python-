def greet(name): return f"Hello, {name}!"
def bye(name):   return f"Goodbye, {name}!"
def shout(name): return f"{name.upper()}!!!"

commands = {
    "greet": greet,
    "bye":   bye,
    "shout": shout
}

cmd, arg = "shout", "yugo"
result = commands[cmd](arg)
print(result)  # → YUGO!!!


def red():    return "Stop"
def yellow(): return "Caution"
def green():  return "Go"

traffic = {"RED": red, "YELLOW": yellow, "GREEN": green}

state = "YELLOW"
print(traffic[state]())  # → Caution


import json, csv, io

def parse_json(data):
    return json.loads(data)

def parse_csv(data):
    reader = csv.reader(io.StringIO(data))
    return list(reader)

parsers = {
    "json": parse_json,
    "csv":  parse_csv
}

data_type = "csv"
raw_data = "name,score\nYugo,100\nAki,95"
parsed = parsers[data_type](raw_data)
print(parsed)  # → [['name','score'],['Yugo','100'],['Aki','95']]
