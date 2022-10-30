#Solution of the problem 1:----
#Lenght of a string without using len()

g="sourajit" #String input
def FindLength(l): #Declaration of Function
    x=0
    for i in l:
        x=x+1
    return x
print(FindLength(g))

#Solution of the problem 2:----
#Index of element in List withot using index()

l=[1,4,5] #Declaration of the list

#Declaration of the Function with arguments inlcude list and number
def GetIndex(l, num): 
    for i in range(len(l)):
        if l[i] == num:
            return i
print(GetIndex(l, 5))

#Solution of the problem 3:----
#print hostname and ip address

import socket #socket library to get hostname and ip address

computer_host = socket.gethostname() #fetches hostname 
IP_Address= socket.gethostbyname(computer_host) #gets ip address

print(f"hostname of computer: ", computer_host)
print(f"ip address of computer: ", IP_Address)

#Solution of the problem 4:----
#Solution to Shutdown Computer by Python


#Solution of the problem 5:----
l = [3.5, 6.56, 4,5,"sudh" , "ineuron" , 'fsda bootcamp 2.0'] #Input List
def MultiValue(l): #Declaration of Function
    num=1
    for i in l:
        if type(i) == float or type(i) == int:
            num=num*i
    print(num)        
MultiValue(l)

