#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned short R_Data[10];
unsigned short kn = 0;

#define LED _pg
#define LEDC _pgc

void UART_Setup();
void Read_Data();
void Send_Data(char data);

void delay(unsigned short dev);

void main()
{
	_wdtc = 0b10101011;
	_scc = 0b00000001;
	_hircc = 0b00000011;
	
	UART_Setup();
	
	LEDC = 0x00;
	LED &= ~0x03;
	delay(5000);
	LED |= 0x02;
	delay(5000);
	LED &= ~0x02;
	
	while(1)
	{
		/*if(R_Data[0] == 'B')
		{
			LED |= 0x01;
			delay(10);
		}
		else if(R_Data[0] == 'O')
		{
			LED &= ~0x01;
			delay(10);
		}*/
		Send_Data('A');
		Send_Data('B');
		Send_Data('C');
		Send_Data('D');
		LED |= 0x01;
		LED &= ~0x02;
		delay(10000);
		
		Send_Data('E');
		LED &= ~0x01;
		LED |= 0x02;
		delay(10000);
	}
}

DEFINE_ISR(Uart_R, 0x3c)
{
	LED |= 0x02;
	Read_Data();
    _ur0f = 0;
    LED &= ~0x02;
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
