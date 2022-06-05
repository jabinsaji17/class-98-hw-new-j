def swapFileData():
  ab = input("Please enter value ")
  bs = input("Please enter value ")

  data_b=(r"file2.txt")
  data_a=(r"file1.txt")

  # To Swap the values of two variables  
  with open(ab,'r') as a:
   data_a = a.read()

  with open(bs,'r') as b:
    data_b = b.read()

  with open(ab,'w') as a:
    a.write(data_b)

  with open(bs,'w') as b:
    b.write(data_a)


  print ("The Value of P after swapping: ",a)
  print ("The Value of Q after swapping: ",b)  
swapFileData()