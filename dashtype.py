variables = {}

def expr(x, default=""):
    try:
      for i,j in variables.items():
        x = x.replace(i,str(j))
      x = x.replace("^","**")
      if x[-1] == ";":
          return str(eval(x[:-1]))+"\n"
      else: return eval(x)
    except:
      print("Error! Expression cannot be evaluated!")
      return default

def out(x):
    y = False
    if type(x) == type("") and x[-1] == "\n":
        y = True
        x = x[:-1]
    try:
        x = float(x)
        if x==int(x):x=int(x)
    except:pass
    finally:
        print(x, end=("\n" if y else ""))

def execute(x):
    x=x.strip()
    if x[0] != ";":
        if x[0] in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_$":
            if x[0] not in variables.keys(): variables[x[0]] = 0
            try:
                if x[1:3] == "<<":
                    if x[3:] in variables.keys(): variables[x[0]] = variables[x[3:]]
                    else: variables[x[0]] = int(x[3:])
            except:
                variables[x[0]] = expr(x[3:], variables[x[0]])
                    
        if x[0:2] == "<<":
            if len(x) == 2: pass
            elif x[2] == "?": out(x[3:])
            elif x[2] in "0123456789":
                if all([i in "0123456789" for i in x[2:]]):out(x[2:])
                else:
                    out(expr(x[2:]))
            elif x[2] in variables.keys():
                if x[2:] in variables.keys():out(variables[x[2:]])
                else: out(expr(x[2:]))
            elif x[2] == ";": out("\n")
            elif x[2] == "(": out(expr(x[2:]))
            else: print("Error! Output is deprecated!")























def run(x):
    with open(x) as f:
        for i in f.readlines():
            execute(i)
            
print("Input file to run (without the .dash extension):")
run(input()+".dash")
