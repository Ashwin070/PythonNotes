#create a class to begin with
class Computer:
  #Now you can add Attributes(Variables) and Behaviour(Methods) to this class
  
  def config(self):
    print("i5,16GB,1TB")
    
#Now we make an object of the class that is made above
com1=Computer()

# Calling the above object
#1st way->
Computer.config(com1)

#2nd way->
com1.config()
