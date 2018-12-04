# -*- coding: utf-8 -*-
"""
Created on Thursday April 12, 2018
Last revised: April 23, 2018

@author: Pairode Kim Jaroensri

###############################################################################
This script monitors the Cryomech compressor with the option to turn on/off
the compressor through serial communuication.

The ability to turn on/off has NOT been tested.
###############################################################################
"""
import minimalmodbus, time, struct
# Constants
minimalmodbus.BAUDRATE = 115200
minimalmodbus.TIMEOUT = 2
port = '/dev/ttyS0'

YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'


def interpret_float(data):
    """ Takes in a list of 2 int16 returned from Instrument.read_registers(),
        then interpret it as one float32 according to Cryomech's documentations.
    """
    temp = bytearray()
    for i in data:
        temp += i.to_bytes(2,'big')
    final = bytearray()
    final.append(temp[1])
    final.append(temp[0])
    final.append(temp[3])
    final.append(temp[2])
    return struct.unpack('f', final)[0]

def operating_state(code):
    if code == 0:
        return "Idling: ready to start"
    if code == 2:
        return "Starting"
    if code == 3:
        return "Running"
    if code == 5:
        return "Stopping"
    if code == 6:
        return "Error Lockout"
    if code == 7:
        return "Error"
    if code == 8:
        return "Helium Cool Down"
    if code == 9:
        return "Power related Error"
    if code == 15:
        return "Recovered from Error"
    return "Unable to interpret status code: " + str(code)

def warning_state(fl_code):
    code = round(fl_code)
    if code == 0:
        return "No warnings"
    if code == -1:
        return "Coolant IN running High"
    if code == -2:
        return "Coolant IN running Low"
    if code == -4:
        return "Coolant OUT running High"
    if code == -8:
        return "Coolant OUT running Low"

    if code == -16:
        return "Oil running High"
    if code == -32:
        return "Oil running Low"
    if code == -64:
        return "Helium running High"
    if code == -128:
        return "Helium running Low"

    if code == -256:
        return "Low Pressure running High"
    if code == -512:
        return "Low Pressure running Low"
    if code == -1024:
        return "High Pressure running High"
    if code == -2048:
        return "High Pressure running Low"

    if code == -4096:
        return "Delta Pressure running High"
    if code == -8192:
        return "Delta Pressure running Low"

    if code == -131072:
        return "Static Pressure running High"
    if code == -262144:
        return "Static Pressure running Low"

    if code == -524288:
        return "Cold head motor Stall"

    return "[Unable to interpret warning code: " + str(fl_code) + "]"

def error_state(fl_code):
    code = round(fl_code)
    if code == 0:
        return "No Errors"
    if code == -1:
        return "Coolant IN High"
    if code == -2:
        return "Coolant IN Low"
    if code == -4:
        return "Coolant OUT High"
    if code == -8:
        return "Coolant OUT Low"

    if code == -16:
        return "Oil High"
    if code == -32:
        return "Oil Low"
    if code == -64:
        return "Helium High"
    if code == -128:
        return "Helium Low"

    if code == -256:
        return "Low Pressure High"
    if code == -512:
        return "Low Pressure Low"
    if code == -1024:
        return "High Pressure High"
    if code == -2048:
        return "High Pressure Low"

    if code == -4096:
        return "Delta Pressure High"
    if code == -8192:
        return "Delta Pressure Low"

    if code == -16384:
        return "Motor Current Low"
    if code == -32768:
        return "Three Phase Error"
    if code == -65536:
        return "Power Supply Error"

    if code == -131072:
        return "Static Pressure High"
    if code == -262144:
        return "Static Pressure Low"

    return "[Unable to interpret error code: " + str(fl_code) + "]"

def pressure_unit(code):
    if code == 0:
        return "PSI"
    if code == 1:
        return "Bar"
    if code == 2:
        return "kPa"
    return "[Unable to interpret pressure unit code: " + str(code) + "]"

def temp_unit(code):
    if code == 0:
        return "F"
    if code == 1:
        return "C"
    if code == 2:
        return "K"
    return "[Unable to interpret temperature unit code: " + str(code) + "]"

def turn_on_compressor(device):
    device.write_register(1, 0x0001, functioncode=6)
    print("Turn on command sent.")

def turn_off_compressor(device):
    device.write_register(1, 0x00FF, functioncode=6)
    print("Turn off command sent.")

def monitor(device):
    p_unit = device.read_register(29, functioncode=4)
    p_unit = pressure_unit(p_unit)

    t_unit = device.read_register(30, functioncode=4)
    t_unit = temp_unit(t_unit)

    state = device.read_register(1, functioncode=4)
    state_text = operating_state(state)

    warning = device.read_registers(3, 2, functioncode=4)
    warning = interpret_float(warning)
    warning_text = YELLOW + warning_state(warning) + WHITE

    error = device.read_registers(5, 2, functioncode=4)
    error = interpret_float(error)
    error_text = RED + error_state(error) + WHITE

    if error == 0:
        coolant_in = device.read_registers(7, 2, functioncode=4)
        coolant_in = '{0:.2f}'.format(interpret_float(coolant_in)) + ' ' + t_unit

        coolant_out = device.read_registers(9, 2, functioncode=4)
        coolant_out = '{0:.2f}'.format(interpret_float(coolant_out)) + ' ' + t_unit

        oil_temp = device.read_registers(11, 2, functioncode=4)
        oil_temp = '{0:.2f}'.format(interpret_float(oil_temp)) + ' ' + t_unit

        he_temp = device.read_registers(13, 2, functioncode=4)
        he_temp = '{0:.2f}'.format(interpret_float(he_temp)) + ' ' + t_unit

        low_pr = device.read_registers(15, 2, functioncode=4)
        low_pr = '{0:.2f}'.format(interpret_float(low_pr)) + ' ' + p_unit

        high_pr = device.read_registers(19, 2, functioncode=4)
        high_pr = '{0:.2f}'.format(interpret_float(high_pr)) + ' ' + p_unit

        delta_avg = device.read_registers(23, 2, functioncode=4)
        delta_avg = '{0:.2f}'.format(interpret_float(delta_avg)) + ' ' + p_unit

        motor_current = device.read_registers(25, 2, functioncode=4)
        motor_current = '{0:.2f}'.format(interpret_float(motor_current)) + ' Amps'

        hours = device.read_registers(27, 2, functioncode=4)
        hours = '{0:.2f}'.format(interpret_float(hours)) + ' Hrs'

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('Operating State:', state_text)
        print('Coolant IN:\t', coolant_in)
        print('Coolant OUT:\t', coolant_out)
        print('Oil temp:\t', oil_temp)
        print('Helium temp:\t', he_temp)
        print('Low Pressure:\t', low_pr)
        print('High Pressure:\t', high_pr)
        print('Delta Average:\t', delta_avg)
        print('Motor Current:\t', motor_current)
        print('Up time:\t', hours)
        if warning != 0:
            print(warning_text)
    else:
        print(error_text)

def main():
    print("\n=============================================")
    print("     Cryomech Compressor Monitor v.1.416     ")
    print("=============================================")

    device = minimalmodbus.Instrument(port, 16)
    while 1:
        print("\nEnter the corresponding number:")
        print("    0 - Start monitoring the compressor.")
        print("    1 - Turn the compressor on/off.")
        print("    2 - Exit")
        choice = input('> ')
        try:
            choice = int(choice)
        except:
            pass
        if choice == 0:
            print("Press Ctl+C any time to return to main menu.")
            time.sleep(2)
            while 1:
                try:
                    monitor(device)
                    time.sleep(2)
                except KeyboardInterrupt:
                    break
        elif choice == 1:
            print("\nEnter the corresponding number:")
            print("    0 - Turn OFF the compressor.")
            print("    1 - Turn ON the compressor.")
            print("    Anything else to cancel.")
            choice, choice2 = input('> '), None
            try:
                choice = int(choice)
                if chocie == 0:
                    print("Selected: Turn OFF")
                    choice2 = input("Enter 'y' to confirm, anything else to cancel: ")
                elif choice == 1:
                    print("Selected: Turn ON")
                    choice2 = input("Enter 'y' to confirm, anything else to cancel: ")
                # Else: the number entered is neither 0 nor 1; cancel the operation.
            except:
                pass
            if choice2 != 'y':
                choice = None
            if choice == 0:
                turn_off_compressor(device)
            elif choice == 1:
                turn_on_compressor(device)
            else:
                print('Operation canceled.')
            time.sleep(2)

        elif choice == 2:
            break
        else:
            print('Invalid choice. Try again.')
            time.sleep(1)

if __name__ == '__main__':
    main()
