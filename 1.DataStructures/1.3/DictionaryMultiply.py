state = {"a":0.5,"b":0.5}

matrix = {
    "a":{"a":0.1,"b":0.9},
    "b":{"a":0.2,"b":0.8},
          }

current = {"a":0,"b":0}

current["a"] = state["a"]*matrix["a"]["a"]+state["b"]*matrix["b"]["a"]
current["b"] = state["a"]*matrix["a"]["b"]+state["b"]*matrix["b"]["b"]

print(current)