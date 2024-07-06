#include <Keypad.h> // https://github.com/Chris--A/Keypad
const byte ROWS=4;
const byte COLS=4;
char keys [ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {2,3,4,5};
byte colPins[COLS] = {6,7,8,9};
byte ledPin = 10;
boolean blink = false;

Keypad keypad = Keypad(makeKeymap(keys),rowPins,colPins,ROWS,COLS);
void setup() {
  pinMode(ledPin, OUTPUT);  
  digitalWrite(ledPin, HIGH);
  Serial.begin(9600);
  keypad.addEventListener(keypadEvent);
}


void loop() {
  char key = keypad.getKey();
  if (key != NO_KEY) {
    Serial.println(key);
  }
  if (blink){
    digitalWrite(ledPin,!digitalRead(ledPin));
    delay(100);
  }
}


void keypadEvent(KeypadEvent key){
  switch(keypad.getState()){
    case PRESSED:
      switch(key){
        case '#': digitalWrite(ledPin,!digitalRead(ledPin)); break;
        case '*': digitalWrite(ledPin,!digitalRead(ledPin)); break;    
      } break;
    case RELEASED:
      switch(key){
        case '*': digitalWrite(ledPin,!digitalRead(ledPin)); break;
        blink=false;
      } break;
    case HOLD:
      switch(key){
        case '*': blink=true; break;
      } break;
    
  }
}

