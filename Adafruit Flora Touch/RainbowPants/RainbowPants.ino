#include <Adafruit_NeoPixel.h>
#include <CapacitiveSensor.h>

#define PIN 9 //Receive pin for strip
#define NUM_LEDS 9 //Number of LEDs on the strip
#define BRIGHTNESS 100 //Set brightness here

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);
CapacitiveSensor cs_9_10 = CapacitiveSensor(9, 10); //CapacitiveSensor(PIN TO GET DATA, PIN THAT RECEIVES CAP INPUT)

//Color declarations
uint32_t red = strip.Color(255, 0, 0);
uint32_t orange = strip.Color(255, 127, 0);
uint32_t yellow = strip.Color(255, 255, 0);
uint32_t green = strip.Color(0, 255, 0);
uint32_t blue = strip.Color(0, 0, 255);
uint32_t purple = strip.Color(160, 0, 255);

uint32_t rainbowColors [6] = { red, orange, yellow, green, blue, purple };

void rainbowCycle(uint8_t wait){
  for(int i=0; i<strip.numPixels(); i++){
    for(int j=0; j<6; j++) {
      strip.setPixelColor(i, rainbowColors[j]);
      strip.show();
      if(i != strip.numPixels() - 1) {
          delay(wait);
      }
      else if (i == strip.numPixels() - 1) {
        for(int k=0; k<strip.numPixels(); k++){
          strip.setPixelColor(k, rainbowColors[0]);
          strip.show();
          strip.clear();
          delay(27);
          strip.setPixelColor(k, rainbowColors[1]);
          strip.show();
          strip.clear();
          delay(27);
          strip.setPixelColor(k, rainbowColors[2]);
          strip.show();
          strip.clear();
          delay(27);
          strip.setPixelColor(k, rainbowColors[3]);
          strip.show();
          strip.clear();
          delay(27);
          strip.setPixelColor(k, rainbowColors[4]);
          strip.show();
          strip.clear();
          delay(27);
          }
        }
        }
        strip.clear();
        strip.show();
    }
  }

void setup() {
  strip.setBrightness(BRIGHTNESS);
  strip.begin();
  strip.show();
  //Serial.begin(9600);
}

void loop() {
  //long start = millis();
  //long total1 = cs_9_10.capacitiveSensor(20);

  //Serial.print(millis() - start);
  //Serial.print("\t");

  //Serial.println(total1);

  //delay(10);

  //if (total1 > 4000){
    //  rainbowCycle(150);
      //cs_9_10.reset_CS_AutoCal();
      rainbowCycle(75);
  }
//}
