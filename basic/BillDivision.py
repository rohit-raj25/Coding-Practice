# Question: Bill Division
# Link: https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    # Write your code here
    sum=0
    for  i in range(len(bill)):
        if i!=k:
            sum+=bill[i]
    amount=sum//2
    
    #print(sum)
    if amount==b:
        print("Bon Appetit")
        
    else:
        print(b-amount)


