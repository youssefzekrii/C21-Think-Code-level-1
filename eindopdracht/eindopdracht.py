print ("Welcome!")
print ("please answer in English and click space once before you answer")



a = input ("what is your name?")
print ("hello,"+ a )

b = input ("are you older than 18?")
if b == 'no' or b =='NO':
    print ("we are sorry, but you have to be older than 18")
    if b == 'yes' or b == 'YES':
        print ("thats good to hear!")

        c = input("how old are you?")
        
        print (c)
        if c==19:
            print("okay nice, im also 19 years old")
    else:
        print("okay thats nice," + a)

