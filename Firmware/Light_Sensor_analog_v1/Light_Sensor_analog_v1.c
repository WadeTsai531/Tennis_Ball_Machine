#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned short R_Data[10];
unsigned short kn = 0;

void UART_Setup();
void Read_Data();
void Send_Data(char data);

unsigned short data_L, data_H;

void delay(unsigned short dev);

void main()
{
	_wdtc = 0b10101011;
	_scc = 0b00000001;
	_hircc = 0b00000011;
	
	// ADC Setup
	_pcs0 = 0b00000011;
	_sadc0 = 0b00110000;
	_sadc1 = 0b00000101;
	_sadc2 = 0b00000000;
	_ade = 1; _emi = 1;
	
	UART_Setup();
	
	Send_Data('S');
	Send_Data('T');
	
	unsigned short t = 0;
	short count = 0;
	while(1)
	{
		if(count >= 500)
		{
			count = 0;
			_start = 1;
			_start = 0;
			Send_Data(data_L);
			Send_Data(data_H);
			Send_Data('/');
		}
		delay(10);
		count++;
	}
}

DEFINE_ISR(ISR_ADC, 0x1c)
{
	data_L = _sadol;
	data_H = _sadoh;
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
	while(!_ridle0);
	R_Data[kn] = _txr_rxr0;
	if(R_Data[kn] == '/' || kn > 9) kn = 0;
	else kn++;
}

void Send_Data(char data)
{
	while(!_txif0);
	_txr_rxr0 = data;
	while(!_tidle0);
}

void delay(unsigned short dev)
{
	unsigned short i, j;
	for(i=0;i<dev;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}
