def convert_temperature(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    else:
        return value 
    input = int(input("Masukkan suhu: "))
    input = input("Masukkan unit (C/F): ")
    print(convert_temperature(input, input))
    
    