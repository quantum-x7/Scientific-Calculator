import datetime
import math
History_file = "history.txt"
def show_history():
   try: 
      with open(History_file,'r') as file:
         lines = file.readlines()
         if len(lines) == 0:
            print("History Not Found")
         else:
            for line in  reversed(lines):
               print(line.strip())   
   except FileNotFoundError as e:
      print("History file not found!")            

def clear_his():
   confirm = input("Are you sure for clearing history(yes/no):")
   if confirm.lower() == "yes":
      with open(History_file,'w') as file:
         print("History is Cleared")
   else:
      print("Clear canceled")   

def save_his(eq,result):
   with open (History_file,'a') as file:
      time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      file.write(f"{time} | {eq} = {str(result)} \n")
def calcu(user):
   part = user.split()
   
   if len(part) == 2 and part[0] in ["sin", "cos", "sqrt", "tan_inv","sin_inv","cos_inv","sqr","cube"]:
      try:
         func = part[0]
         num = float(part[1])
         if func == "sin":
            result = math.sin(math.radians(num))
         elif func == "cos":
             result = math.cos(math.radians(num))      
         elif func == "tan":
             result = math.tan(math.radians(num))
         elif func == "sin_inv":
             if num < -1 or num > 1:
                print("Error: sin_inv input must be between -1 and 1")
                return
             result = math.degrees(math.asin(num))
         elif func == "cos_inv":
             if num < -1 or num > 1:
                print("Error: cos_inv input must be between -1 and 1")
                return
             result = math.degrees(math.acos(num))
         elif func == "tan_inv":
             result = math.degrees(math.atan(num))
         elif func == "sqr":
             result = (num*num)
         elif func == "cube":
             result = (num*num*num)
         elif func == "sqrt":
             if num < 0:
                print("Not meant to sqrt of neg no.")
             else:
                result = math.sqrt(num)

         print("Result:", result)
         save_his(user,result)
         return       
      except ValueError:
         print("Invalid value")
   if len(part) != 3:
       print("Invalid input! Correct format: num1 operator num2 (Example: 5 + 3)or sin 78")
       return 
   try: 
      num1 = float(part[0])
      op = part[1]
      num2 = float(part[2])
   
   except ValueError:
       print("Error: Invalid number format!")   
       return
    
   if op == "+":
       result = num1 + num2
   elif op == "-":
       result = num1 - num2
   elif op in ["x" , '*']:
       result = num1 * num2
   elif op == "/" :
        try:
            result = num1 / num2
        except ZeroDivisionError as e:
            print("Caught error:", e)
            return
   elif op in[ "^" , "**"]:
       result = num1 ** num2
   else:
       print("Invalid Operand!")   
   if int(result) == result:
       result = int(result)   
   print("Result: ",result)
   save_his(user,result)  
def main():
   print("=== Welcome to Terminal Calculator ===")  
   while True:
      user = input("Enter Calculation(+,-,x,/,^ and scitefic) or Commands(Show history,clear history or exit): ")

      user = user.lower().strip()
      if user == "exit":
         print("Good Bye")
         break
      elif user in ["show history","history"]:
         print("HISTORY:")
         show_history()
      elif user == "clear history":
         clear_his()
      elif user in ["scientific", "sci"]:
         print("OPTIONS: sin", "cos", "sqrt", "tan_inv",'\n','\t' "sin_inv","cos_inv","sqr","cube")

      else:
         calcu(user)
main() 