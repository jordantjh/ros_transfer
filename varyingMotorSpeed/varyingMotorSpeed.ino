
#include <ros.h>
#include <std_msgs/String.h>   //sudo chmod a+rw /dev/ttyUSB0


#define delay_fast 2
#define delay_slow_down 7
#define motor_signal 5

ros::NodeHandle  nh;
String latest_color = "red";  // default to "green" as well
int cur_stepper_val;

void messageCb( const std_msgs::String& color_published){
  latest_color = color_published.data;   // blink the led
}

ros::Subscriber<std_msgs::String> sub("command_card_t", &messageCb); // command_card_t is the topic to subscribe to

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  pinMode(motor_signal, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);   
}

//spinOnce() checks if received publication, if so, call cb()
void loop() {
  
  for(int stepperVal=0; stepperVal < 256; stepperVal++){
    nh.spinOnce();

    while(latest_color == "red"){
      delay(1);
    }
    
    analogWrite(motor_signal, stepperVal);
    if(latest_color == "green"){   // green color, usual(fast) speed motor
      delay(delay_fast);    
    }else{     // yellow color, slow down motor
      delay(delay_slow_down);      
    }
  }
    
  for(int stepperVal=255; stepperVal > 0; stepperVal--){
    nh.spinOnce();

    while(latest_color == "red"){
      delay(1);
    }
    
    analogWrite(motor_signal, stepperVal);
    
    if(latest_color == "green"){   // green color, usual(fast) speed motor
      delay(delay_fast);    
    }else{     // yellow color, slow down motor
      delay(delay_slow_down);      
    }
  }

  delay(1);
}
