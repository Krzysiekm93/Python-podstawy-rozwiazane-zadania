body_weight = float(input("podaj mase w kilogramach: "))
body_height = float(input("podaj wzrost w metrach: "))

def countBMI(weight, height):
    BMI = weight / (height * height)
    return BMI

countedBMI = round(countBMI(body_weight, body_height), 1)

if countedBMI < 18.5:
    print("Twoje BMI to {}. Masz niedowage!".format(countedBMI))
elif 18.5 <= countedBMI <= 24.9:
    print("Twoje BMI to {}. Waga prawidlowa!".format(countedBMI))
elif countedBMI >= 25:
    print("Twoje BMI to {}. Masz nadwage!".format(countedBMI))