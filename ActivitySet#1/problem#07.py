# String
largest = 0
smallest=50
while True:
      try:
            num = input("Enter a number: ")
            if num == 'done':
                break
            n = int(num)
            if(n<smallest):
                 smallest=n
            if(n>largest):
                 largest=n
      except:
             print("Invalid input")
        
   
      
           

print("Maximum is", largest)
print("Minimum is", smallest)
