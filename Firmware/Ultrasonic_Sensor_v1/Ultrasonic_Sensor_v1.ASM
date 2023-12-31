; Generated by holtek-gcc v3.19, Fri Oct 28 22:53:36 2022
; 
; Configuration:
;       with long instruction
;       Multi-ROM, Multi-RAM
;       bits_per_rom_unit:16
;       with mp1
;       with tbhp, address(0x9)
;          Use tabrd-const
;       
; SFR address of long-instruction arch:
;    mp0 = -1,1,0
;    mp1 = 4,3,2
;    mp2 = 14,13,12
;    tbp = 9,7,8
;    acc = 5
;    pcl = 6
;    status = 10
;    bp = 11
;    intc = 16
;       
;       
; use 'tabrdc' instead of 'tabrd'
;       

#pragma translator "holtek-gcc 4.6.4" "3.19" "build 20130711"
; Rebuild 718

ir equ [2]
mp equ [3]
sbp equ [4]
acc equ [5]
bp equ [11]
tblp equ [7]
tbhp equ [9]
status equ [10]
c equ [10].0
ac equ [10].1
z equ [10].2
ov equ [10].3
cz equ [10].6
sc equ [10].7
intc equ [16]
mduwr0 equ [59h]
mduwr1 equ [5ah]
mduwr2 equ [5bh]
mduwr3 equ [5ch]
mduwr4 equ [5dh]
mduwr5 equ [5eh]
mduwrctrl equ [5fh]

extern ra:byte
extern rb:byte
extern rc:byte
extern rd:byte
extern re:byte
extern rf:byte
extern rg:byte
extern rh:byte
extern _Crom2Prom:near
extern _Crom2PromNext:near

RAMBANK 0 @BITDATASEC, @BITDATASEC1
@HCCINIT	.section 'data'
@HCCINIT0	.section 'data'
@BITDATASEC	 .section 'data'
@BITDATASEC1	 .section 'data'

#pragma debug scope 1 1
	extern __DELAY3:near
	extern __DELAYX3:near
	extern __DELAYX6:near
	extern __DELAYY5:near
	extern __DELAYY3:near
	extern _builtin_holtek_delay_2:byte
___ptm0al equ [74]
___ptm0ah equ [75]
___ptm0c0 equ [70]
___mfi0 equ [51]
public _ten_us_delay
#pragma debug scope 2 1
#line 62 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
_ten_us_delay .section 'code'
_ten_us_delay proc
#line 64 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,6
	mov [74],a
	clr [75]
#line 65 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [70].3
_L3:
#line 66 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	snz [51].5
	jmp _L3
#line 67 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [51].5
#line 68 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [70].3
	ret
_ten_us_delay endp
#line 68 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
#pragma debug scope 1 1
___pas1 equ [334]
___u0cr1 equ [273]
___u0cr2 equ [274]
___brg0 equ [276]
___mfi5 equ [56]
___intc3 equ [19]
___intc0 equ [16]
public _UART_Setup
#pragma debug scope 3 1
#line 72 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
_UART_Setup .section 'code'
_UART_Setup proc
#line 73 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,240
	lmov [334],a
#line 74 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,128
	lmov [273],a
#line 75 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,196
	lmov [274],a
#line 76 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,12
	lmov [276],a
#line 77 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [56].0
#line 78 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [56].4
#line 79 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [19].3
#line 80 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [16].0
	ret
_UART_Setup endp
#line 80 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
#pragma debug scope 1 1
___u0sr equ [272]
___txr_rxr0 equ [275]
public _Send_Data
#pragma debug scope 4 1
#line 84 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
_Send_Data .section 'code'
_Send_Data proc
    local _Send_Data_2 db 1 dup(?)	; 0,1
	mov _Send_Data_2[0],a
#pragma debug variable 7 4 _Send_Data_2+0 "data"
_L8:
#line 85 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	lsnz [272].0
	jmp _L8
#line 86 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,_Send_Data_2[0]
	lmov [275],a
_L10:
#line 87 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	lsnz [272].1
	jmp _L10
	ret
_Send_Data endp
#line 87 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
#pragma debug scope 1 1
public _delay
#pragma debug scope 5 1
#line 91 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
_delay .section 'code'
_delay proc
public _delay_2
    local _delay_2 db 2 dup(?)	; 2,0
#pragma debug variable 10 5 _delay_2+0 "var"
#line 93 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr rb
	clr rc
_L12:
#line 93 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,rb
	sub a,_delay_2[0]
	mov a,rc
	sbc a,_delay_2[1]
	sz cz
	jmp _L11
	clr ra
_L15:
#line 95 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
;# 95 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c" 1
	nop
	inc ra
#line 94 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,ra
	sub a,25
	snz z
	jmp _L15
#line 93 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	inc rb
	sz z
	inc rc
	jmp _L12
_L11:
	ret
_delay endp
#line 93 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
#pragma debug scope 1 1
___wdtc equ [62]
___ptm0c1 equ [71]
___intc1 equ [17]
___pc equ [27]
___pcc equ [28]
public _main
#pragma debug scope 6 1
#line 16 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
IFDEF WITH_DEFAULT_STARTUP
extern _main_initial0:near
extern _main_startup:near
ENDIF

ROMBANK 0 @start
@start .section com_l 'code'
_main_startup1:
@start .section com_e 'code'
	mov a,bank _main
	mov bp,a
	jmp _main

_main .section 'code'
_main proc
    local _main_2 db 4 dup(?)
    local cr1 dbit
#pragma debug variable 13 6 _main_2+0 "duration"
#pragma debug variable 2 6 cr1 "c"
#line 17 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,171
	mov [62],a
#line 19 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	fcall _UART_Setup
#line 21 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,32
	mov [70],a
#line 22 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,193
	mov [71],a
#line 23 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [51].1
#line 24 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [51].5
#line 25 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [17].1
#line 26 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [16].0
#line 28 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [27].0
#line 29 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [28].0
#line 30 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [28].1
#line 31 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,75
	fcall _Send_Data
#line 32 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,-120
	mov _delay_2[0],a
	mov a,19
	mov _delay_2[1],a
	fcall _delay
#line 35 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr cr1
_L21:
#line 38 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [27].0
#line 39 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	fcall _ten_us_delay
#line 40 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [27].0
#line 42 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,83
	fcall _Send_Data
#line 43 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,1
	mov [74],a
	clr [75]
#line 44 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [51].5
#line 45 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	set [70].3
#line 46 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr _main_2[0]
	clr _main_2[1]
	clr _main_2[2]
	clr _main_2[3]
_L17:
	sz cr1
	jmp _L22
_L20:
#line 48 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	sz [51].5
	jmp _L23
#line 49 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr ra
	sz [27].1
	inc ra
	clr cr1
	sz ra.0
	set cr1
	jmp _L20
_L23:
#line 50 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [51].5
#line 51 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,2
	addm a,_main_2[0]
	mov a,0
	adcm a,_main_2[1]
	adcm a,_main_2[2]
	adcm a,_main_2[3]
	jmp _L17
_L22:
#line 53 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	clr [70].3
#line 54 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,68
	fcall _Send_Data
#line 55 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,_main_2[0]
	fcall _Send_Data
#line 57 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	mov a,16
	mov _delay_2[0],a
	mov a,39
	mov _delay_2[1],a
	fcall _delay
	set cr1
#line 58 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
	jmp _L21
	jmp $
_main endp

@dummy proc
	call _main
@dummy endp

#line 58 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
#pragma debug scope 1 1
#pragma debug struct_begin 42 "__intc0_bits"
#pragma debug field 21 8 0 1 "__emi" ;0,1
#pragma debug field 21 8 0 1 "__int0e" ;1,1
#pragma debug field 21 8 0 1 "__int1e" ;2,1
#pragma debug field 21 8 0 1 "__cp0e" ;3,1
#pragma debug field 21 8 0 1 "__int0f" ;4,1
#pragma debug field 21 8 0 1 "__int1f" ;5,1
#pragma debug field 21 8 0 1 "__cp0f" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 43 ""
#pragma debug field 2 42 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 43 1 ___intc0 "__intc0" 1
#pragma debug struct_begin 44 "__intc1_bits"
#pragma debug field 21 8 0 1 "__cp1e" ;0,1
#pragma debug field 21 8 0 1 "__mf0e" ;1,1
#pragma debug field 21 8 0 1 "__mf1e" ;2,1
#pragma debug field 21 8 0 1 "__ade" ;3,1
#pragma debug field 21 8 0 1 "__cp1f" ;4,1
#pragma debug field 21 8 0 1 "__mf0f" ;5,1
#pragma debug field 21 8 0 1 "__mf1f" ;6,1
#pragma debug field 21 8 0 1 "__adf" ;7,1
#pragma debug struct_end
#pragma debug union_begin 45 ""
#pragma debug field 2 44 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 45 1 ___intc1 "__intc1" 1
#pragma debug struct_begin 46 "__intc3_bits"
#pragma debug field 21 8 0 1 "__int2e" ;0,1
#pragma debug field 21 8 0 1 "__int3e" ;1,1
#pragma debug field 21 8 0 1 "__mf4e" ;2,1
#pragma debug field 21 8 0 1 "__mf5e" ;3,1
#pragma debug field 21 8 0 1 "__int2f" ;4,1
#pragma debug field 21 8 0 1 "__int3f" ;5,1
#pragma debug field 21 8 0 1 "__mf4f" ;6,1
#pragma debug field 21 8 0 1 "__mf5f" ;7,1
#pragma debug struct_end
#pragma debug union_begin 47 ""
#pragma debug field 2 46 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 47 1 ___intc3 "__intc3" 1
#pragma debug struct_begin 48 "__pc_bits"
#pragma debug field 21 8 0 1 "__pc0" ;0,1
#pragma debug field 21 8 0 1 "__pc1" ;1,1
#pragma debug field 21 8 0 1 "__pc2" ;2,1
#pragma debug field 21 8 0 1 "__pc3" ;3,1
#pragma debug field 21 8 0 1 "__pc4" ;4,1
#pragma debug field 21 8 0 1 "__pc5" ;5,1
#pragma debug field 21 8 0 1 "__pc6" ;6,1
#pragma debug field 21 8 0 1 "__pc7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 49 ""
#pragma debug field 2 48 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 49 1 ___pc "__pc" 1
#pragma debug struct_begin 50 "__pcc_bits"
#pragma debug field 21 8 0 1 "__pcc0" ;0,1
#pragma debug field 21 8 0 1 "__pcc1" ;1,1
#pragma debug field 21 8 0 1 "__pcc2" ;2,1
#pragma debug field 21 8 0 1 "__pcc3" ;3,1
#pragma debug field 21 8 0 1 "__pcc4" ;4,1
#pragma debug field 21 8 0 1 "__pcc5" ;5,1
#pragma debug field 21 8 0 1 "__pcc6" ;6,1
#pragma debug field 21 8 0 1 "__pcc7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 51 ""
#pragma debug field 2 50 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 51 1 ___pcc "__pcc" 1
#pragma debug struct_begin 52 "__mfi0_bits"
#pragma debug field 21 8 0 1 "__ptm0pe" ;0,1
#pragma debug field 21 8 0 1 "__ptm0ae" ;1,1
#pragma debug field 21 8 0 1 "__stm0pe" ;2,1
#pragma debug field 21 8 0 1 "__stm0ae" ;3,1
#pragma debug field 21 8 0 1 "__ptm0pf" ;4,1
#pragma debug field 21 8 0 1 "__ptm0af" ;5,1
#pragma debug field 21 8 0 1 "__stm0pf" ;6,1
#pragma debug field 21 8 0 1 "__stm0af" ;7,1
#pragma debug struct_end
#pragma debug union_begin 53 ""
#pragma debug field 2 52 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 53 1 ___mfi0 "__mfi0" 1
#pragma debug struct_begin 54 "__mfi5_bits"
#pragma debug field 21 8 0 1 "__ur0e" ;0,1
#pragma debug field 21 8 0 1 "__ur1e" ;1,1
#pragma debug field 21 8 0 1 "__ur2e" ;2,1
#pragma debug field 21 8 0 1 ;3,1
#pragma debug field 21 8 0 1 "__ur0f" ;4,1
#pragma debug field 21 8 0 1 "__ur1f" ;5,1
#pragma debug field 21 8 0 1 "__ur2f" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 55 ""
#pragma debug field 2 54 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 55 1 ___mfi5 "__mfi5" 1
#pragma debug struct_begin 56 "__wdtc_bits"
#pragma debug field 21 8 0 1 "__ws0" ;0,1
#pragma debug field 21 8 0 1 "__ws1" ;1,1
#pragma debug field 21 8 0 1 "__ws2" ;2,1
#pragma debug field 21 8 0 1 "__we0" ;3,1
#pragma debug field 21 8 0 1 "__we1" ;4,1
#pragma debug field 21 8 0 1 "__we2" ;5,1
#pragma debug field 21 8 0 1 "__we3" ;6,1
#pragma debug field 21 8 0 1 "__we4" ;7,1
#pragma debug struct_end
#pragma debug union_begin 57 ""
#pragma debug field 2 56 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 57 1 ___wdtc "__wdtc" 1
#pragma debug struct_begin 58 "__ptm0c0_bits"
#pragma debug field 21 8 0 3 ;0,3
#pragma debug field 21 8 0 1 "__pt0on" ;3,1
#pragma debug field 21 8 0 1 "__pt0ck0" ;4,1
#pragma debug field 21 8 0 1 "__pt0ck1" ;5,1
#pragma debug field 21 8 0 1 "__pt0ck2" ;6,1
#pragma debug field 21 8 0 1 "__pt0pau" ;7,1
#pragma debug struct_end
#pragma debug union_begin 59 ""
#pragma debug field 2 58 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 59 1 ___ptm0c0 "__ptm0c0" 1
#pragma debug struct_begin 60 "__ptm0c1_bits"
#pragma debug field 21 8 0 1 "__pt0cclr" ;0,1
#pragma debug field 21 8 0 1 "__pt0capts" ;1,1
#pragma debug field 21 8 0 1 "__pt0pol" ;2,1
#pragma debug field 21 8 0 1 "__pt0oc" ;3,1
#pragma debug field 21 8 0 1 "__pt0io0" ;4,1
#pragma debug field 21 8 0 1 "__pt0io1" ;5,1
#pragma debug field 21 8 0 1 "__pt0m0" ;6,1
#pragma debug field 21 8 0 1 "__pt0m1" ;7,1
#pragma debug struct_end
#pragma debug union_begin 61 ""
#pragma debug field 2 60 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 61 1 ___ptm0c1 "__ptm0c1" 1
#pragma debug variable 8 1 ___ptm0al "__ptm0al" 1
#pragma debug variable 8 1 ___ptm0ah "__ptm0ah" 1
#pragma debug struct_begin 62 "__u0sr_bits"
#pragma debug field 21 8 0 1 "__txif0" ;0,1
#pragma debug field 21 8 0 1 "__tidle0" ;1,1
#pragma debug field 21 8 0 1 "__rxif0" ;2,1
#pragma debug field 21 8 0 1 "__ridle0" ;3,1
#pragma debug field 21 8 0 1 "__oerr0" ;4,1
#pragma debug field 21 8 0 1 "__ferr0" ;5,1
#pragma debug field 21 8 0 1 "__nf0" ;6,1
#pragma debug field 21 8 0 1 "__perr0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 63 ""
#pragma debug field 2 62 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 63 1 ___u0sr "__u0sr" 1
#pragma debug struct_begin 64 "__u0cr1_bits"
#pragma debug field 21 8 0 1 "__tx80" ;0,1
#pragma debug field 21 8 0 1 "__rx80" ;1,1
#pragma debug field 21 8 0 1 "__txbrk0" ;2,1
#pragma debug field 21 8 0 1 "__stops0" ;3,1
#pragma debug field 21 8 0 1 "__prt0" ;4,1
#pragma debug field 21 8 0 1 "__pren0" ;5,1
#pragma debug field 21 8 0 1 "__bno0" ;6,1
#pragma debug field 21 8 0 1 "__uarten0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 65 ""
#pragma debug field 2 64 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 65 1 ___u0cr1 "__u0cr1" 1
#pragma debug struct_begin 66 "__u0cr2_bits"
#pragma debug field 21 8 0 1 "__teie0" ;0,1
#pragma debug field 21 8 0 1 "__tiie0" ;1,1
#pragma debug field 21 8 0 1 "__rie0" ;2,1
#pragma debug field 21 8 0 1 "__wake0" ;3,1
#pragma debug field 21 8 0 1 "__adden0" ;4,1
#pragma debug field 21 8 0 1 "__brgh0" ;5,1
#pragma debug field 21 8 0 1 "__rxen0" ;6,1
#pragma debug field 21 8 0 1 "__txen0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 67 ""
#pragma debug field 2 66 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 67 1 ___u0cr2 "__u0cr2" 1
#pragma debug variable 8 1 ___txr_rxr0 "__txr_rxr0" 1
#pragma debug variable 8 1 ___brg0 "__brg0" 1
#pragma debug struct_begin 68 "__pas1_bits"
#pragma debug field 21 8 0 1 "__pas10" ;0,1
#pragma debug field 21 8 0 1 "__pas11" ;1,1
#pragma debug field 21 8 0 1 "__pas12" ;2,1
#pragma debug field 21 8 0 1 "__pas13" ;3,1
#pragma debug field 21 8 0 1 "__pas14" ;4,1
#pragma debug field 21 8 0 1 "__pas15" ;5,1
#pragma debug field 21 8 0 1 "__pas16" ;6,1
#pragma debug field 21 8 0 1 "__pas17" ;7,1
#pragma debug struct_end
#pragma debug union_begin 69 ""
#pragma debug field 2 68 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 69 1 ___pas1 "__pas1" 1
#line 16 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Ultrasonic_Sensor_v1\Ultrasonic_Sensor_v1.c"
@code .section at 0 'code'
	clr bp
	jmp _main_startup1


; 
; Generated by holtek-gcc v3.19, Fri Oct 28 22:53:36 2022
; Rebuild 718
; end of file
