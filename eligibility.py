ssc=int(input("Enter your SSC marks : "))
hsc=int(input("Enter your HSC marks : "))

if(ssc>=60):
    if(hsc>=70):
        print("eligible")
    else:
        print("Not Eligible because HSC Marks are less than 70.")
else:
    print("Not Eligible because SSC Marks are less than 60.")