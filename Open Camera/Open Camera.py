from time import sleep
import time
import glob, os
import psutil
import lupa

# these functions are placed up here due to errors

# mod prompt is up here so it can be global
strModPrompt = input("Do you want to use mods, y = yes, n = no: ");
if strModPrompt == "y":
    # library for mods and process vm call needed for mods
    from lupa import LuaRuntime
    lua = LuaRuntime()

    # The mod file must be in your home directory and must be called note_data_to_instrument_mod.lua
    lua.execute(r'''dofile("Open_Camera_Mod.lua")''')
    
    # get the mod global envirorment
    globals = lua.globals()
    
    # Mod Notice and Name
    strModNoticeAndName = lua.globals().strNoticeAndName
    print("You are using a mod: \n")
    print(strModNoticeAndName)
    
if strModPrompt == "n":
    print("You decided not to use a mod")

# Raspberry Pi function
def RaspberryPi():
    #spi must be enabled in raspi-config
    
    # calls gpio module
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(5, GPIO.OUT)

    intPixelCount = 1
    
    # input for Bit 0 mode
    strCameraMode = input("press 1 then enter to take a picture:");
    # header needed for file
    picture = open(strPictureName, "a")
    picture.write("P3")
    picture.write("\n")
    picture.write("5")
    picture.write("\n")
    picture.write("5")
    picture.write("\n")
    picture.write("255")
    picture.write("\n")
    picture.close()
    # if digital is selected for bit 0 it goes to the digital bit 0 function
    if strCameraMode == "1":
        if strModPrompt == "y":
            # functions for reading each primary color, writes data for each pixel to file and amt of time to use motor
            while intPixelCount < 26:
                RaspberryPiRedMod();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                RaspberryPiGreenMod();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                RaspberryPiBlueMod();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                intPixelCount += 1
                GPIO.output(5, GPIO.HIGH)
                time.sleep(0.06593)
                GPIO.output(5, GPIO.LOW)
            
        if strModPrompt == "n":
            # functions for reading each primary color, writes data for each pixel to file and amt of time to use motor
            while intPixelCount < 26:
                RaspberryPiRed();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                RaspberryPiGreen();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                RaspberryPiBlue();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                intPixelCount += 1
                GPIO.output(5, GPIO.HIGH)
                time.sleep(0.06593)
                GPIO.output(5, GPIO.LOW)
                
    # validation    
    else:
        print("Good Bye")
        exit();
        
    print("Good Bye")
    exit();

# Raspberry Pi Red function
def RaspberryPiRed():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # tells driver what ADC it is using
    adc = MCP3008()
    # Reads from channel 0 of the ADC
    value = adc.read0( channel = 0 )
    #needed to reliably read the data
    sleep(1)
    value = int(value)
    value = str(value)
    # test case
    print(value)
    
    # writes value to .txt file
    picture = open(strPictureName, "a")
    picture.write(value)
    picture.close()

    # Returns value
    return value;
        
# Raspberry Pi Green function
def RaspberryPiGreen():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 1 of the ADC
    value = adc.read1( channel = 1 )
    value = int(value)
    value = str(value)
    # test case
    print(value)
    
    # writes value to .txt file
    picture = open(strPictureName, "a")
    picture.write(value)
    picture.close()

    # Returns value
    return value;
        
# Raspberry Pi Blue function
def RaspberryPiBlue():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 2 of the ADC
    value = adc.read2( channel = 2 )
    value = int(value)
    value = str(value)
    # test case
    print(value)
    
    # writes value to .txt file
    picture = open(strPictureName, "a")
    picture.write(value)
    picture.close()

    # Returns value
    return value;

# Raspberry Pi Red Mod function
def RaspberryPiRedMod():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # tells driver what ADC it is using
    adc = MCP3008()
    # Reads from channel 0 of the ADC
    value = adc.read0( channel = 0 )
    #needed to reliably read the data
    sleep(1)
    value = int(value)
    # results from each mod function
    result = globals.RedFunction(value)
    result = str(result)
    # test case
    print(result)
    
    # writes value to .txt file
    picture = open(strPictureName, "a")
    picture.write(result)
    picture.close()

    # Returns value
    return result;
        
# Raspberry Pi Green Mod function
def RaspberryPiGreenMod():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 1 of the ADC
    value = adc.read1( channel = 1 )
    value = int(value)
    # results from each mod function
    result = globals.GreenFunction(value)
    result = str(result)
    # test case
    print(result)
    
    # writes value to .txt file
    picture = open(strPictureName, "a")
    picture.write(result)
    picture.close()

    # Returns value
    return result;
        
# Raspberry Pi Blue Mod function
def RaspberryPiBlueMod():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 2 of the ADC
    value = adc.read2( channel = 2 )
    value = int(value)
    # results from each mod function
    result = globals.BlueFunction(value)
    result = str(result)
    # test case
    print(value)
    
    # writes value to .txt file
    picture = open(strPictureName, "a")
    picture.write(result)
    picture.close()

    # Returns value
    return result;

# Arduino function
def Arduino():
    intPixelCount = 1
    
    # input for Bit 0 mode
    strCameraMode = input("press 1 then enter to take a picture:");
    # header needed for file
    picture = open(strPictureName, "a")
    picture.write("P3")
    picture.write("\n")
    picture.write("5")
    picture.write("\n")
    picture.write("5")
    picture.write("\n")
    picture.write("255")
    picture.write("\n")
    picture.close()
    # if digital is selected for bit 0 it goes to the digital bit 0 function
    if strCameraMode == "1":
        # tells arduino to take pictures
        arduinoDriver.write(b'1')
        if strModPrompt == "y":
            # functions for reading each primary color and writes data for each pixel to file
            while intPixelCount < 26:
                ArduinoRedMod();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                ArduinoGreenMod();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                ArduinoBlueMod();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                intPixelCount += 1
        if strModPrompt == "n":
            # functions for reading each primary color and writes data for each pixel to file
            while intPixelCount < 26:
                ArduinoRed();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                ArduinoGreen();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                ArduinoBlue();
                picture = open(strPictureName, "a")
                picture.write("\n")
                picture.close()
                intPixelCount += 1
        
                
    # validation    
    else:
        print("Good Bye")
        exit();
        
    # goes back to the menu
    print("Good Bye")
    exit();
        
# Arduino Red function
def ArduinoRed():
    
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()

    picture = open(strPictureName, "a")
    picture.write(value)
    picture.close()

    print(value)
    return value;

# Arduino Green function
def ArduinoGreen():
    
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()

    picture = open(strPictureName, "a")
    picture.write(value)
    picture.close()

    print(value)
    return value;

# Arduino Blue function
def ArduinoBlue():
    
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()

    picture = open(strPictureName, "a")
    picture.write(value)
    picture.close()

    print(value)
    return value;

# Arduino Red Mod function
def ArduinoRedMod():
    
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()
    # turns string into int
    value2 = int(float(value))
    # results from each mod function
    result = globals.RedFunction(value2)

    picture = open(strPictureName, "a")
    picture.write(str(result))
    picture.close()

    print(result)
    return result;

# Arduino Green Mod function
def ArduinoGreenMod():
    
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()
    # turns string into int
    value2 = int(float(value))
    # results from each mod function
    result = globals.GreenFunction(value2)

    picture = open(strPictureName, "a")
    picture.write(str(result))
    picture.close()

    print(result)
    return result;

# Arduino Blue Modfunction
def ArduinoBlueMod():
    
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()
    # turns string into int
    value2 = int(value)
    # results from each mod function
    result = globals.BlueFunction(value2)

    picture = open(strPictureName, "a")
    picture.write(str(result))
    picture.close()

    print(result)
    return result;
# new line to seperate instances
# Copyright and license notice
print("\n");
print("Copyright (C) 2023 Daniel Hanrahan");
print("\n");
print("This program is free software: you can redistribute it and/or modify it under the terms of the GNU");
print("General Public License as published by the Free Software Foundation, either version 3 of the License, or");
print("(at your option) any later version.");
print("\n");
print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without");
print("even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.");
print("See the GNU General Public License for more details.");
print("\n");
print("You should have received a copy of the GNU General Public License along with this program. If not, see");
print("<https://www.gnu.org/licenses/>.");
print("\n");

# asks user if he has arduino port
arduinoDriverPortOption = input("Do you have an arduino port y = yes,n = no:")
# What heppens when yes is chosen
if arduinoDriverPortOption == "y":
    
    # calls usb ports
    import serial
    
    # asks for the port for arduino
    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");
    
    # calls the Arduino driver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600, timeout=.1)
    
    # asks for name of picture
    strPictureName = input("What do you want to name your picture with path where you want to put it (case sensitive):")
    # appends .ppm extension
    strPictureName += '.ppm'
    # creates file of that name
    picture = open(strPictureName, "x")
    Arduino()
    
if arduinoDriverPortOption == "n":
    print("you are now using raspberry pi option");
    # asks for name of picture
    strPictureName = input("What do you want to name your picture with path where you want to put it (case sensitive):")
    # appends .ppm extension
    strPictureName += '.ppm'
    # creates file of that name
    picture = open(strPictureName, "x")
    RaspberryPi()
    
    
else:
    print("Good bye")
    exit()

print("Good Bye")
exit();
