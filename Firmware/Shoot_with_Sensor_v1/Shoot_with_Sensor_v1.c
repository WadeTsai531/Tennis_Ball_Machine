#include "HT66F2390.h"

#define Sensor _pa4
#define SensorC _pac4
#define SensorU _papu4

void Timer_setup();
void delay(unsigned short dev);

void main()
{
	_wdtc = 0b10101011;
	_scc = 0b00000001;
	_hircc = 0b00000011;
	
	Timer_setup();
	_st2on = 1;
	
	SensorC = 1;
	SensorU = 1;
	
	_stm2al = 210%256; _stm2ah = 210/256;
	
	while(1)
	{
		if(!Sensor)
		{
			_stm2al = 190%256; _stm2ah = 190/256;
			delay(10000);
			_stm2al = 210%256; _stm2ah = 210/256;
			delay(3000);
		}
	}
}

void Timer_setup()
{	
	// stm 2
	_stm2c0 = 0b00110000;	// fH/64 => 0.125MHz => 8us
	_stm2c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm2rp = 0x0a;			// 10*256 =>> f=48hz
	_stm2al = 0x00; _stm2ah = 0x00;
	
	_pfs1 = 0b10000000; 	// PF7 => STM2
}

void delay(unsigned short dev)
{
	unsigned short i, j;
	for(i=0;i<dev;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}
