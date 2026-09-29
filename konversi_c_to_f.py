def convert_temperature(temprature, unit):
    if unit == 'C':
        return (temprature * 9/5) + 32
    elif unit == 'F':
        return (temprature - 32) * 5/9
    else:
        return "unit tidak valid "


print(convert_temperature(30, "C"))
print(convert_temperature(86, "F"))