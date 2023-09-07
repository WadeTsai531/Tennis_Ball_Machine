#include "HT66F2390.h"

#define FH 8000000
#define BR 9600

#define Trigger _pc0
#define TriggerC _pcc0
#define Echo _pc1
#define EchoC _pcc1

void UART_Setup();
void Send_Data(char data);
void ten_us_delay();
void delay(unsigned short var);
void main()
{
	_wdtc = 0b10101011;
	
	UART_Setup();
	
	_ptm0c0 = 0b00100000;
	_ptm0c1 = 0b11000001;
	_ptm0ae = 1;
	_ptm0af = 0;
	_mf0e = 1;
	_emi = 1;
	
	Trigger = 0;
	TriggerC = 0;
	EchoC = 1;
	Send_Data('K');
	delay(5000);
	
	long duration, cm;
	bit c = 0;
	while(1)
	{
		Trigger = 1;
		ten_us_delay();
		Trigger = 0;
		
		Send_Data('S');
		_ptm0al = 1; _ptm0ah = 0;
		_ptm0af = 0;
		_pt0on = 1;
		while(!c)
		{
			while(!_ptm0af)
				c = Echo;
			_ptm0af = 0;
			duration = duration + 2;
		}
		_pt0on = 0;
		Send_Data('D');
		Send_Data(duration);
		duration = 0;
		delay(10000);
	}
}

void ten_us_delay()
{
	unsigned short i;
	_ptm0al = 6; _ptm0ah = 0;
	_pt0on = 1;
	while(!_ptm0af);
	_ptm0af = 0;
	_pt0on = 0;
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

void Send_Data(char data)
{
	while(!_txif0);
	_txr_rxr0 = data;
	while(!_tidle0);
}

void delay(unsigned short var)
{
	unsigned short i, j;
	for(i=0;i<var;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}