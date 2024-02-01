// variables needed
int intCommandData;
unsigned long lngMotorTime;
int intPixelCount = 1;
int intRed = 0;
int intGreen = 0;
int intBlue = 0;
// function needed
void CameraCommands(int intCommand) {
  // counts to 25 before stopping
   while (intPixelCount < 25){
    // read intRed
    int intRed = analogRead(A0);
    // sends data from intRed back to user
    Serial.print(intRed);
    // new line so user can tell between color values
    Serial.print('\n');
    // read dblGreen
    int intGreen = analogRead(A1);
    // sends data from intGreen back to user
    Serial.print(intGreen);
    // new line so user can tell between color values
    Serial.print('\n');
    // read intBlue
    int intBlue = analogRead(A2);
    // sends data from intBlue back to user
    Serial.print(intBlue);
    // new line so user can tell between color values
    Serial.print('\n');
    // uses pin 2 for motor on the arduino
      digitalWrite(2, HIGH); 
      // what happens when motor time is up
      if(lngMotorTime == 0.06593) {
        // uses pin 2 for motor on the arduino
        digitalWrite(2, LOW);
        // set lngMotorTime to 0
        lngMotorTime = 0;
        // add 1 to intPixelCount
        intPixelCount += 1;      
      }
    }
  // turns off motor when done
  digitalWrite(2, LOW);
}
void setup() {
  // put your setup code here, to run once:
  // starts serial connection at 57600 baud
  Serial.begin(57600);
  pinMode(2, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // uses pin 2 for motor on the arduino
  if(Serial.available() > 0){
    // input for open camera
    intCommandData = Serial.read();
    // function needed
    CameraCommands(intCommandData);
    
  }
}
