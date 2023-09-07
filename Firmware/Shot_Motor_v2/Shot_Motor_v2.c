#include "HT66F2390.h"

#define Control _pg
#define ControlC _pgc

void stm_setup();
void delay(unsigned short dev);

void main()
{
	_wdtc = 0b10101011;
	_scc = 0b00000001;
	_hircc = 0b00000011;	// Bit 3~2 00: 8MHz, 01: 12MHz, 10: 16MHz
	
	ControlC = 0x00;
	Control = 0x00;
	
	stm_setup();
	
	while(1)
	{
		_stm0al = 500%256; _stm0ah = 500/256;
		Control = 0b00001010;
		delay(30000);
		
		Control = 0b00000000;
		delay(10000);
	}
}

void stm_setup()
{
	// stm 0
	_stm0c0 = 0b00110000;	// fH/64 => 0.125MHz => 8us
	_stm0c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm0rp = 0x02;			// 2 * 256
	
	_pcs1 = 0b00100000;		// PC6 => STP0
	_st0on = 1; _stm0al = 500%256; _stm0ah = 500/256;
}

void delay(unsigned short dev)
{
	unsigned short i, j;
	for(i=0;i<dev;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}
