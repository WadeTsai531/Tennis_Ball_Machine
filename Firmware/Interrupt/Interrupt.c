#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned char R_Data[10];
unsigned char Data[10];
unsigned short kn = 0;

#define Control _pg
#define ControlC _pgc

#define Sensor _pd4
#define SensorC _pdc4
#define SensorU _pdpu4

char dir = 'R';

void UART_Setup();
void Read_Data();
void Send_Data(char data);
void stm_setup();
void delay(unsigned short dev);

void main()
{
	_wdtc = 0b10101011;
	_scc = 0b00000001;
	_hircc = 0b00000011;
	
	UART_Setup();
	
	_integ = 0b00000001;
	_int0f = 0;
	_int0e = 1;
	
	stm_setup();
	_st2on = 1;
	
	ControlC = 0x00;
	Control = 0x00;
		
	SensorC = 1;
	SensorU = 1;
	
	Send_Data('S');
	Send_Data('t');
	Send_Data('a');
	Send_Data('r');
	Send_Data('t');
	unsigned short x_value = 230;
	_stm2al = x_value%256; _stm2ah = x_value/256;  // 100
	
	while(!Sensor)
	{
		Control |= 0b01000000;
	}
	delay(20000);
	
	Control &= ~0b11000000;
	delay(10000);
	
	while(1)
	{
		Control |= 0b10000000;
		delay(20000);
		
		Control &= ~0b11000000;
		delay(10000);
		
		Control |= 0b01000000;
		delay(20000);
		
		Control &= ~0b11000000;
		delay(10000);
	}
}

void stm_setup()
{
	// stm 0
	_stm0c0 = 0b00100000;	// fH/16 => 0.5MHz => 2us
	_stm0c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm0rp = 0x02;			// 2 * 256
	_stm0al = 0x00; _stm0ah = 0x00;
	
	_pcs1 = 0b00100000;		// PC6 => STP0
	
	// stm 2
	_stm2c0 = 0b00100000;	// fH/16 => 0.5MHz => 2us
	_stm2c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm2rp = 0x02;			// 2 * 256
	_stm2al = 0x00; _stm2ah = 0x00;
	
	_pfs1 = 0b10000000; 	// PF7 => STM2
}

DEFINE_ISR(Uart_R, 0x3c)
{
    Read_Data();
    _ur0f = 0;
}

DEFINE_ISR(Sen, 0x04)
{
	Send_Data(dir);
	if(dir == 'R')
		dir = 'L';
	else
		dir = 'R';
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
