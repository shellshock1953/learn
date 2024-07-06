#include <DS1302.h> // https://github.com/msparks/arduino-ds1302
#include <stdio.h>
#include <string.h>

// More info:
// https://fritzing.org/projects/using-the-mh-real-time-clock-modules-2
//
// Code examples:
// https://github.com/msparks/arduino-ds1302/tree/master/examples

// CE (RST), I / O (line Data aka DAT), and sCLK (serial clock)
uint8_t CE_PIN = 7;
uint8_t IO_PIN = 6;
uint8_t SCLK_PIN = 5;

char buf [50];
char day [10];

String comdata = "";
int numdata[7]= {0}, j=0, mark=0;

DS1302 rtc (CE_PIN, IO_PIN, SCLK_PIN);

void print_time(){
  Time t = rtc.time();
  memset(day,0,sizeof(day));
  snprintf(buf, sizeof(buf), "%04d-%02d-%02d %02d:%02d:%02d", t.yr, t.mon, t.date, t.hr, t.min, t.sec);
  Serial.println (buf);
}

void setup(){
  Serial.begin (9600);
  rtc.writeProtect (false);
  rtc.halt (false);
}

void loop(){
  while(Serial.available()>0){
    comdata+=char(Serial.read());
    delay(2);
    mark=1;
  }
  if(mark==1){
    Serial.print("You inputed:");
    Serial.println(comdata);
    for(int i=0;i<comdata.length();i++){
      if(comdata[i]==','||comdata[i]==0x10||comdata[i]==0x13){
        j++;
      } else {
        numdata[j]=numdata[j]*10+(comdata[i]-'0');
      }
    }
    
    Time t(numdata[0],numdata[1],numdata[2],numdata[3],numdata[4],numdata[5],numdata[6]);
    rtc.time(t);
    mark=0;j=0;
    comdata=String("");
    for(int i=0;i<7;i++)numdata[i]=0;
  }
  
  print_time();
  delay(1000);
}
