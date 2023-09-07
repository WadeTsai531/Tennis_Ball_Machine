#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned char R_Data[10];
unsigned char Data[10];
unsigned short kn = 0;

#define Control _pg
#define ControlC _pgc

#define Sensor _pa1
#define SensorC _pac1
#define SensorU _papu1

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
	_st0on = 1;
	_st1on = 1;
	_st2on = 1;
	
	ControlC = 0x00;
	Control = 0x00;

	SensorC = 1;
	SensorU = 1;
	
	_stm0al = 500%256; _stm0ah = 500/256;  // 100
	_stm1al = 200%256; _stm1ah = 200/256;  
	_stm2al = 180%256; _stm2ah = 180/256;  
	
	unsigned short shot_value, rotate_value = 0;
	
	while(1)
	{
		// Shot Motor
	    if(R_Data[0] == 'F')
		{
			shot_value = (R_Data[1] - 48)*100 + (R_Data[2] - 48)*10 + (R_Data[3] - 48);
			_stm0al = shot_value%256; _stm0ah = shot_value/256;
			Control |= 0b00001010;
			delay(1);
		}
		else if(R_Data[0] == 'S')
		{
			Control &= ~0b00001111;
			
			delay(1);
		}
		// Rotate Motor
		else if(R_Data[0] == 'R')
		{
			rotate_value = (R_Data[1] - 48)*100 + (R_Data[2] - 48)*10 + (R_Data[3] - 48);
			_stm1al = rotate_value%256; _stm1ah = rotate_value/256;	
			
			Control |= 0b00100000;
			delay(1);
		}
		else if(R_Data[0] == 'L')
		{
			rotate_value = (R_Data[1] - 48)*100 + (R_Data[2] - 48)*10 + (R_Data[3] - 48);
			_stm1al = rotate_value%256; _stm1ah = rotate_value/256;
			Control |= 0b00010000;
			delay(1);
		}
		else if(R_Data[0] == 'm')
		{
			Control &= ~0b00110000;
			delay(1);
		}
		// Raise Motor
		else if(R_Data[0] == 'U')
		{
			Control |= 0b01000000;
			delay(1);
		}
		else if(R_Data[0] == 'D')
		{
			Control |= 0b10000000;
			delay(1);
		}
		else if(R_Data[0] == 'k')
		{
			Control &= ~0b11000000;
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
	
	// stm 1
	_stm1c0 = 0b00100000;	// fH/16 => 0.5MHz => 2us
	_stm1c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm1rp = 0x02;			// 2 * 256
	_stm1al = 0x00; _stm1ah = 0x00;
	
	// stm 2
	_stm2c0 = 0b00110000;	// fH/64 => 0.125MHz => 8us
	_stm2c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm2rp = 0x0a;			// 10*256 =>> f=48hz
	_stm2al = 0x00; _stm2ah = 0x00;
	
	_pcs1 = 0b00100000;		// PC6 => STP0
	_pds0 = 0b00000010;		// PD0 => STP1
	_pfs1 = 0b10000000; 	// PF7 => STM2
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
