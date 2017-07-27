#include <Adafruit_NeoPixel.h>

#define PIN 9
#define NUM_LEDS 10
#define BRIGHTNESS //Decide brightness

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, Neo_GRB + NEO_KHZ800);

void setup() {
	strip.setBrightness(BRIGHTNESS);
	strip.begin();
	strip.show();
}

void loop() {
	//On touch, each pix loops through colors for a set time
	//For loop iterating each pix through a color of the rainbow
	//?On touch from two inputs, do a different pattern?
}