#include "HT66F2390.h"

#define FH 8000000
#define BR 9600
unsigned char R_Data[10];
unsigned char Data[10];
unsigned short kn = 0;

#define Control _pg
#define ControlC _pgc

#define Sensor _pa4
#define SensorC _pac4
#define SensorU _papu4

#define Sensor2 _pa3
#define Sensor2C _pac3
#define Sensor2U _papu3

#define Signal _ph0
#define SignalC _phc0
#define Signal2 _ph1
#define Signal2C _phc1

void UART_Setup();
void Read_Data();
void Timer_setup();
void Sensor_switch(char m);
void Send_Data(char data);
void delay(unsigned short dev);

char dir = 'R';
char mode = 'C';

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
	Sensor_switch('I');

	SensorC = 1;
	SensorU = 1;
	
	SignalC = 0;
	Signal = 0;
	Signal2C = 0;
	Signal2 = 0;
	
	_stm0al = 500%256; _stm0ah = 500/256;  // 100
	_stm1al = 200%256; _stm1ah = 200/256;  
	_stm2al = 190%256; _stm2ah = 190/256;
	
	unsigned short shot_value, rotate_value = 0;
	char stop_flag = 0;
	
	while(1)
	{
		// Shot Motor
	    if(R_Data[0] == 'S' & R_Data[1] == 'c' & R_Data[2] == 'r' & R_Data[3] == 'o' & R_Data[4] == 'l' & R_Data[5] == 'l')
		{
			shot_value = (R_Data[6] - 48)*100 + (R_Data[7] - 48)*10 + (R_Data[8] - 48);
			_stm0al = shot_value%256; _stm0ah = shot_value/256;
			Signal = 1; Signal2 = 1;
			Control |= 0b00001010;
			delay(1);
		}
		else if(R_Data[0] == 'S' & R_Data[1] == 't' & R_Data[2] == 'o' & R_Data[3] == 'p')
		{
			Signal = 0; Signal2 = 0;
			delay(10);
			Control &= ~0b00001111;
			delay(1);
		}
		else if(R_Data[0] == 'S' & R_Data[1] == 'h' & R_Data[2] == 'o' & R_Data[3] == 't')
		{
			_stm2al = 210%256; _stm2ah = 210/256;
			_st2on = 1;
			delay(1);
		}
		else if(R_Data[0] == 'S' & R_Data[1] == 'h' & R_Data[2] == 'S' & R_Data[3] == 'o' & R_Data[4] == 't')
		{
			_stm2al = 210%256; _stm2ah = 210/256;
			_st2on = 1;
			stop_flag = 1;
			delay(1);
		}
		else if(R_Data[0] == 'S' & R_Data[1] == 'S' & R_Data[2] == 'h' & R_Data[3] == 'o' & R_Data[4] == 't')
		{
			_stm2al = 190%256; _stm2ah = 190/256;
			_st2on = 0;
			delay(1);
		}
		// Rotate Motor
		else if(R_Data[0] == 'R' & R_Data[1] == 'i' & R_Data[2] == 'g' & R_Data[3] == 'h' & R_Data[4] == 't')
		{
			rotate_value = (R_Data[5] - 48)*100 + (R_Data[6] - 48)*10 + (R_Data[7] - 48);
			_stm1al = rotate_value%256; _stm1ah = rotate_value/256;	
			Control |= 0b00100000;
			dir = 'R';
			delay(1);
		}
		else if(R_Data[0] == 'L' & R_Data[1] == 'e' & R_Data[2] == 'f' & R_Data[3] == 't')
		{
			rotate_value = (R_Data[4] - 48)*100 + (R_Data[5] - 48)*10 + (R_Data[6] - 48);
			_stm1al = rotate_value%256; _stm1ah = rotate_value/256;
			Control |= 0b00010000;
			dir = 'L';
			delay(1);
		}
		else if(R_Data[0] == 'S' & R_Data[1] == 'R' & R_Data[2] == 'o' & R_Data[3] == 't' & R_Data[4] == 'a' & R_Data[5] == 't' & R_Data[6] == 'e')
		{
			Control &= ~0b00110000;
			//Sensor_switch('I');
			delay(1);
		}
		// Raise Motor
		else if(R_Data[0] == 'U' & R_Data[1] == 'p')
		{
			Control |= 0b01000000;
			delay(1);
		}
		else if(R_Data[0] == 'D' & R_Data[1] == 'o' & R_Data[2] == 'w' & R_Data[3] == 'n')
		{
			Control |= 0b10000000;
			delay(1);
		}
		else if(R_Data[0] == 'S' & R_Data[1] == 'R' & R_Data[2] == 'a' & R_Data[3] == 'i' & R_Data[4] == 's' & R_Data[5] == 'e')
		{
			Control &= ~0b11000000;
			delay(1);
		}
		else if(R_Data[0] == 'C' & R_Data[1] == 'a' & R_Data[2] == 'b')
		{
			_stm1al = 300%256; _stm1ah = 300/256;
			Control |= 0b00100000;
			Sensor_switch('S');
			while(!Sensor2);
			Control &= ~0b00110000;
			delay(10000);
			
			Control |= 0b00010000;
			delay(10000);
			Control &= ~0b00110000;
			delay(10000);
			Sensor_switch('I');
		}
		
		if(stop_flag & !Sensor)
		{
			stop_flag = 0;
			_st2on = 0;
			_stm2al = 185%256; _stm2ah = 185/256;
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

DEFINE_ISR(Sen, 0x08)
{
	Send_Data('S');
}

void Sensor_switch(char m)
{
	if(m == 'I')
	{
		_integ |= 0b00000100;
		_int1f = 0;
		_int1e = 1;
	}
	else
	{
		_int1e = 0;
		Sensor2C = 1;
		Sensor2U = 1;
	}
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
