prices={
      'rice':50,
      'wheat':40,
      'sugar':45,
      }
quantity={
      'rice':2,
      'wheat':3,
      'sugar':1,
      }
total=0
for item in prices:
      total+= prices[item]+quantity.get(item,0)
      print("Total Bill=",total)
      
