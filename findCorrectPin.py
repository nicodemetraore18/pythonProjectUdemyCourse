def pin_is_ok(pins_digit):
    if pins_digit[0]


for pins in range(0,10000):
    this_pin = str(pins).zfill(5)
    pins_digit={}
    pins_digit[first]=int(this_pin[0])
    pins_digit[second]=int(this_pin[1])
    pins_digit[third]=int(this_pin[2])
    pins_digit[fourth]=int(this_pin[2])
    pins_digit[fifth]=int(this_pin[3])
     
    if pin_is_ok(pins_digit):
        print(pins)