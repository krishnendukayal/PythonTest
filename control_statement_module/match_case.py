def access(user):
   match user:
      case "admin" | "manager": return "Full access"
      case "Guest": return "Limited access"
      case _: return "No access"
print (access("manager"))
print (access("Guest"))
print (access("Ravi"))

def greeting(details):
   match details:
      case [time, name]:
         return f'Good {time} {name}!'
      case [time, *names]:
         msg=''
         for name in names:
            msg+=f'Good {time} {name}!\n'
         return msg

print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))


def intr(details):
   match details:
      case [amt, duration] if amt<10000:
         return amt*10*duration/100
      case [amt, duration] if amt>=10000:
         return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))


numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
   print (x)


numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x,y in numbers.items():
   print (x,":", y)


numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.keys():
   print (x, ":", numbers[x])