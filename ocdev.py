# Odor compass device
# sample three gas sensors and send data to ground station via UDP protocol
# written by Roice Luo for Jia-Ying~
# 2017-02-25

from multiprocessing import Process, Lock, Array
from ocdev_daq import ocdev_daq
from ocdev_comm import ocdev_comm

NUM_SENSORS = 3
LEN_DAQ = 100

if __name__ == '__main__':

    # memory to store DAQ data
    daq_data = Array('f', range(NUM_SENSORS*LEN_DAQ))
    # lock to access DAQ data
    lock_daq_data = Lock()

    # create DAQ process
    p_daq = Process(target=ocdev_daq, args=(lock_daq_data, daq_data, LEN_DAQ, NUM_SENSORS))
    # create Comm process
    p_comm = Process(target=ocdev_comm, args=(lock_daq_data, daq_data, LEN_DAQ, NUM_SENSORS))

    # start processes
    p_daq.start()
    p_comm.start()

    # end processes
    p_comm.join()
    p_daq.join()
