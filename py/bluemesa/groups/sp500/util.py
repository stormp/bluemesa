import json
import os

# given a symbol return the industry group name
def get_industry_group_symbol(symbol):
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500.json'
    with open(path) as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
              if symbol in dict_item[key]:
                  return(key)

# given a symbol get the company name
def get_symbol_name(symbol):
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500n.json'
    with open(path) as json_file:
        data = json.load(json_file)
        return(data[symbol])

# get all of the sp500 industry group symbols
def get_industry_group_symbols():
    symbols = set()
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500.json'
    with open(path) as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
              symbols.add(key)
    return(symbols)

# get all of the symbols in the sp500
def get_all_symbols_sp500():
    symbols = set()
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500.json'
    with open(path) as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
            for key in dict_item:
                #print(dict_item[key])
                #print("")
                for item in dict_item[key]:
                    #print(item)
                    symbols.add(item)
    return(symbols)

def get_set_from_dict(list):
    symbols = set()
    for item in list:
        symbols.add(item)
    return(symbols)

# get all of the symbols in a particular industy group
def get_industry_group(symbol):
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500.json'
    with open(path) as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
              if key == symbol:
                  set = get_set_from_dict(dict_item[key])
                  return(set)

if __name__ == "__main__":

    xa = "alle"
    ig = get_industry_group_symbol(xa)
    print(xa, "is in the industry group",ig)
    xa = "cvx"
    ig = get_industry_group_symbol(xa)
    print(xa, "is in the industry group",ig)
    xa = "mo"
    ig = get_industry_group_symbol(xa)
    print(xa, "is in the industry group",ig)

    get_symbol_name("fb")
    get_symbol_name("amzn")

    myig = "xlc"
    ig = get_industry_group(myig)
    print("\nThe symbols in the " + myig + " industry group")
    print(ig)

    print("\nThe Industry Group Symbols")
    symbols = get_industry_group_symbols()
    print(symbols)

    print("\nNumber of symbols in the sp500")
    symbols = get_all_symbols_sp500()
    print(len(symbols))
