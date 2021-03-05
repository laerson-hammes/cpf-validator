def validate_digit(digit, code, position):
   if int(code[position]) == digit:
      if not position + 1 == len(code):
         validation(code, 10)
      else:
         print(f"[+] {True}")
   else:
      print(f"[-] {False}")
     
listGenerator = lambda code: list(range(len(code) + 1, 1, -1))

def validation(code, position):
   result = list_generator(code[:position])
   calc = []
   for number in range(0, len(result), + 1):
      calc.append(int(code[number]) * int(result[number]))
   digit = (sum(calc)) % 11
   if digit < 2:
      validate_digit(digit, code, position)
   else:
      digit = 11 - digit
      validate_digit(digit, code, position)
   
def verify_input(code):
   if len(code) == 11:
      validation(code, 9)
   else:
      for element in code:
         if not element.isnumeric():
            code.remove(element)
      if len(code) != 11:
         print("[-] ERROR")
      else:
         verify_input(code)
            
   
code = str(input("[+] CPF: "))
verify_input(list(code))
