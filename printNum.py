import ourModule
import datetime





if __name__=="__main__":
    results =ourModule.getNumbers(5,9)
    print(results)
    a = ourModule.person1['name']
    print(a)
    x = datetime.datetime.now()
    print(x)

#This is a comment.
#The function above is creating a results function and it imports the getNumber function we createed
#We put in the values 5 and 9 and it will display 45 in the IDLE
# we called the datetime import with the datetime.now function. That will display the current time
