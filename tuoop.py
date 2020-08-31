#import module
import turtle
turtle.speed(1)

#creating class
class Art:
	#creating constructor
	def __init__(self,c,s):
		self.color=c
		self.shape=s
	#setting position	
	def p(self,x,y):
		turtle.penup()
		turtle.setposition(x,y)
		turtle.pendown()
	#line method		
	def line(self,length):
		turtle.forward(length)	
	#square method	
	def square(self,length):
		turtle.color(self.color)
		turtle.shape(self.shape)

		for i in range(4):
			turtle.fd(length)
			turtle.lt(90)
	#rombos method
	def rombos(self,length):
		turtle.color(self.color)
		turtle.shape(self.shape)
		for i in range(2):
			turtle.fd(length)
			turtle.left(45)
			turtle.fd(length)
			turtle.left(135)		
	#samantorik method
	def samantorik(self,length1,length2):
		for i in range(2):
			turtle.fd(length1)
			turtle.left(60)
			turtle.fd(length2)
			turtle.left(120)

#creating object and declaring attribute
karimGreen=Art("green","turtle")
karimRed=Art("red","triangle")
karimBlue=Art("blue","circle")

#method calling
karimGreen.p(100,100)
karimGreen.square(100)


karimRed.p(100,-100)
karimRed.square(100)

karimBlue.p(-100,-100)
karimBlue.square(100)


#start turtle
turtle.exitonclick()

