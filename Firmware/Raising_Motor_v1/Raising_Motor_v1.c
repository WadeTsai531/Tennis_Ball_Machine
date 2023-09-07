#include "HT66F2390.h"

#define Control _pg
#define ControlC _pgc

void stm_setup();
void delay(unsigned short var);

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
		//_stm1al = 290%256; _stm1ah = 290/256;
		Control = 0b10000000;	// Down
		delay(40000);
		
		Control = 0b00000000;
		delay(10000);
		
		Control = 0b01000000;	// Up
		delay(45000);
		
		Control = 0b00000000;
		delay(10000);
	}
}

void stm_setup()
{
	// stm 1
	_stm1c0 = 0b00110000;	// fH/16 => 0.5MHz => 2us
	_stm1c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm1rp = 0x02;			// 2 * 256
	
	_pds0 = 0b00000010;		// PD0 => STP1
	_st1on = 1; _stm1al = 210%256; _stm1ah = 210/256;
}

void delay(unsigned short dev)
{
	unsigned short i, j;
	for(i=0;i<dev;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}
