#include "HT66F2390.h"

#define LED _pg
#define LEDC _pgc

void delay(unsigned short var);
void main()
{
	_wdtc = 0b10101011;
	
	LEDC = 0x00;
	LED = 0x00;
	
	while(1)
	{
		LED |= 0x03;
		delay(5000);
		LED &= ~0x03;
		delay(5000);
	}
}

void delay(unsigned short var)
{
	unsigned short i, j;
	for(i=0;i<var;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}