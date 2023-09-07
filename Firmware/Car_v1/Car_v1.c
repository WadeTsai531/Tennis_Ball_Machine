#include "HT66F2390.h"

#define IN1 _pc0
#define IN1C _pcc0
#define IN2 _pc1
#define IN2C _pcc1

#define IN3 _pc2
#define IN3C _pcc2
#define IN4 _pc3
#define IN4C _pcc3

void delay(unsigned short dev);

void main()
{
	_wdtc = 0b10101011;
	
	IN1C = 0;
	IN2C = 0;
	IN3C = 0;
	IN4C = 0;
	
	IN1 = 0;
	IN2 = 0;
	IN3 = 0;
	IN4 = 0;
	
	while(1)
	{
		IN1 = 1;
		IN2 = 0;
		IN3 = 1;
		IN4 = 0;
		delay(60000);
		
		IN1 = 0;
		IN2 = 0;
		IN3 = 0;
		IN4 = 0;
		delay(20000);
	}
}

void delay(unsigned short dev)
{
	unsigned short i, j;
	for(i=0;i<dev;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}
