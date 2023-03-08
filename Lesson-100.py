
x = 1000
y = 5
raz = 'testing'
#leaving a note to see final test
print(x +y)


def my_function(first_name):
    print(first_name + ' Lightyear')

#created function with a parameter to add 'Lightyear' to the first name' 

my_function('Buzz')

# called my_function with Buzz as the argument. 

cars = ['Ford','BMW','Hyundai','Cadilac','Honda']
for x in cars:
    print(x)
    if x == 'Hyundai':
        break


def first_function(name,score):
    player = 'Hey {} you scored {} points!'.format('Jake',20)
    print(player)

Jake_score = first_function('Jake',20)

print(Jake_score)


class score:
    def __init__(self,name,points):
        self.name=name
        self.points=points
    def printScore(self):
        print('Congrats {} you scored {} points this time'.format(self.name,self.points))
        

player1 =score('Mark',55)
print(player1.printScore)
