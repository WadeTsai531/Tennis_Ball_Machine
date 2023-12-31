; Generated by holtek-gcc v3.19, Wed Jul 27 16:09:11 2022
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
___stm2c0 equ [313]
___stm2c1 equ [314]
___stm2rp equ [319]
___stm2al equ [317]
___stm2ah equ [318]
___pfs1 equ [344]
public _stm_setup
#pragma debug scope 2 1
#line 79 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
_stm_setup .section 'code'
_stm_setup proc
#line 81 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,32
	mov [78],a
#line 82 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,168
	mov [79],a
#line 83 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,2
	mov [84],a
#line 84 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	clr [82]
	clr [83]
#line 86 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,32
	lmov [338],a
#line 89 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,32
	lmov [313],a
#line 90 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,168
	lmov [314],a
#line 91 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,2
	lmov [319],a
#line 92 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	lclr [317]
	lclr [318]
#line 94 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,128
	lmov [344],a
	ret
_stm_setup endp
#line 94 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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
#line 113 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
_UART_Setup .section 'code'
_UART_Setup proc
#line 114 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,240
	lmov [334],a
#line 115 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,128
	lmov [273],a
#line 116 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,196
	lmov [274],a
#line 117 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,12
	lmov [276],a
#line 118 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [56].0
#line 119 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	clr [56].4
#line 120 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [19].3
#line 121 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [16].0
	ret
_UART_Setup endp
#line 121 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
#pragma debug scope 1 1
___u0sr equ [272]
___txr_rxr0 equ [275]
public _Read_Data
#pragma debug scope 4 1
#line 125 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
_Read_Data .section 'code'
_Read_Data proc
_L5:
#line 126 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	lsnz [272].3
	jmp _L5
#line 127 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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
#line 128 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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
#line 129 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,1
	add a,rb
	mov _kn[0],a
	mov a,0
	adc a,rc
	mov _kn[1],a
_L3:
	ret
_Read_Data endp
#line 129 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
#pragma debug scope 1 1
public _Uart_R
#pragma debug scope 5 1
#line 98 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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
#line 99 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	fcall _Read_Data
#line 100 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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

#line 100 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
#pragma debug scope 1 1
public _Send_Data
#pragma debug scope 7 1
#line 133 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
_Send_Data .section 'code'
_Send_Data proc
    local _Send_Data_2 db 1 dup(?)	; 0,1
	mov _Send_Data_2[0],a
#pragma debug variable 7 7 _Send_Data_2+0 "data"
_L16:
#line 134 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	lsnz [272].0
	jmp _L16
#line 135 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,_Send_Data_2[0]
	lmov [275],a
_L18:
#line 136 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	lsnz [272].1
	jmp _L18
	ret
_Send_Data endp
#line 136 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
#pragma debug scope 1 1
public _Sen
#pragma debug scope 8 1
#line 104 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
rombank 0 @Sen_code
@Sen_code .section at 4 'code'
	mov r1,a
	mov a,bp
	clr bp
	jmp _Sen
ROMBANK 0 _Sen
#pragma debug scope 1 1
@dummy4 proc
	call _Sen
@dummy4 endp
#pragma debug scope 9 1
_Sen .section 'code'
_Sen proc
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
#line 105 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,_dir[0]
	fcall _Send_Data
#line 106 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,_dir[0]
	sub a,82
	snz z
	jmp _L20
#line 107 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,76
	mov _dir[0],a
	jmp _L19
_L20:
#line 109 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,82
	mov _dir[0],a
_L19:
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
_Sen endp

#line 109 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
#pragma debug scope 1 1
public _delay
#pragma debug scope 10 1
#line 140 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
_delay .section 'code'
_delay proc
public _delay_2
    local _delay_2 db 2 dup(?)	; 2,0
#pragma debug variable 10 10 _delay_2+0 "dev"
#line 142 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	clr rb
	clr rc
_L23:
#line 142 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,rb
	sub a,_delay_2[0]
	mov a,rc
	sbc a,_delay_2[1]
	sz cz
	jmp _L22
	clr ra
_L26:
#line 144 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
;# 144 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c" 1
	nop
	inc ra
#line 143 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,ra
	sub a,25
	snz z
	jmp _L26
#line 142 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	inc rb
	sz z
	inc rc
	jmp _L23
_L22:
	ret
_delay endp
#line 142 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
#pragma debug scope 1 1
___wdtc equ [62]
___scc equ [58]
___hircc equ [59]
___integ equ [57]
___pgc equ [40]
___pg equ [39]
___pdc equ [31]
___pdpu equ [32]
___pd equ [30]
public _main
#pragma debug scope 11 1
#line 25 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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
#line 26 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,171
	mov [62],a
#line 27 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,1
	mov [58],a
#line 28 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,3
	mov [59],a
#line 30 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	fcall _UART_Setup
#line 32 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,1
	mov [57],a
#line 33 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	clr [16].4
#line 34 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [16].1
#line 36 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	fcall _stm_setup
#line 37 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	lset [313].3
#line 39 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	clr [40]
#line 40 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	clr [39]
#line 42 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [31].4
#line 43 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [32].4
#line 45 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,83
	fcall _Send_Data
#line 46 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,116
	fcall _Send_Data
#line 47 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,97
	fcall _Send_Data
#line 48 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,114
	fcall _Send_Data
#line 49 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,116
	fcall _Send_Data
#line 51 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,230
	lmov [317],a
	lclr [318]
_L28:
#line 53 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	sz [30].4
	jmp _L31
#line 55 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [39].6
	jmp _L28
_L31:
#line 57 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,32
	mov _delay_2[0],a
	mov a,78
	mov _delay_2[1],a
	fcall _delay
#line 59 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,63
	andm a,[39]
#line 60 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,16
	mov _delay_2[0],a
	mov a,39
	mov _delay_2[1],a
	fcall _delay
#line 64 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [39].7
#line 65 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,32
	mov _delay_2[0],a
	mov a,78
	mov _delay_2[1],a
	fcall _delay
#line 67 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,63
	andm a,[39]
#line 68 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	mov a,16
	mov _delay_2[0],a
	mov a,39
	mov _delay_2[1],a
	fcall _delay
#line 70 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
	set [39].6
	jmp _L31
	jmp $
_main endp

@dummy proc
	call _main
@dummy endp

#line 70 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
#pragma debug scope 1 1
public _dir
@HCCINIT	.section 'data'
#line 16 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
@HCCINIT_dir .section 'data'
_dir label byte
#pragma debug variable 7 1 _dir "dir"
	db 82
@ROMDATA_BASE .section inpage 'code'
	db 82
@HCCINIT_dir .section 'data'
public _kn
#line 7 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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
#line 6 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
public _Data
@HCCINIT0_Data .section 'data'
_Data	db 10 dup(0)
#pragma debug array 42 8 10 1
#pragma debug variable 42 1 _Data "Data"

@HCCINIT .section 'data'
#line 5 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
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
#pragma debug struct_begin 47 "__pd_bits"
#pragma debug field 21 8 0 1 "__pd0" ;0,1
#pragma debug field 21 8 0 1 "__pd1" ;1,1
#pragma debug field 21 8 0 1 "__pd2" ;2,1
#pragma debug field 21 8 0 1 "__pd3" ;3,1
#pragma debug field 21 8 0 1 "__pd4" ;4,1
#pragma debug field 21 8 0 1 "__pd5" ;5,1
#pragma debug field 21 8 0 1 "__pd6" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 48 ""
#pragma debug field 2 47 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 48 1 ___pd "__pd" 1
#pragma debug struct_begin 49 "__pdc_bits"
#pragma debug field 21 8 0 1 "__pdc0" ;0,1
#pragma debug field 21 8 0 1 "__pdc1" ;1,1
#pragma debug field 21 8 0 1 "__pdc2" ;2,1
#pragma debug field 21 8 0 1 "__pdc3" ;3,1
#pragma debug field 21 8 0 1 "__pdc4" ;4,1
#pragma debug field 21 8 0 1 "__pdc5" ;5,1
#pragma debug field 21 8 0 1 "__pdc6" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 50 ""
#pragma debug field 2 49 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 50 1 ___pdc "__pdc" 1
#pragma debug struct_begin 51 "__pdpu_bits"
#pragma debug field 21 8 0 1 "__pdpu0" ;0,1
#pragma debug field 21 8 0 1 "__pdpu1" ;1,1
#pragma debug field 21 8 0 1 "__pdpu2" ;2,1
#pragma debug field 21 8 0 1 "__pdpu3" ;3,1
#pragma debug field 21 8 0 1 "__pdpu4" ;4,1
#pragma debug field 21 8 0 1 "__pdpu5" ;5,1
#pragma debug field 21 8 0 1 "__pdpu6" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 52 ""
#pragma debug field 2 51 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 52 1 ___pdpu "__pdpu" 1
#pragma debug struct_begin 53 "__pg_bits"
#pragma debug field 21 8 0 1 "__pg0" ;0,1
#pragma debug field 21 8 0 1 "__pg1" ;1,1
#pragma debug field 21 8 0 1 "__pg2" ;2,1
#pragma debug field 21 8 0 1 "__pg3" ;3,1
#pragma debug field 21 8 0 1 "__pg4" ;4,1
#pragma debug field 21 8 0 1 "__pg5" ;5,1
#pragma debug field 21 8 0 1 "__pg6" ;6,1
#pragma debug field 21 8 0 1 "__pg7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 54 ""
#pragma debug field 2 53 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 54 1 ___pg "__pg" 1
#pragma debug struct_begin 55 "__pgc_bits"
#pragma debug field 21 8 0 1 "__pgc0" ;0,1
#pragma debug field 21 8 0 1 "__pgc1" ;1,1
#pragma debug field 21 8 0 1 "__pgc2" ;2,1
#pragma debug field 21 8 0 1 "__pgc3" ;3,1
#pragma debug field 21 8 0 1 "__pgc4" ;4,1
#pragma debug field 21 8 0 1 "__pgc5" ;5,1
#pragma debug field 21 8 0 1 "__pgc6" ;6,1
#pragma debug field 21 8 0 1 "__pgc7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 56 ""
#pragma debug field 2 55 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 56 1 ___pgc "__pgc" 1
#pragma debug struct_begin 57 "__mfi5_bits"
#pragma debug field 21 8 0 1 "__ur0e" ;0,1
#pragma debug field 21 8 0 1 "__ur1e" ;1,1
#pragma debug field 21 8 0 1 "__ur2e" ;2,1
#pragma debug field 21 8 0 1 ;3,1
#pragma debug field 21 8 0 1 "__ur0f" ;4,1
#pragma debug field 21 8 0 1 "__ur1f" ;5,1
#pragma debug field 21 8 0 1 "__ur2f" ;6,1
#pragma debug field 21 8 0 1 ;7,1
#pragma debug struct_end
#pragma debug union_begin 58 ""
#pragma debug field 2 57 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 58 1 ___mfi5 "__mfi5" 1
#pragma debug struct_begin 59 "__integ_bits"
#pragma debug field 21 8 0 1 "__int0s0" ;0,1
#pragma debug field 21 8 0 1 "__int0s1" ;1,1
#pragma debug field 21 8 0 1 "__int1s0" ;2,1
#pragma debug field 21 8 0 1 "__int1s1" ;3,1
#pragma debug field 21 8 0 1 "__int2s0" ;4,1
#pragma debug field 21 8 0 1 "__int2s1" ;5,1
#pragma debug field 21 8 0 1 "__int3s0" ;6,1
#pragma debug field 21 8 0 1 "__int3s1" ;7,1
#pragma debug struct_end
#pragma debug union_begin 60 ""
#pragma debug field 2 59 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 60 1 ___integ "__integ" 1
#pragma debug struct_begin 61 "__scc_bits"
#pragma debug field 21 8 0 1 "__fsiden" ;0,1
#pragma debug field 21 8 0 1 "__fhiden" ;1,1
#pragma debug field 21 8 0 1 "__fss" ;2,1
#pragma debug field 21 8 0 1 "__fhs" ;3,1
#pragma debug field 21 8 0 1 ;4,1
#pragma debug field 21 8 0 1 "__cks0" ;5,1
#pragma debug field 21 8 0 1 "__cks1" ;6,1
#pragma debug field 21 8 0 1 "__cks2" ;7,1
#pragma debug struct_end
#pragma debug union_begin 62 ""
#pragma debug field 2 61 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 62 1 ___scc "__scc" 1
#pragma debug struct_begin 63 "__hircc_bits"
#pragma debug field 21 8 0 1 "__hircen" ;0,1
#pragma debug field 21 8 0 1 "__hircf" ;1,1
#pragma debug field 21 8 0 1 "__hirc0" ;2,1
#pragma debug field 21 8 0 1 "__hirc1" ;3,1
#pragma debug field 21 8 0 4 ;4,4
#pragma debug struct_end
#pragma debug union_begin 64 ""
#pragma debug field 2 63 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 64 1 ___hircc "__hircc" 1
#pragma debug struct_begin 65 "__wdtc_bits"
#pragma debug field 21 8 0 1 "__ws0" ;0,1
#pragma debug field 21 8 0 1 "__ws1" ;1,1
#pragma debug field 21 8 0 1 "__ws2" ;2,1
#pragma debug field 21 8 0 1 "__we0" ;3,1
#pragma debug field 21 8 0 1 "__we1" ;4,1
#pragma debug field 21 8 0 1 "__we2" ;5,1
#pragma debug field 21 8 0 1 "__we3" ;6,1
#pragma debug field 21 8 0 1 "__we4" ;7,1
#pragma debug struct_end
#pragma debug union_begin 66 ""
#pragma debug field 2 65 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 66 1 ___wdtc "__wdtc" 1
#pragma debug struct_begin 67 "__stm0c0_bits"
#pragma debug field 21 8 0 3 ;0,3
#pragma debug field 21 8 0 1 "__st0on" ;3,1
#pragma debug field 21 8 0 1 "__st0ck0" ;4,1
#pragma debug field 21 8 0 1 "__st0ck1" ;5,1
#pragma debug field 21 8 0 1 "__st0ck2" ;6,1
#pragma debug field 21 8 0 1 "__st0pau" ;7,1
#pragma debug struct_end
#pragma debug union_begin 68 ""
#pragma debug field 2 67 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 68 1 ___stm0c0 "__stm0c0" 1
#pragma debug struct_begin 69 "__stm0c1_bits"
#pragma debug field 21 8 0 1 "__st0cclr" ;0,1
#pragma debug field 21 8 0 1 "__st0dpx" ;1,1
#pragma debug field 21 8 0 1 "__st0pol" ;2,1
#pragma debug field 21 8 0 1 "__st0oc" ;3,1
#pragma debug field 21 8 0 1 "__st0io0" ;4,1
#pragma debug field 21 8 0 1 "__st0io1" ;5,1
#pragma debug field 21 8 0 1 "__st0m0" ;6,1
#pragma debug field 21 8 0 1 "__st0m1" ;7,1
#pragma debug struct_end
#pragma debug union_begin 70 ""
#pragma debug field 2 69 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 70 1 ___stm0c1 "__stm0c1" 1
#pragma debug variable 8 1 ___stm0al "__stm0al" 1
#pragma debug variable 8 1 ___stm0ah "__stm0ah" 1
#pragma debug struct_begin 71 "__stm0rp_bits"
#pragma debug field 21 8 0 1 "__st0rp0" ;0,1
#pragma debug field 21 8 0 1 "__st0rp1" ;1,1
#pragma debug field 21 8 0 1 "__st0rp2" ;2,1
#pragma debug field 21 8 0 1 "__st0rp3" ;3,1
#pragma debug field 21 8 0 1 "__st0rp4" ;4,1
#pragma debug field 21 8 0 1 "__st0rp5" ;5,1
#pragma debug field 21 8 0 1 "__st0rp6" ;6,1
#pragma debug field 21 8 0 1 "__st0rp7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 72 ""
#pragma debug field 2 71 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 72 1 ___stm0rp "__stm0rp" 1
#pragma debug struct_begin 73 "__u0sr_bits"
#pragma debug field 21 8 0 1 "__txif0" ;0,1
#pragma debug field 21 8 0 1 "__tidle0" ;1,1
#pragma debug field 21 8 0 1 "__rxif0" ;2,1
#pragma debug field 21 8 0 1 "__ridle0" ;3,1
#pragma debug field 21 8 0 1 "__oerr0" ;4,1
#pragma debug field 21 8 0 1 "__ferr0" ;5,1
#pragma debug field 21 8 0 1 "__nf0" ;6,1
#pragma debug field 21 8 0 1 "__perr0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 74 ""
#pragma debug field 2 73 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 74 1 ___u0sr "__u0sr" 1
#pragma debug struct_begin 75 "__u0cr1_bits"
#pragma debug field 21 8 0 1 "__tx80" ;0,1
#pragma debug field 21 8 0 1 "__rx80" ;1,1
#pragma debug field 21 8 0 1 "__txbrk0" ;2,1
#pragma debug field 21 8 0 1 "__stops0" ;3,1
#pragma debug field 21 8 0 1 "__prt0" ;4,1
#pragma debug field 21 8 0 1 "__pren0" ;5,1
#pragma debug field 21 8 0 1 "__bno0" ;6,1
#pragma debug field 21 8 0 1 "__uarten0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 76 ""
#pragma debug field 2 75 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 76 1 ___u0cr1 "__u0cr1" 1
#pragma debug struct_begin 77 "__u0cr2_bits"
#pragma debug field 21 8 0 1 "__teie0" ;0,1
#pragma debug field 21 8 0 1 "__tiie0" ;1,1
#pragma debug field 21 8 0 1 "__rie0" ;2,1
#pragma debug field 21 8 0 1 "__wake0" ;3,1
#pragma debug field 21 8 0 1 "__adden0" ;4,1
#pragma debug field 21 8 0 1 "__brgh0" ;5,1
#pragma debug field 21 8 0 1 "__rxen0" ;6,1
#pragma debug field 21 8 0 1 "__txen0" ;7,1
#pragma debug struct_end
#pragma debug union_begin 78 ""
#pragma debug field 2 77 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 78 1 ___u0cr2 "__u0cr2" 1
#pragma debug variable 8 1 ___txr_rxr0 "__txr_rxr0" 1
#pragma debug variable 8 1 ___brg0 "__brg0" 1
#pragma debug struct_begin 79 "__stm2c0_bits"
#pragma debug field 21 8 0 3 ;0,3
#pragma debug field 21 8 0 1 "__st2on" ;3,1
#pragma debug field 21 8 0 1 "__st2ck0" ;4,1
#pragma debug field 21 8 0 1 "__st2ck1" ;5,1
#pragma debug field 21 8 0 1 "__st2ck2" ;6,1
#pragma debug field 21 8 0 1 "__st2pau" ;7,1
#pragma debug struct_end
#pragma debug union_begin 80 ""
#pragma debug field 2 79 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 80 1 ___stm2c0 "__stm2c0" 1
#pragma debug struct_begin 81 "__stm2c1_bits"
#pragma debug field 21 8 0 1 "__st2cclr" ;0,1
#pragma debug field 21 8 0 1 "__st2dpx" ;1,1
#pragma debug field 21 8 0 1 "__st2pol" ;2,1
#pragma debug field 21 8 0 1 "__st2oc" ;3,1
#pragma debug field 21 8 0 1 "__st2io0" ;4,1
#pragma debug field 21 8 0 1 "__st2io1" ;5,1
#pragma debug field 21 8 0 1 "__st2m0" ;6,1
#pragma debug field 21 8 0 1 "__st2m1" ;7,1
#pragma debug struct_end
#pragma debug union_begin 82 ""
#pragma debug field 2 81 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 82 1 ___stm2c1 "__stm2c1" 1
#pragma debug variable 8 1 ___stm2al "__stm2al" 1
#pragma debug variable 8 1 ___stm2ah "__stm2ah" 1
#pragma debug struct_begin 83 "__stm2rp_bits"
#pragma debug field 21 8 0 1 "__st2rp0" ;0,1
#pragma debug field 21 8 0 1 "__st2rp1" ;1,1
#pragma debug field 21 8 0 1 "__st2rp2" ;2,1
#pragma debug field 21 8 0 1 "__st2rp3" ;3,1
#pragma debug field 21 8 0 1 "__st2rp4" ;4,1
#pragma debug field 21 8 0 1 "__st2rp5" ;5,1
#pragma debug field 21 8 0 1 "__st2rp6" ;6,1
#pragma debug field 21 8 0 1 "__st2rp7" ;7,1
#pragma debug struct_end
#pragma debug union_begin 84 ""
#pragma debug field 2 83 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 84 1 ___stm2rp "__stm2rp" 1
#pragma debug struct_begin 85 "__pas1_bits"
#pragma debug field 21 8 0 1 "__pas10" ;0,1
#pragma debug field 21 8 0 1 "__pas11" ;1,1
#pragma debug field 21 8 0 1 "__pas12" ;2,1
#pragma debug field 21 8 0 1 "__pas13" ;3,1
#pragma debug field 21 8 0 1 "__pas14" ;4,1
#pragma debug field 21 8 0 1 "__pas15" ;5,1
#pragma debug field 21 8 0 1 "__pas16" ;6,1
#pragma debug field 21 8 0 1 "__pas17" ;7,1
#pragma debug struct_end
#pragma debug union_begin 86 ""
#pragma debug field 2 85 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 86 1 ___pas1 "__pas1" 1
#pragma debug struct_begin 87 "__pcs1_bits"
#pragma debug field 21 8 0 1 "__pcs10" ;0,1
#pragma debug field 21 8 0 1 "__pcs11" ;1,1
#pragma debug field 21 8 0 1 "__pcs12" ;2,1
#pragma debug field 21 8 0 1 "__pcs13" ;3,1
#pragma debug field 21 8 0 1 "__pcs14" ;4,1
#pragma debug field 21 8 0 1 "__pcs15" ;5,1
#pragma debug field 21 8 0 1 "__pcs16" ;6,1
#pragma debug field 21 8 0 1 "__pcs17" ;7,1
#pragma debug struct_end
#pragma debug union_begin 88 ""
#pragma debug field 2 87 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 88 1 ___pcs1 "__pcs1" 1
#pragma debug struct_begin 89 "__pfs1_bits"
#pragma debug field 21 8 0 1 "__pfs10" ;0,1
#pragma debug field 21 8 0 1 "__pfs11" ;1,1
#pragma debug field 21 8 0 1 "__pfs12" ;2,1
#pragma debug field 21 8 0 1 "__pfs13" ;3,1
#pragma debug field 21 8 0 1 "__pfs14" ;4,1
#pragma debug field 21 8 0 1 "__pfs15" ;5,1
#pragma debug field 21 8 0 1 "__pfs16" ;6,1
#pragma debug field 21 8 0 1 "__pfs17" ;7,1
#pragma debug struct_end
#pragma debug union_begin 90 ""
#pragma debug field 2 89 "bits"
#pragma debug field 0 8 "byte"
#pragma debug union_end
#pragma debug variable 90 1 ___pfs1 "__pfs1" 1
extern r1:byte
extern r2:byte
extern r3:byte
extern r4:byte
extern r5:byte
extern r6:byte
extern r7:byte
#line 25 "D:\Wade\Project\Tennis_Ball_Machine\Firmware\Interrupt\Interrupt.c"
@code .section at 0 'code'
	clr bp
	jmp _main_startup1


; 
; Generated by holtek-gcc v3.19, Wed Jul 27 16:09:11 2022
; Rebuild 718
; end of file
