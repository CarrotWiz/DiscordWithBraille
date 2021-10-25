#include <LEDMatrixDriver.hpp>

const uint8_t LEDMATRIX_CS_PIN = 9;
const int LEDMATRIX_SEGMENTS = 4;
const int LEDMATRIX_WIDTH    = LEDMATRIX_SEGMENTS * 8;
LEDMatrixDriver lmd(LEDMATRIX_SEGMENTS, LEDMATRIX_CS_PIN);

void setup() {
  Serial.begin(9600); // REPLACE 9600 WITH YOUR BAUD
  Serial.setTimeout(1);
  lmd.setEnabled(true);
  lmd.setIntensity(0);
}

String readString; 

// lights up the 32x8 LED board given a 256 character binary string
void lightUpBoard(String str) {
  lmd.display();
  int pos = 0;
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 32; j++) {
      lmd.setPixel(j, i, str.charAt(pos) == '1');
      pos++;
    }
  }
}

void loop() {
  lmd.display(); // clears LED display
  while (Serial.available()) {
    if (Serial.available() > 0) { // recieved a string from serial
      char c = Serial.read();
      readString += c; 
    }
    if(readString.length() == 256){ // once the full 256 length string is read
      lightUpBoard(readString);
      readString = "";
    }
  }
}
