def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours:")
    pay = input("Enter Pay:")
    # end assignment
    try:
        h = float(hrs)
        p = float(pay)
    except:
        print ("Error, please enter numeric input")
        quit()
    if h > 40 :
        print("OverTime")
        reg = h * p
        opt = (h - 40.0) * (p *.5)
        print(reg,opt)
        x = reg + opt
    else:
        print("Regular") 
        x = (h * p)
    print("Pay:",x)
## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
