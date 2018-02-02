#!/usr/bin/python

###Comments
##Script Comments

#Title of the Program : Python Language Fundamentals
#Author of the program : Sanjeev Kumar
#Date and Time of Creation : 02/02/2018 16:00 GMT
#Version of the program : 0.1
#Description : This is Sanjeev's first attemp at understanding Pythong language fundamentals.
#The version on the python used by Sanjeev is 2.7.6

###Import Statements
###Local Functions
###Global Variables

### Python statements
##Code Comments

# I/O statement to print Hello World on screen.
# Print text can be included either in single or double quote
# no line delimiter required
# This is only one of the many styles of print statements.

# version 2.x
print "Hello World"

#version 3.x
#print ("Hello World")

### labels/variables : Primitive Types (Uniary Type)

##Numeric Type
a=10   #int
b=3.99 #float
c=2+4j #complex

##Non Numeric Type
d="Sanjeev" #str
e=True      #bool
f=False     #bool
g=None      #NoneType

#to print pass comma seperated labels/literlas to print statement

print "------------------Style 1 --------------------"
print a
print type(a)
print b
print type(b)
print c
print type(c)
print d
print type(d)
print e
print type(e)
print f
print type(f)
print g
print type(g)

print "------------------Style 2 --------------------"
print a,type(a)
print b,type(b)
print c,type(c)
print d,type(d)
print e,type(e)
print f,type(f)
print g,type(g)

print "------------------Style 3 --------------------"
print "Numeric Type Integer Value:",a,type(a)
print "Numeric Type Float Value:",b,type(b)
print "Numeric Type Complex Value:",c,type(c)
print "Non Numeric Type String Value:",d,type(d)
print "Non Numeric Type Bollean Value:",e,type(e)
print "Non Numeric Type  Boolean Value:",f,type(f)
print "Non Numeric Type  NoneType Value:",g,type(g)

#Formatted Type Print
#Unformatted Type print
#if any message is to be printed as is
#if any value is to be printed as is 
#if both message and value has to be printed

print "------------------unformatted print of message --------------------"
print "welcome to python programing" #unformatted print of message

print "------------------formatted print of message --------------------"
print "%s" % "welcome to python programming" # fomratted print of message

print "------------------unformatted print of value --------------------"
print a #unformatted print of value

print "------------------formatted print of value --------------------"
print "%i" % a   #formatted print of value

print "------------------unformatted print of message and value --------------------"
print "The value of label a is",a #unformatted print of both message and value

print "------------------formatted print of message and value --------------------"
print "The value of label a is %i" % a #fomratted print for both message and value


### operators - Arithmetic operator, logical operator..etc
### its the type of value that finally decides what operator will do

print "------------------type of value that finally decides what operator will do --------------------"
i=10
k=20
print i+k
print '10'+'20'

### Delimiter & Assignment

# multi statement in single line

e=20
r=30

print e,r
l=30;t=80  # python supports multi statements in single line with help of delimiter
print l,t

# multi label multi value assigment ..the python way

v,u=6,4;
print v,u

# Enclose string in single or double quote or mix of both

print "hi Sanjeev"
print 'hi Sanjeev'
print "It's Mine"
print 'It"s Wrong'


