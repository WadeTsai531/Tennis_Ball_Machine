#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned char R_Data[10];
unsigned char Data[10];
unsigned short kn = 0;

#define Control _pg
#define ControlC _pgc
#define Signal _pa3
#define SignalC _pac3

void UART_Setup();
void Read_Data();
void Timer_setup();
void delay(unsigned short dev);
void main()
{
	_wdtc = 0b10101011;
	_scc = 0b00000001;
	_hircc = 0b00000011;	// Bit 3~2 00: 8MHz, 01: 12MHz, 10: 16MHz
	
	UART_Setup();
	Timer_setup();
	
	ControlC = 0x00;
	SignalC = 0;
	Signal = 0;
	
	_st0on = 1;
	_stm0al = 500%256; _stm0ah = 500/256;  // 100
	while(1)
	{
		if(R_Data[0] == 'S' & R_Data[1] == 'c' & R_Data[2] == 'r' & R_Data[3] == 'o' & R_Data[4] == 'l' & R_Data[5] == 'l')
		{
			shot_value = (R_Data[6] - 48)*100 + (R_Data[7] - 48)*10 + (R_Data[8] - 48);
			_stm0al = shot_value%256; _stm0ah = shot_value/256;
			Control |= 0b00001010;
			delay(1);
		}
		else if(R_Data[0] == 'S' & R_Data[1] == 't' & R_Data[2] == 'o' & R_Data[3] == 'p')
		{
			Control &= ~0b00001111;
			
			delay(1);
		}
	}	
}

void Timer_setup()
{
	// stm 0
	_stm0c0 = 0b00100000;	// fH/16 => 0.5MHz => 2us
	_stm0c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm0rp = 0x02;			// 2 * 256
	_stm0al = 0x00; _stm0ah = 0x00;
	
	_pcs1 = 0b00100000;		// PC6 => STP0
}

DEFINE_ISR(Uart_R, 0x3c)
{
    Read_Data();
    _ur0f = 0;
}

void UART_Setup()
{
    _pas1 = 0b11110000;	// PA6 => Rx PA7 => Tx
	_u0cr1 = 0b10000000;
	_u0cr2 = 0b11000100;
	_brg0 = FH/((unsigned long)64*BR) - 1;
	_ur0e = 1;
	_ur0f = 0;
	_mf5e = 1;
	_emi = 1;
}

void Read_Data()
{
	while(_ridle0 == 0);
	R_Data[kn] = _txr_rxr0;
	if(R_Data[kn] == '/' || kn > 9)	kn = 0;
	else kn++;
}

void delay(unsigned short dev)
{
	unsigned short i, j;
	for(i=0;i<dev;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}