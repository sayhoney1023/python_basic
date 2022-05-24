import fah_converter

celsius = float(input('섭씨 온도를 입력 : '))
fahrenheit = fah_converter.convert_c_to_f (celsius)
print("{}C = {}F".format(celsius,fahrenheit))
