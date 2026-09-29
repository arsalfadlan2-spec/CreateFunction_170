def convert_temperature(temprature, unit):
    if unit == 'C':
        return (temprature * 9/5) + 32
    elif unit == 'F':
        return (temprature - 32) * 5/9
    else:
        print("Unit tidak valid. Silakan masukkan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")