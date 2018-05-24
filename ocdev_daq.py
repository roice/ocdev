import Adafruit_BBIO.ADC as adc
import time

CHANNELS = ["AIN0", "AIN1", "AIN2", "AIN3", "AIN4", "AIN5", "AIN6"]
#CHANNELS = ["P9_39", "P9_40", "P9_37", "P9_38", "P9_33", "P9_36", "P9_35"]

def ocdev_daq(lock, data, len_daq, num_chs):
    if num_chs > 7:
        return False
    if len_daq <= 0:
        return False
    adc.setup()
    n = 0
    while(True):
        lock.acquire()
        t0 = time.time()
        for idx_daq in range(len_daq):
            for idx_ch in range(num_chs):
                data[idx_daq*num_chs+idx_ch] = adc.read(CHANNELS[idx_ch])
        t1 = time.time()
        #print str(t1-t0)
        n += 1
        #print str(n)
        lock.release()

