import random 
captcha=("Rh7yA","ju97g","gP0h3","mn0Gl","Ril98")
ran_captcha=random.choice(captcha)
print("Enter the following captcha to check if you are a robot:",ran_captcha)
enter=str(input())
if enter==ran_captcha :
    print("You are not a robot")
else :
    print("You are a robot")

