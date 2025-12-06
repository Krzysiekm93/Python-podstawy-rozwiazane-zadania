h_ft = int(input("Podaj wysokosc w stopach: "))
h_inch = int(input("Podaj wysokosc w calach: "))

oneft_in_cm = 30.48
oneinch_in_cm = 2.54

def myconverter(ft, inch):
    ft_to_cm = ft * oneft_in_cm
    inch_to_cm = inch * oneinch_in_cm
    result = round((inch_to_cm + ft_to_cm), 2)
    return result

convertedvalue = myconverter(h_ft,h_inch)

print("{}ft and {}in is {}cm".format(h_ft, h_inch, convertedvalue))



