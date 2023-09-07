#include "HT66F2390.h"

#define LED _pg0
#define LEDC _pgc0

#define Signal _pc0
#define SignalC _pcc0
#define SignalU _pcpu0

void main()
{
	_wdtc = 0b10101011;
	
	LEDC = 0;
	SignalC = 1;
	SignalU = 1;
	
	LED = 0;
	
	while(1)
	{
		if(Signal == 1)
		{
			LED = 1;
		}
		else
		{
			LED = 0;
		}
	}
}