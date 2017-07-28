#include <Adafruit_NeoPixel.h>

void rainbowCycle() {
	for(int i=0; i<strip.numPixels(); i++){
		strip.setPixelColor(i, 255, 0, 0); //Red
		strip.show();
		delay(wait);
		strip.setPixelColor(i, 255, 127, 0); //Orange
		strip.show();
		delay(wait);
		strip.setPixelColor(i, 255, 255, 0); //Yellow
		strip.show();
		delay(wait);
		strip.setPixelColor(i, 0, 255, 0); //Green
		strip.show();
		delay(wait);
		strip.setPixelColor(i, 0, 0, 255); //Blue
		strip.show();
		delay(wait);
		strip.setPixelColor(i, 75, 0, 130); //Indigo
		strip.show();
		delay(wait);
		strip.setPixelColor(i, 148, 0, 211); //Violet
		strip.show();
		delay(wait);
	}
}