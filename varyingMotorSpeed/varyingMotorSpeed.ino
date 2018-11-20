#define delay_fast 2
#define delay_slow_down 7

void setup() {
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int stepperVal=0; stepperVal < 256; stepperVal++){
    analogWrite(trans_base_out, stepperVal);
    //delay(delay_fast);
    delay(delay_slow_down);
  }

  for(int stepperVal=255; stepperVal > 0; stepperVal--){
    analogWrite(trans_base_out, stepperVal);
    //delay(delay_fast);
    delay(delay_slow_down);
  }

  delay(2);
}
