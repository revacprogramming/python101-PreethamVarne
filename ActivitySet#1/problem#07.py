# String
largest = None
smallest= None
while True:
      try:
            num = input("Enter a number: ")
            n = int(num)
            
      except:
        if num == 'done':
                break
        else:
          print("Invalid input")
      
      if largest is None:
        largest=n
          
      elif(n>largest):
        largest=n
      if smallest is None:
        smallest=n
        
      elif(n<smallest):
        smallest=n

print("Maximum is", largest)
print("Minimum is", smallest)
