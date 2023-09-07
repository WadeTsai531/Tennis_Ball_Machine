#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned char R_Data[10];
unsigned char Data[10];
unsigned short kn = 0;

#define IN1 _pc0
#define IN1C _pcc0
#define IN2 _pc1
#define IN2C _pcc1

#define IN3 _pc2
#define IN3C _pcc2
#define IN4 _pc3
#define IN4C _pcc3

void UART_Setup();
void Read_Data();
void stm_setup();
void delay(unsigned short dev);

void main()
{
	_wdtc = 0b10101011;
	
	UART_Setup();
	
	stm_setup();
	_st0on = 1;
	_st1on = 1;
	
	IN1C = 0;
	IN2C = 0;
	IN1 = 0;
	IN2 = 0;
	
	IN3C = 0;
	IN4C = 0;
	IN3 = 0;
	IN4 = 0;
	
	_stm0al = 300%256; _stm0ah = 300/256;  // 100
	_stm1al = 300%256; _stm1ah = 300/256;
	
	unsigned short x_value = 300;
	
	while(1)
	{
		if(R_Data[0] == 'F')
		{
			x_value = (R_Data[1] - 48)*100 + (R_Data[2] - 48)*10 + (R_Data[3] - 48);
			_stm0al = x_value%256; _stm0ah = x_value/256;
			_stm1al = x_value%256; _stm1ah = x_value/256;
				
			IN1 = 0;
			IN2 = 1;
			IN3 = 1;
			IN4 = 0;
			delay(1);
		}
		else if(R_Data[0] == 'S')
		{
			IN1 = 0;
			IN2 = 0;
			IN3 = 0;
			IN4 = 0;
			delay(1);
		}
	}
}

void stm_setup()
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
	
	_pcs1 = 0b00100000;		// PC6 => STP0
	_pds0 = 0b00000010;		// PD0 => STP1
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
