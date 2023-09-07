#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned char R_Data[10];
unsigned char Data[10];
unsigned short kn = 0;

#define LED _ph0
#define LEDC _phc0

void UART_Setup();
void Read_Data();
void main()
{
	_wdtc = 0b10101011;
	
	UART_Setup();
	LEDC = 0;
	LED = 0;
	
	while(1)
	{
		if(R_Data[0] == 'O')
		{
			LED = 1;
		}
		else if(R_Data[0] == 'N')
		{
			LED = 0;
		}
	}
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
