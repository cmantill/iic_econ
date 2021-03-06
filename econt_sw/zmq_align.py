from time import sleep
import zmq_controller as zmqctrl

# IP address of the zynq on the econ-testing board (localhost for the moment)
remoteIP = "localhost"

# port of the zynq waiting for daq (? fc/link) commands
daqPort = "6677"

# port of the zynq waiting for I2C config and commands (initialize/configure)
i2cPort = "5555"

daq_socket = zmqctrl.daqController(remoteIP, daqPort, "configs/init_data.yaml")
i2c_socket = zmqctrl.i2cController(remoteIP, i2cPort, "configs/init_data.yaml")

# i2c 
i2c_socket.initialize()

# daq
daq_socket.configure()
daq_socket.start()

#i2c_socket.read_config("configs/init.yaml")
i2c_socket.read_config("zmq_i2c/configs/read_align.yaml")
#print( yaml.dump(i2csocket.read_config("zmq_i2c/configs/read_align.yaml")) )

