from json import dump, load
from os import path

def readJson(filename):
    if(path.exists(filename)):
        with open(filename, "r") as f:
            return load(f)
    else:
        return []
    

def writeJson(newData, filename):
    data = readJson(filename)
    data.append({"id": len(data) + 1, **newData})
    with open(filename, "w") as f:
       dump(data, f, indent=4)
    return "Data berhasil di tambahkan"
    
def deleteJson(id, filename):
    data = readJson(filename)
    index = [i for i, item in enumerate(data) if item["id"] == id]
    if not index: return "Data not Found"
    del data[index[0]]
    with open(filename, "w") as f:
       dump(data, f, indent=4)
    return "Data berhasil di deleted"
    
def updateJson(id, newData, filename):
    data = readJson(filename)
    index = [i for i, item in enumerate(data) if item["id"] == id]
    if not index: return "Data not Found"
    data[index[0]] = { "id": id, **newData }
    with open(filename, "w") as f:
       dump(data, f, indent=4)
    return "Data berhasil di updated"