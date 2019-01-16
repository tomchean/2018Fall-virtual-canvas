/*
  This example configures LinkIt 7697 to act as a simple GATT server with 1 characteristic.
  The GATT server notifies changes of the characteristic periodically.
  
  created Aug 2017
*/
#include <LBLE.h>
#include <LBLEPeriphral.h>

// Define a simple GATT service with only 1 characteristic
LBLEService counterService("19B10010-E8F2-537E-4F6C-D104768A1214");
LBLECharacteristicInt counterCharacteristic1("19B10011-E8F2-537E-4F6C-D104768A1214", LBLE_READ | LBLE_WRITE);
LBLECharacteristicInt counterCharacteristic2("19B10012-E8F2-537E-4F6C-D104768A1214", LBLE_READ | LBLE_WRITE);

const int usr_btn1 = 6; // USR BTN pin is P6 
const int usr_btn2 = 3; // USR BTN pin is P6 

 
void pin_change1(void) 
{ 
    Serial.println("button pressed"); 
    if(LBLEPeripheral.connected())
    {
      // increment the value
      const int newValue = counterCharacteristic1.getValue() + 1;
      counterCharacteristic1.setValue(newValue);

      // broadcasting value changes to all connected central devices
      LBLEPeripheral.notifyAll(counterCharacteristic1);
    }
} 
void pin_change2(void) 
{ 

    Serial.println("button pressed"); 
    if(LBLEPeripheral.connected())
    {
      // increment the value
      const int newValue = counterCharacteristic2.getValue() + 1;
      counterCharacteristic2.setValue(newValue);

      // broadcasting value changes to all connected central devices
      LBLEPeripheral.notifyAll(counterCharacteristic2);
    }
} 
 

void setup() {

  attachInterrupt(usr_btn1, pin_change1, RISING); 
  attachInterrupt(usr_btn2, pin_change2, CHANGE); 



  //Initialize serial and wait for port to open:
  Serial.begin(9600);

  // Initialize BLE subsystem
  LBLE.begin();
  while (!LBLE.ready()) {
    delay(100);
  }
  Serial.println("BLE ready");


  // configure our advertisement data.
  // In this case, we simply create an advertisement that represents an
  // connectable device with a device name
  LBLEAdvertisementData advertisement;
  advertisement.configAsConnectableDevice("GATT");

  // Configure our device's Generic Access Profile's device name
  // Ususally this is the same as the name in the advertisement data.
  LBLEPeripheral.setName("GATT Test");

  // Add characteristics into counterService
  counterService.addAttribute(counterCharacteristic1);
  counterService.addAttribute(counterCharacteristic2);
  
  // Add service to GATT server (peripheral)
  LBLEPeripheral.addService(counterService);

  // start the GATT server - it is now 
  // available to connect
  LBLEPeripheral.begin();
  Serial.print("Device Address = [");
  Serial.print(LBLE.getDeviceAddress());
  Serial.println("]");

  
  // start advertisment
  LBLEPeripheral.advertise(advertisement);
}

void loop() {
  delay(1000);
  Serial.print("conected=");
  Serial.println(LBLEPeripheral.connected());

}
