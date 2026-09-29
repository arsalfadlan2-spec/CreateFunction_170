def convert_temperature(temprature, unit):
    if unit == 'C':
        return (temprature * 9/5) + 32
    elif unit == 'F':
        return (temprature - 32) * 5/9
    else:
        print("Unit tidak valid. Silakan masukkan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")

    print("=============== Konversi suhu =================")

    input = float(input("Masukkan suhu: "))
unit = input("Masukkan unit (C/F): ")
konversi = convert_temperature(input, unit)
if unit == 'C':
    print(f"{input} derajat Celsius = {konversi} derajat Fahrenheit")
elif unit == 'F':
    print(f"{input} derajat Fahrenheit = {konversi} derajat Celsius")
else:
    print("Unit tidak valid. Silakan masukkan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")