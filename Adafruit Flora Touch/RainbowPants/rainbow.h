#include <Adafruit_NeoPixel.h>

void rainbowCycle(wait) {
	uint32_t red = strip.Color(255, 0, 0);
	uint32_t orange = strip.Color(255, 127, 0);
	uint32_t yellow = strip.Color(255, 255, 0);
	uint32_t green = strip.Color(0, 255, 0);
	uint32_t blue = strip.Color(0, 0, 255);
	uint32_t indigo = strip.Color(75, 0, 130);
	uint32_t violet = strip.Color(148, 0, 211);

	uint32_t rainbowColors [7] = { red, orange, yellow, green, blue, indigo, violet };

	for(int i=0; i<strip.numPixels(); i++){
		for(int j=0; j<7; j++) {
			strip.setPixelColor(i, rainbowColors[j]);
			strip.show();
			delay(wait);
		}
	}
}


strip.show();
          strip.clear();
          delay(100);
          strip.show();
