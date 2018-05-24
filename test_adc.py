import Adafruit_BBIO.ADC as adc

print "start to test"
adc.setup()
adc.read("AIN1")
print "end test"
