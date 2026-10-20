def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("* ",end="")
        print()
#output:
'''
* * *
* * *
* * *
'''

def pattern2(n):
    for i in range(n):
        for j in range(i):
            print("* ",end="")     
        print()    

#output:
'''
*
* *
* * *
* * * *
'''


def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()    
#output:
'''
1
1 2
1 2 3
1 2 3 4
'''


def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

#output:
'''
1
1 2
1 2 3
1 2 3 4
'''

def pattern5(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print("*",end="")
        print()    


#output:
'''
*****
****
***
**
*
'''

def pattern6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j,end="")
        print()    
'''
12345
1234
123
12
1
'''

#pattern7 -pyramid pattern
def pattern7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()


#pattern8 - pyramid pattern with numbers
def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(2*n-1-2*i):
            print("*",end=" ")
        print()

'''
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          * 
'''          


def pattern9(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")    
        for j in range(2*i+1):
            print("*",end=" ")   
        print()

    for i in range(n):
        for j in range(i):
           print(" ",end=" ")
        for j in range(2*n-1-2*i):
          print("*",end=" ")   

        print()       

#output:
'''
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
'''        
# #half diamond patttern
# def pattern10(n):
#     for  i in range(n):
#         for j in range(i):
#             print("*",end=" ")
#         print()     
#     for i in  range(n):
#         for j in range(n-i):
#             print("*",end=" ")
#         print()    
# #output:it is another way to write        

'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
#half diamond pattern want to print is another way
def pattern10(n):

    for i in range(2*n - 1):

        if i < n:
            star = i + 1
        else:
            star = 2*n - i - 1

        for j in range(star):
            print("*", end=" ")

        print()

#pattern 11
def pattern11(n):
   for i in range(n):
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(i+1):
        print(start,end=" ")
        start=1-start
    print( )    


#output:
'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
'''    

# def pattern12(n):
#     for i in  range(n):

#         for j in range(i+1):

#             print(j,end=" ")

#         for j in range(2 * n - 2 * i - 2):

#             print(" ",end="")

#         for j in range(i,-1,-1):

#             print(j,end=" ")

#         print() 

# def test_case(l,pattern):
#     for i in range(l):
#         n=int(input("Enter your number"))
#         pattern(n)
# test_case(2,pattern12)        



def pattern12(n):
    for i in range(n):
        for j in range(i+1):
            print(j, end=" ")

        for j in range(2 * (n - i - 1)):
            print(" ", end=" ")

        for j in range(i, -1, -1):
            print(j, end=" ")

        print()

#output:
'''
0                     0
0 1                 1 0
0 1 2             2 1 0
0 1 2 3         3 2 1 0
0 1 2 3 4     4 3 2 1 0
0 1 2 3 4 5 5 4 3 2 1 0         
'''


def pattern13(n):
    num=1

    for i in range(n):
        
        for  j in range(i+1):
            print(num,end=" ")
            num+=1
        print()    
        
         
def pattern14(n):
    
    for i in range(n):
        ch='A'
        for j in range(i+1):
            print(ch,end=" ")
            ch=chr(ord(ch)+1)

        print()   

#output:
'''
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
'''         


def pattern15(n):
    
    for i in range(n):
        ch='A'
        
        for j in range(n-i):
            print(ch,end=" ")
            ch=chr(ord(ch)+1)
            
        print()    
'''
A B C D E 
A B C D 
A B C 
A B 
A         
'''            

def pattern16(n):
    for i in range(n):
        ch=chr(ord('A')+i)
        for j in range(i+1):
            print(ch,end=" ")
        print()    



def pattern17(n):
    for i in range(n):
        ch='A'
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            if j<((2*i)+1)/2:
              print(ch,end=" ") 
              ch=chr(ord(ch)+1)
            else:
                ch=chr(ord(ch)-2)
                print(ch,end=" ")
                ch=chr(ord(ch)+1)
        for j in range(n-i-1):
            print(" ",end='')  
        print()     


def pattern18(n):
    for i in range(n):
        ch=chr(ord('E')-i)
        for j in  range(i+1):
            print(ch,end=" ")
            ch=chr(ord(ch)+1)
            
        print()


def pattern19(n):
    space=0
    for i in range(n):

        for j in range(n-i):
            print("*",end=" ")

        for j in range(space):
            print(" ",end=" ")
            

        for j in range(n-i):
            print("*",end=" ") 
        # space+=2 
        space+=2
        print() 
    space=2*n-2 
    for i in range(n):
       
        for j in range(i+1):
            print("*",end=" ")

        for j in range(space):
            print(" ",end=" ")

        for j in range(i+1):
            print("*",end=" ")   

        space-=2            
        
        print()
                   
'''
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * * 
'''


#this is one type


# def pattern20(n):
#     space=2*n-2
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end=" ")
#         for j in range(space):
#             print(" ",end=" ") 
#         for j in range(i+1):
#             print("*",end=" ")   
#         space-=2
#         print()
#     space=2*n-8    
#     for i in range(n):
#         for j in range(n-i-1):
#             print("*",end=" ")
#         for j in range(space):
#             print(" ",end=" ")
#         for j in range(n-i-1):
#             print("*",end=" ") 
#         space+=2
#         print()


#another type 




def pattern20(n):

    space=2*n-2
    for i in range(1,2*n):
    #stars
        star=i
        if i>n:
            star=2*n-i
        for j in range(star):
            print("*",end=" ")
          
    #spaces    
        for j in range(space):
            print(" ",end=" ") 
        
        for j in range(star):
            print("*",end=" ")

        print()
    
        if i>=n:
            space+=2
        else:    
           space-=2
    

#output:
'''
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 *
'''     

def pattern21(n):
    for i in range(1,n+1): #or (n)
        for j in range(1,n+1): #or (n)
            if i==1 or  j==1 or i==n or j==n: #or i==0 or j==0 i==n-1 or j==n-1
                print("*",end=" ")
            else:
                print(" ",end=" ")    
        print()




def pattern22(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top=i
            left=j
            right=(2*n-2)-j
            down=(2*n-2)-i
            print(n-min(min(top,down),min(left,right)),end=" ")


        print()
'''


5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
'''
'''
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
'''








 
# def test_case(l,pattern):
#     for i in range(l):
#         n=int(input("Enter your number :"))
#         pattern(n)
# test_case(2,pattern22)




 def pattern20( n):

        space=2*n-2

        for i in range(2*n-1):
            
            if i<n:

                star=i+1
            else:

                star=2*n-i-1

            

            for j in range(star):

                print("*",end="")

            for j in range(space):

                print(" ",end="")

            for j in range(star):

                print("*",end="")

            if i<n:

                space-=2


            else:
                space+=2 

            print()                     

pattern20(5)
            
