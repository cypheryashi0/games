print("Welcome to the love calculator !")
name1 = input("What is your name ? \n")
name2 = input("What is thier name ?\n")
name = name1 + name2
lowercase_count_name = name.lower()
count_t = lowercase_count_name.count("t")
count_r = lowercase_count_name.count("r")
count_u = lowercase_count_name.count("u")
count_e = lowercase_count_name.count("e")
count_l = lowercase_count_name.count("l")
count_o = lowercase_count_name.count("o")
count_v = lowercase_count_name.count("v")
count1 = count_t + count_r + count_u + count_e
count2 = count_l + count_o + count_v + count_e
love_percent = str(count1) + str(count2)
lovepercent_int = int(love_percent)
ily = ("your love percent is " + love_percent )
if lovepercent_int<=10 or lovepercent_int >= 90:
    print(f"{ily}% You have a coke mentos relationship !")
elif  lovepercent_int<=50 and lovepercent_int>= 40:
    print(f"{ily}% You have a fine relationship.")  
else:
    print(ily +"%"+ " It's fine !")    




 

