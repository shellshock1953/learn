int ledPin = 13;
int redPin = 11;
int greenPin = 9;
int bluePin = 10;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}


void loop() {
  color(255, 0, 0);
  delay(1000);
  color(0, 255, 0);
  delay(1000);
  color(0, 0, 255);
  delay(1000);
}

void color(
  unsigned char red,
  unsigned char green,
  unsigned char blue) {
    digitalWrite(redPin, red);
    digitalWrite(greenPin, green);
    digitalWrite(bluePin, blue);
}
