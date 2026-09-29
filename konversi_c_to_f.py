def convert_temperature(temprature, unit):
    if unit == 'C':
        return (temprature * 9/5) + 32
    else:
        return temprature