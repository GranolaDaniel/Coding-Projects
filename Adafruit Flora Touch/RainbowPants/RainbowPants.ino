#include <Adafruit_NeoPixel.h>
#include <CapacitiveSensor.h>

#define PIN 9 //Receive pin for strip
#define NUM_LEDS 9 //Number of LEDs on the strip
#define BRIGHTNESS 255 //Set brightness here

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

void colorPop(){
       for(int m=0; m<strip.numPixels(); m++){
          strip.setPixelColor(m, rainbowColors[0]);
  }
      strip.show();
      strip.clear();
      delay(500);
      strip.show();
      for(int m=0; m<strip.numPixels(); m++){
          strip.setPixelColor(m, rainbowColors[1]);
  }
      strip.show();
      strip.clear();
      delay(500);
      strip.show();
      for(int m=0; m<strip.numPixels(); m++){
          strip.setPixelColor(m, rainbowColors[2]);
  }
      strip.show();
      strip.clear();
      delay(500);
      strip.show();
      for(int m=0; m<strip.numPixels(); m++){
          strip.setPixelColor(m, rainbowColors[3]);
  }
      strip.show();
      strip.clear();
      delay(500);
      strip.show();
      for(int m=0; m<strip.numPixels(); m++){
          strip.setPixelColor(m, rainbowColors[4]);
  }
      strip.show();
      strip.clear();
      delay(500);
      strip.show();
      for(int m=0; m<strip.numPixels(); m++){
          strip.setPixelColor(m, rainbowColors[5]);
  }
      strip.show();
      strip.clear();
      delay(500);
      strip.show();
 } 


void setup() {
  strip.setBrightness(BRIGHTNESS);
  strip.begin();
  strip.show();
}

void loop() {
      rainbowCycle(75);
      colorPop();
      
      delay(30000);
}
