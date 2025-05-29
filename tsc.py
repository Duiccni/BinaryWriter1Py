def form(s: str):
   s = s.split(';', 1)[0]
   if len(s) == 0:
      return ('\0', '\0')
   return (s[0].upper(), s[1:].strip())

# C:/Users/abi37/AppData/Local/Programs/Python/Python312/python.exe tsc.py dll.tsl mydll.dll
# C:/Users/abi37/AppData/Local/Programs/Python/Python312/python.exe tsc.py input.tsl PE2.exe

import sys

file = open(sys.argv[1], "r")
lines = list(map(form, file.readlines()))
file.close()

data = []
variables = {}

for line in lines:
   variables["_HERE"] = len(data)
   match line[0]:
      case 'C':
         nv = line[1][1:].split(',', 1)
         index, value = eval(nv[0], variables), eval(nv[1], variables)
         match line[1][0]:
            case 'B':
               data[index] = value & 0xFF
            case 'W':
               data[index] = value & 0xFF
               data[index + 1] = (value >> 8) & 0xFF
            case 'D':
               data[index] = value & 0xFF
               data[index + 1] = (value >> 8) & 0xFF
               data[index + 2] = (value >> 16) & 0xFF
               data[index + 3] = (value >> 24) & 0xFF
            case 'Q':
               data[index] = value & 0xFF
               data[index + 1] = (value >> 8) & 0xFF
               data[index + 2] = (value >> 16) & 0xFF
               data[index + 3] = (value >> 24) & 0xFF
               data[index + 4] = (value >> 32) & 0xFF
               data[index + 5] = (value >> 40) & 0xFF
               data[index + 6] = (value >> 48) & 0xFF
               data[index + 7] = (value >> 56) & 0xFF
      case 'I':
         s = line[1]
         if s[0] != '"' or s[-1] != '"':
            raise ValueError("Expected String")
         file = open(s[1:-1], "rb")
         data += file.read()
         file.close()
      case 'M':
         nv = line[1].split(',', 1)
         variables[nv[0].strip()] = eval(nv[1], variables)
      case 'L':
         variables[line[1]] = len(data)
      case 'B':
         value = eval(line[1], variables)
         data.append(value & 0xFF)
      case 'W':
         value = eval(line[1], variables)
         data.append(value & 0xFF)
         data.append((value >> 8) & 0xFF)
      case 'D':
         value = eval(line[1], variables)
         data.append(value & 0xFF)
         data.append((value >> 8) & 0xFF)
         data.append((value >> 16) & 0xFF)
         data.append((value >> 24) & 0xFF)
      case 'Q':
         value = eval(line[1], variables)
         data.append(value & 0xFF)
         data.append((value >> 8) & 0xFF)
         data.append((value >> 16) & 0xFF)
         data.append((value >> 24) & 0xFF)
         data.append((value >> 32) & 0xFF)
         data.append((value >> 40) & 0xFF)
         data.append((value >> 48) & 0xFF)
         data.append((value >> 56) & 0xFF)
      case 'A':
         value = eval(line[1], variables)
         data += [0] * ((((len(data) + value - 1) // value) * value) - len(data))
      case 'Z':
         value = eval(line[1], variables)
         data += [0] * value
      case 'S':
         s = line[1]
         if s[0] != '"' or s[-1] != '"':
            raise ValueError("Expected String")
         for c in s[1:-1]:
            data.append(ord(c))

# for i in data:
#    s = hex(i)[2:]
#    print(s if len(s) == 2 else '0' + s, end=' ')

file = open(sys.argv[2], "wb")
file.write(bytearray(data))
file.close()