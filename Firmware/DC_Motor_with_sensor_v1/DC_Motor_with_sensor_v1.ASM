; Generated by holtek-gcc v3.19, Tue Apr 12 19:16:37 2022
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
___stm0c0 equ [78]
___stm0c1 equ [79]
___stm0rp equ [84]
___stm0al equ [82]
___stm0ah equ [83]
___pcs1 equ [338]
public _stm_setup
#pragma debug scope 2 1
#line 142 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
_stm_setup .section 'code'
_stm_setup proc
#line 144 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,32
	mov [78],a
#line 145 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,168
	mov [79],a
#line 146 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,2
	mov [84],a
#line 147 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [82]
	clr [83]
#line 149 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,32
	lmov [338],a
	ret
_stm_setup endp
#line 149 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
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
#line 159 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
_UART_Setup .section 'code'
_UART_Setup proc
#line 160 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,240
	lmov [334],a
#line 161 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,128
	lmov [273],a
#line 162 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,196
	lmov [274],a
#line 163 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,12
	lmov [276],a
#line 164 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [56].0
#line 165 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [56].4
#line 166 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [19].3
#line 167 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [16].0
	ret
_UART_Setup endp
#line 167 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
#pragma debug scope 1 1
___u0sr equ [272]
___txr_rxr0 equ [275]
public _Read_Data
#pragma debug scope 4 1
#line 171 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
_Read_Data .section 'code'
_Read_Data proc
_L5:
#line 172 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	lsnz [272].3
	jmp _L5
#line 173 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,_kn[0]
	mov rb,a
	mov a,_kn[1]
	mov rc,a
	lmov a,[275]
	mov ra,a
	mov a,low offset _R_Data
	add a,rb
	mov mp,a
	mov a,high offset _R_Data
	adc a,rc
	mov sbp,a
	mov a,ra
	mov ir,a
#line 174 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,ra
	sub a,47
	sz z
	jmp _L6
	mov a,9
	sub a,rb
	mov a,0
	sbc a,rc
	sz c
	jmp _L7
_L6:
	clr _kn[0]
	clr _kn[1]
	jmp _L3
_L7:
#line 175 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,1
	add a,rb
	mov _kn[0],a
	mov a,0
	adc a,rc
	mov _kn[1],a
_L3:
	ret
_Read_Data endp
#line 175 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
#pragma debug scope 1 1
public _Uart_R
#pragma debug scope 5 1
#line 153 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
rombank 0 @Uart_R_code
@Uart_R_code .section at 60 'code'
	mov r1,a
	mov a,bp
	clr bp
	jmp _Uart_R
ROMBANK 0 _Uart_R
#pragma debug scope 1 1
@dummy60 proc
	call _Uart_R
@dummy60 endp
#pragma debug scope 6 1
_Uart_R .section 'code'
_Uart_R proc
	mov r2,a
	mov a, status
	mov r3,a
	mov a,mp
	mov r4,a
	mov a,sbp
	mov r5,a
	mov a,tblp
	mov r6,a
	mov a,tbhp
	mov r7,a
#line 154 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	fcall _Read_Data
#line 155 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [56].4
	mov a,r2
	mov bp,a
	mov a,r3
	mov status,a
	mov a,r4
	mov mp,a
	mov a,r5
	mov sbp,a
	mov a,r6
	mov tblp,a
	mov a,r7
	mov tbhp,a
	tabrdc acc
	mov a,r1
	reti
_Uart_R endp

#line 155 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
#pragma debug scope 1 1
public _delay
#pragma debug scope 7 1
#line 179 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
_delay .section 'code'
_delay proc
public _delay_2
    local _delay_2 db 2 dup(?)	; 2,0
#pragma debug variable 10 7 _delay_2+0 "dev"
#line 181 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr rb
	clr rc
_L15:
#line 181 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,rb
	sub a,_delay_2[0]
	mov a,rc
	sbc a,_delay_2[1]
	sz cz
	jmp _L14
	clr ra
_L18:
#line 183 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
;# 183 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c" 1
	nop
	inc ra
#line 182 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,ra
	sub a,25
	snz z
	jmp _L18
#line 181 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	inc rb
	sz z
	inc rc
	jmp _L15
_L14:
	ret
_delay endp
#line 181 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
#pragma debug scope 1 1
___wdtc equ [62]
___pcc equ [28]
___pc equ [27]
___pf equ [36]
___pfc equ [37]
___pdc equ [31]
___pdpu equ [32]
___pd equ [30]
public _main
#pragma debug scope 8 1
#line 29 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
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
#line 30 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,171
	mov [62],a
#line 32 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	fcall _UART_Setup
#line 34 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	fcall _stm_setup
#line 35 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [78].3
#line 37 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [28].0
#line 38 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [28].1
#line 39 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].0
#line 40 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].1
#line 42 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [28].2
#line 43 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [28].3
#line 44 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].2
#line 45 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].3
#line 47 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [36].0
#line 48 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [37].0
#line 50 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [31].0
#line 51 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [32].0
#line 55 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,144
	mov [82],a
	mov a,1
	mov [83],a
_L24:
#line 60 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,144
	mov [82],a
	mov a,1
	mov [83],a
#line 61 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [27].0
#line 62 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].1
#line 63 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,16
	mov _delay_2[0],a
	mov a,39
	mov _delay_2[1],a
	fcall _delay
#line 65 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].0
#line 66 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].1
#line 67 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,16
	mov _delay_2[0],a
	mov a,39
	mov _delay_2[1],a
_L25:
#line 75 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	fcall _delay
#line 69 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	sz [30].0
	jmp _L27
#line 72 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,24
	mov [82],a
	mov a,1
	mov [83],a
#line 73 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].0
#line 74 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [27].1
#line 75 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,1
	mov _delay_2[0],a
	clr _delay_2[1]
	jmp _L25
_L27:
#line 78 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].0
#line 79 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].1
#line 80 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,-120
	mov _delay_2[0],a
	mov a,19
	mov _delay_2[1],a
_L26:
#line 88 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	fcall _delay
#line 82 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	sz [30].0
	jmp _L28
#line 85 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,210
	mov [82],a
	clr [83]
#line 86 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	set [27].0
#line 87 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].1
#line 88 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,1
	mov _delay_2[0],a
	clr _delay_2[1]
	jmp _L26
_L28:
#line 91 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].0
#line 92 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	clr [27].1
#line 93 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	mov a,32
	mov _delay_2[0],a
	mov a,78
	mov _delay_2[1],a
	fcall _delay
#line 138 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
	jmp _L24
	jmp $
_main endp

@dummy proc
	call _main
@dummy endp

#line 138 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
#pragma debug scope 1 1
public _kn
@HCCINIT	.section 'data'
#line 7 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
@HCCINIT_kn .section 'data'
_kn label byte
#pragma debug variable 10 1 _kn "kn"
	db 0
@ROMDATA_BASE .section inpage 'code'
	db 0
@HCCINIT_kn .section 'data'
	db 0
@ROMDATA_BASE .section inpage 'code'
	db 0
@HCCINIT_kn .section 'data'
#line 6 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
public _Data
@HCCINIT0_Data .section 'data'
_Data	db 10 dup(0)
#pragma debug array 42 8 10 1
#pragma debug variable 42 1 _Data "Data"

@HCCINIT .section 'data'
#line 5 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
public _R_Data
@HCCINIT0_R_Data .section 'data'
_R_Data	db 10 dup(0)
#pragma debug variable 42 1 _R_Data "R_Data"

@HCCINIT .section 'data'
#pragma debug struct_begin 43 "__intc0_bits"
#pragma debug field 21 8 0 1 "__emi" ;0,1
#pragma debug field 21 8 0 1 "__int0e" ;1,1
#pragma debug field 21 8 0 1 "__int1e" ;2,1
#pragma debug field 21 8 0 1 "__cp0e" ;3,1
#pragma debug field 21 8 0 1 "__int0f" ;4,1
#pragma debug field 21 8 0 1 "__int1f" ;5,1
#pragma debug field 21 8 0 1 "__cp0f" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 44 ""
#pragma debug field 2 43 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 44 1 ___intc0 "__intc0" 1
#pragma debug struct_begin 45 "__intc3_bits"
#pragma debug field 21 8 0 1 "__int2e" ;0,1
#pragma debug field 21 8 0 1 "__int3e" ;1,1
#pragma debug field 21 8 0 1 "__mf4e" ;2,1
#pragma debug field 21 8 0 1 "__mf5e" ;3,1
#pragma debug field 21 8 0 1 "__int2f" ;4,1
#pragma debug field 21 8 0 1 "__int3f" ;5,1
#pragma debug field 21 8 0 1 "__mf4f" ;6,1
#pragma debug field 21 8 0 1 "__mf5f" ;7,1
#pragma debug struct_end
#pragma debug union_begin 46 ""
#pragma debug field 2 45 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 46 1 ___intc3 "__intc3" 1
#pragma debug struct_begin 47 "__pc_bits"
#pragma debug field 21 8 0 1 "__pc0" ;0,1
#pragma debug field 21 8 0 1 "__pc1" ;1,1
#pragma debug field 21 8 0 1 "__pc2" ;2,1
#pragma debug field 21 8 0 1 "__pc3" ;3,1
#pragma debug field 21 8 0 1 "__pc4" ;4,1
#pragma debug field 21 8 0 1 "__pc5" ;5,1
#pragma debug field 21 8 0 1 "__pc6" ;6,1
#pragma debug field 21 8 0 1 "__pc7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 48 ""
#pragma debug field 2 47 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 48 1 ___pc "__pc" 1
#pragma debug struct_begin 49 "__pcc_bits"
#pragma debug field 21 8 0 1 "__pcc0" ;0,1
#pragma debug field 21 8 0 1 "__pcc1" ;1,1
#pragma debug field 21 8 0 1 "__pcc2" ;2,1
#pragma debug field 21 8 0 1 "__pcc3" ;3,1
#pragma debug field 21 8 0 1 "__pcc4" ;4,1
#pragma debug field 21 8 0 1 "__pcc5" ;5,1
#pragma debug field 21 8 0 1 "__pcc6" ;6,1
#pragma debug field 21 8 0 1 "__pcc7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 50 ""
#pragma debug field 2 49 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 50 1 ___pcc "__pcc" 1
#pragma debug struct_begin 51 "__pd_bits"
#pragma debug field 21 8 0 1 "__pd0" ;0,1
#pragma debug field 21 8 0 1 "__pd1" ;1,1
#pragma debug field 21 8 0 1 "__pd2" ;2,1
#pragma debug field 21 8 0 1 "__pd3" ;3,1
#pragma debug field 21 8 0 1 "__pd4" ;4,1
#pragma debug field 21 8 0 1 "__pd5" ;5,1
#pragma debug field 21 8 0 1 "__pd6" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 52 ""
#pragma debug field 2 51 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 52 1 ___pd "__pd" 1
#pragma debug struct_begin 53 "__pdc_bits"
#pragma debug field 21 8 0 1 "__pdc0" ;0,1
#pragma debug field 21 8 0 1 "__pdc1" ;1,1
#pragma debug field 21 8 0 1 "__pdc2" ;2,1
#pragma debug field 21 8 0 1 "__pdc3" ;3,1
#pragma debug field 21 8 0 1 "__pdc4" ;4,1
#pragma debug field 21 8 0 1 "__pdc5" ;5,1
#pragma debug field 21 8 0 1 "__pdc6" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 54 ""
#pragma debug field 2 53 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 54 1 ___pdc "__pdc" 1
#pragma debug struct_begin 55 "__pdpu_bits"
#pragma debug field 21 8 0 1 "__pdpu0" ;0,1
#pragma debug field 21 8 0 1 "__pdpu1" ;1,1
#pragma debug field 21 8 0 1 "__pdpu2" ;2,1
#pragma debug field 21 8 0 1 "__pdpu3" ;3,1
#pragma debug field 21 8 0 1 "__pdpu4" ;4,1
#pragma debug field 21 8 0 1 "__pdpu5" ;5,1
#pragma debug field 21 8 0 1 "__pdpu6" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 56 ""
#pragma debug field 2 55 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 56 1 ___pdpu "__pdpu" 1
#pragma debug struct_begin 57 "__pf_bits"
#pragma debug field 21 8 0 1 "__pf0" ;0,1
#pragma debug field 21 8 0 1 "__pf1" ;1,1
#pragma debug field 21 8 0 1 "__pf2" ;2,1
#pragma debug field 21 8 0 1 "__pf3" ;3,1
#pragma debug field 21 8 0 1 "__pf4" ;4,1
#pragma debug field 21 8 0 1 "__pf5" ;5,1
#pragma debug field 21 8 0 1 "__pf6" ;6,1
#pragma debug field 21 8 0 1 "__pf7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 58 ""
#pragma debug field 2 57 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 58 1 ___pf "__pf" 1
#pragma debug struct_begin 59 "__pfc_bits"
#pragma debug field 21 8 0 1 "__pfc0" ;0,1
#pragma debug field 21 8 0 1 "__pfc1" ;1,1
#pragma debug field 21 8 0 1 "__pfc2" ;2,1
#pragma debug field 21 8 0 1 "__pfc3" ;3,1
#pragma debug field 21 8 0 1 "__pfc4" ;4,1
#pragma debug field 21 8 0 1 "__pfc5" ;5,1
#pragma debug field 21 8 0 1 "__pfc6" ;6,1
#pragma debug field 21 8 0 1 "__pfc7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 60 ""
#pragma debug field 2 59 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 60 1 ___pfc "__pfc" 1
#pragma debug struct_begin 61 "__mfi5_bits"
#pragma debug field 21 8 0 1 "__ur0e" ;0,1
#pragma debug field 21 8 0 1 "__ur1e" ;1,1
#pragma debug field 21 8 0 1 "__ur2e" ;2,1
#pragma debug field 21 8 0 1 ;3,1
#pragma debug field 21 8 0 1 "__ur0f" ;4,1
#pragma debug field 21 8 0 1 "__ur1f" ;5,1
#pragma debug field 21 8 0 1 "__ur2f" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 62 ""
#pragma debug field 2 61 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 62 1 ___mfi5 "__mfi5" 1
#pragma debug struct_begin 63 "__wdtc_bits"
#pragma debug field 21 8 0 1 "__ws0" ;0,1
#pragma debug field 21 8 0 1 "__ws1" ;1,1
#pragma debug field 21 8 0 1 "__ws2" ;2,1
#pragma debug field 21 8 0 1 "__we0" ;3,1
#pragma debug field 21 8 0 1 "__we1" ;4,1
#pragma debug field 21 8 0 1 "__we2" ;5,1
#pragma debug field 21 8 0 1 "__we3" ;6,1
#pragma debug field 21 8 0 1 "__we4" ;7,1
#pragma debug struct_end
#pragma debug union_begin 64 ""
#pragma debug field 2 63 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 64 1 ___wdtc "__wdtc" 1
#pragma debug struct_begin 65 "__stm0c0_bits"
#pragma debug field 21 8 0 3 ;0,3
#pragma debug field 21 8 0 1 "__st0on" ;3,1
#pragma debug field 21 8 0 1 "__st0ck0" ;4,1
#pragma debug field 21 8 0 1 "__st0ck1" ;5,1
#pragma debug field 21 8 0 1 "__st0ck2" ;6,1
#pragma debug field 21 8 0 1 "__st0pau" ;7,1
#pragma debug struct_end
#pragma debug union_begin 66 ""
#pragma debug field 2 65 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 66 1 ___stm0c0 "__stm0c0" 1
#pragma debug struct_begin 67 "__stm0c1_bits"
#pragma debug field 21 8 0 1 "__st0cclr" ;0,1
#pragma debug field 21 8 0 1 "__st0dpx" ;1,1
#pragma debug field 21 8 0 1 "__st0pol" ;2,1
#pragma debug field 21 8 0 1 "__st0oc" ;3,1
#pragma debug field 21 8 0 1 "__st0io0" ;4,1
#pragma debug field 21 8 0 1 "__st0io1" ;5,1
#pragma debug field 21 8 0 1 "__st0m0" ;6,1
#pragma debug field 21 8 0 1 "__st0m1" ;7,1
#pragma debug struct_end
#pragma debug union_begin 68 ""
#pragma debug field 2 67 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 68 1 ___stm0c1 "__stm0c1" 1
#pragma debug variable 8 1 ___stm0al "__stm0al" 1
#pragma debug variable 8 1 ___stm0ah "__stm0ah" 1
#pragma debug struct_begin 69 "__stm0rp_bits"
#pragma debug field 21 8 0 1 "__st0rp0" ;0,1
#pragma debug field 21 8 0 1 "__st0rp1" ;1,1
#pragma debug field 21 8 0 1 "__st0rp2" ;2,1
#pragma debug field 21 8 0 1 "__st0rp3" ;3,1
#pragma debug field 21 8 0 1 "__st0rp4" ;4,1
#pragma debug field 21 8 0 1 "__st0rp5" ;5,1
#pragma debug field 21 8 0 1 "__st0rp6" ;6,1
#pragma debug field 21 8 0 1 "__st0rp7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 70 ""
#pragma debug field 2 69 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 70 1 ___stm0rp "__stm0rp" 1
#pragma debug struct_begin 71 "__u0sr_bits"
#pragma debug field 21 8 0 1 "__txif0" ;0,1
#pragma debug field 21 8 0 1 "__tidle0" ;1,1
#pragma debug field 21 8 0 1 "__rxif0" ;2,1
#pragma debug field 21 8 0 1 "__ridle0" ;3,1
#pragma debug field 21 8 0 1 "__oerr0" ;4,1
#pragma debug field 21 8 0 1 "__ferr0" ;5,1
#pragma debug field 21 8 0 1 "__nf0" ;6,1
#pragma debug field 21 8 0 1 "__perr0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 72 ""
#pragma debug field 2 71 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 72 1 ___u0sr "__u0sr" 1
#pragma debug struct_begin 73 "__u0cr1_bits"
#pragma debug field 21 8 0 1 "__tx80" ;0,1
#pragma debug field 21 8 0 1 "__rx80" ;1,1
#pragma debug field 21 8 0 1 "__txbrk0" ;2,1
#pragma debug field 21 8 0 1 "__stops0" ;3,1
#pragma debug field 21 8 0 1 "__prt0" ;4,1
#pragma debug field 21 8 0 1 "__pren0" ;5,1
#pragma debug field 21 8 0 1 "__bno0" ;6,1
#pragma debug field 21 8 0 1 "__uarten0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 74 ""
#pragma debug field 2 73 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 74 1 ___u0cr1 "__u0cr1" 1
#pragma debug struct_begin 75 "__u0cr2_bits"
#pragma debug field 21 8 0 1 "__teie0" ;0,1
#pragma debug field 21 8 0 1 "__tiie0" ;1,1
#pragma debug field 21 8 0 1 "__rie0" ;2,1
#pragma debug field 21 8 0 1 "__wake0" ;3,1
#pragma debug field 21 8 0 1 "__adden0" ;4,1
#pragma debug field 21 8 0 1 "__brgh0" ;5,1
#pragma debug field 21 8 0 1 "__rxen0" ;6,1
#pragma debug field 21 8 0 1 "__txen0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 76 ""
#pragma debug field 2 75 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 76 1 ___u0cr2 "__u0cr2" 1
#pragma debug variable 8 1 ___txr_rxr0 "__txr_rxr0" 1
#pragma debug variable 8 1 ___brg0 "__brg0" 1
#pragma debug struct_begin 77 "__pas1_bits"
#pragma debug field 21 8 0 1 "__pas10" ;0,1
#pragma debug field 21 8 0 1 "__pas11" ;1,1
#pragma debug field 21 8 0 1 "__pas12" ;2,1
#pragma debug field 21 8 0 1 "__pas13" ;3,1
#pragma debug field 21 8 0 1 "__pas14" ;4,1
#pragma debug field 21 8 0 1 "__pas15" ;5,1
#pragma debug field 21 8 0 1 "__pas16" ;6,1
#pragma debug field 21 8 0 1 "__pas17" ;7,1
#pragma debug struct_end
#pragma debug union_begin 78 ""
#pragma debug field 2 77 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 78 1 ___pas1 "__pas1" 1
#pragma debug struct_begin 79 "__pcs1_bits"
#pragma debug field 21 8 0 1 "__pcs10" ;0,1
#pragma debug field 21 8 0 1 "__pcs11" ;1,1
#pragma debug field 21 8 0 1 "__pcs12" ;2,1
#pragma debug field 21 8 0 1 "__pcs13" ;3,1
#pragma debug field 21 8 0 1 "__pcs14" ;4,1
#pragma debug field 21 8 0 1 "__pcs15" ;5,1
#pragma debug field 21 8 0 1 "__pcs16" ;6,1
#pragma debug field 21 8 0 1 "__pcs17" ;7,1
#pragma debug struct_end
#pragma debug union_begin 80 ""
#pragma debug field 2 79 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 80 1 ___pcs1 "__pcs1" 1
extern r1:byte
extern r2:byte
extern r3:byte
extern r4:byte
extern r5:byte
extern r6:byte
extern r7:byte
#line 29 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\DC_Motor_with_sensor_v1\DC_Motor_with_sensor_v1.c"
@code .section at 0 'code'
	clr bp
	jmp _main_startup1


; 
; Generated by holtek-gcc v3.19, Tue Apr 12 19:16:37 2022
; Rebuild 718
; end of file
