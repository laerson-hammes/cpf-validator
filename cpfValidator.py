def validateDigit(digit, code, position):
   if int(code[position]) == digit:
      if not position + 1 == len(code):
         validation(code, 10)
      else:
         print(f"{True}")
   else:
      print(f"{False}")
     
def listGenerator(code):
   return list(range(len(code) + 1, 1, -1))

def validation(code, position):
   result = listGenerator(code[:position])
   calc = []
   for number in range(0, len(result), + 1):
      calc.append(int(code[number]) * int(result[number]))
   digit = (sum(calc)) % 11
   if digit < 2:
      validateDigit(digit, code, position)
   else:
      digit = 11 - digit
      validateDigit(digit, code, position)
   
def verifyInput(code):
   if len(code) == 11:
      validation(code, 9)
   else:
      for element in code:
         if not element.isnumeric():
            code.remove(element)
      if len(code) != 11:
         print("[-] ERROR")
      else:
         verifyInput(code)
            
   
code = str(input("[+] CPF: "))
verifyInput(list(code))
