def topping():
    toppings = str("")
    top=str("")
    while(top!=str("done")):
        top=str(input("Add a topping/Enter done if complete..."))
        if(top!=str("done")):
            toppings+=str(", ")
            toppings+=(top)
    
    if (toppings==str("")):
        return (str("no toppings."))
    else:
        return (toppings)        
    
def pizza():
    size=input("Small, medium, or large? ")
    p=str((size," pizza with ",topping()))
    print("You have ordered a: ",p,". Place another order or enter done.")
    return p
    
def dressing():
    dressing=str(input("What kind of dressing would you like? "))
    return dressing
    
def salad():
    salad_type=str(input("Would you like a house salad or a greek salad? "))
    s=str((salad_type,"salad with ", dressing()," dressing"))
    print("You have ordered a: ",s,". Place another order or enter done.")
    return s
    
def select_meal():
    order=""
    ps=str("")
    while(ps!=str("done")):
        ps=str(input("Hello, would you like to order pizza or salad? "))
        if(ps==str("pizza")):
            order+=(" a ") 
            order+=(pizza()) 
        elif(ps==str("salad")):   
            order+=(" a ")
            order+=(salad()) 
    print("Thank You! Your order has been placed! You have ordered",order)
        


select_meal()
    