#include "HT66F2390.h"

#define Servo_deg_0 256 // fsys=16MHz 128, fsys=8MHz 64

#define Sensor _ph1
#define SensorC _phc1
#define SensorPU _phpu1

#define Control _pg
#define ControlC _pgc

void timer_setup();
void servo_setup();

void delay(unsigned short var);

void main()
{
	_wdtc = 0b10101011;
	
	_scc = 0b00000001;
	_hircc = 0b00001111; // 8MHz
	
	SensorC = 1;
	SensorPU = 1;
	ControlC = 0x00;
	
	Control = 0b00000110;
	
	// Servo Setup
	servo_setup(); // 80~180~280
	while(1)
	{
		_stm2al = 210%256; _stm2ah = 210/256;
		delay(20000);
		
		_stm2al = 180%256; _stm2ah = 180/256;
		delay(10000);
		
		_stm2al = 80%256; _stm2ah = 80/256;
		delay(20000);
		
		_stm2al = 180%256; _stm2ah = 180/256;
		delay(10000);
		
		/*while(Sensor != 0);
		_st0on = 0;
		delay(10000);
		
		_st0on = 1;
		delay(2000);*/
	}
}

void timer_setup()
{
	_stm0c0 = 0b00110000; // Pause Contorl: Run, Clock: fh/64
	_stm0c1 = 0b10101000; // Mode: PWM, Output Control: Active High
	_stm0rp = 0x0a; // 10*256 =>> f=48hz
	
	// stm 1
	_stm1c0 = 0b00100000;	// fH/16 => 0.5MHz => 2us
	_stm1c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm1rp = 0x02;			// 2 * 256
	
	// stm 2
	_stm2c0 = 0b00110000;	// fH/16 => 0.5MHz => 2us
	_stm2c1 = 0b10101000;	// PWM mode, Active High, CCRA => duty
	_stm2rp = 0x0a;			// 2 * 256
}

void servo_setup()
{
	timer_setup();
	_pcs1 = 0b00100010; // PC6 => STM0, PC4 => PTM1
	_pds0 = 0b00000010;		// PD0 => STP1
	_pfs1 = 0b10000000; 	// PF7 => STM2
	
	_st0on = 1; _stm0al = Servo_deg_0%256; _stm0ah = Servo_deg_0/256;
	_st1on = 1; _stm1al = 300%256; _stm1ah = 300/256;
	_st2on = 1; _stm2al = 180%256; _stm2ah = 180/256;
}

void delay(unsigned short var)
{
	unsigned short i, j;
	for(i=0;i<var;i++)
		for(j=0;j<25;j++)
			GCC_NOP();
}
