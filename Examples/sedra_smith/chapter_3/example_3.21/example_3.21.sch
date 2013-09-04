EESchema Schematic File Version 2  date Thursday 08 August 2013 11:23:14 AM IST
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:analogSpice
LIBS:analogXSpice
LIBS:convergenceAidSpice
LIBS:converterSpice
LIBS:digitalSpice
LIBS:digitalXSpice
LIBS:linearSpice
LIBS:measurementSpice
LIBS:portSpice
LIBS:sine
LIBS:sourcesSpice
LIBS:example_3.21-cache
EELAYER 25  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 1 1
Title ""
Date "8 aug 2013"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	5800 5100 5800 4550
Wire Wire Line
	8000 5000 8000 5250
Wire Wire Line
	8000 5250 6250 5250
Wire Wire Line
	6250 5250 6250 4550
Connection ~ 7400 5000
Connection ~ 5800 5000
Wire Wire Line
	4600 4700 4600 5000
Wire Wire Line
	8000 4100 8000 3650
Connection ~ 6250 3950
Wire Wire Line
	6900 3950 6250 3950
Connection ~ 6250 3400
Wire Wire Line
	6650 3400 6250 3400
Wire Wire Line
	5250 3650 5100 3650
Wire Wire Line
	5950 3650 5650 3650
Wire Wire Line
	6250 3350 6250 3450
Wire Wire Line
	6250 3850 6250 4050
Wire Wire Line
	5800 4050 5800 3650
Connection ~ 5800 3650
Wire Wire Line
	4600 3650 4600 3800
Wire Wire Line
	7050 3400 7400 3400
Wire Wire Line
	7400 3400 7400 3450
Wire Wire Line
	6900 4350 6900 4500
Wire Wire Line
	8000 3850 8400 3850
Connection ~ 8000 3850
Wire Wire Line
	8400 3850 8400 3950
Wire Wire Line
	7400 3950 7400 5000
Connection ~ 6900 5000
Wire Wire Line
	6250 2850 6250 2750
Wire Wire Line
	6250 2750 8000 2750
Connection ~ 7400 3400
Connection ~ 4600 3650
Wire Wire Line
	7400 5000 4600 5000
$Comp
L GND #PWR01
U 1 1 520331E1
P 5800 5100
F 0 "#PWR01" H 5800 5100 30  0001 C CNN
F 1 "GND" H 5800 5030 30  0001 C CNN
	1    5800 5100
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG02
U 1 1 520331C8
P 8000 3850
F 0 "#FLG02" H 8000 3945 30  0001 C CNN
F 1 "PWR_FLAG" H 8000 4030 30  0000 C CNN
	1    8000 3850
	1    0    0    -1  
$EndComp
$Comp
L VPLOT8_1 U1
U 2 1 5200BC51
P 7400 3100
F 0 "U1" H 7250 3200 50  0000 C CNN
F 1 "VPLOT8_1" H 7550 3200 50  0000 C CNN
	2    7400 3100
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR03
U 1 1 5200A388
P 8400 3950
F 0 "#PWR03" H 8400 3950 30  0001 C CNN
F 1 "GND" H 8400 3880 30  0001 C CNN
	1    8400 3950
	1    0    0    -1  
$EndComp
$Comp
L VPLOT8_1 U1
U 1 1 5200A35B
P 4600 3350
F 0 "U1" H 4450 3450 50  0000 C CNN
F 1 "VPLOT8_1" H 4750 3450 50  0000 C CNN
	1    4600 3350
	1    0    0    -1  
$EndComp
$Comp
L AC v1
U 1 1 5200A218
P 4600 4250
F 0 "v1" H 4400 4350 60  0000 C CNN
F 1 "AC" H 4400 4200 60  0000 C CNN
F 2 "R1" H 4300 4250 60  0000 C CNN
	1    4600 4250
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 52008BF4
P 4850 3650
F 0 "R1" V 4930 3650 50  0000 C CNN
F 1 "10k" V 4850 3650 50  0000 C CNN
	1    4850 3650
	0    -1   -1   0   
$EndComp
$Comp
L C C1
U 1 1 52008BEA
P 5450 3650
F 0 "C1" H 5500 3750 50  0000 L CNN
F 1 "10u" H 5500 3550 50  0000 L CNN
	1    5450 3650
	0    -1   -1   0   
$EndComp
$Comp
L R R2
U 1 1 52008BDA
P 5800 4300
F 0 "R2" V 5880 4300 50  0000 C CNN
F 1 "340k" V 5800 4300 50  0000 C CNN
	1    5800 4300
	1    0    0    -1  
$EndComp
$Comp
L DC v3
U 1 1 52008BC7
P 8000 4550
F 0 "v3" H 7800 4650 60  0000 C CNN
F 1 "5" H 7800 4500 60  0000 C CNN
F 2 "R1" H 7700 4550 60  0000 C CNN
	1    8000 4550
	1    0    0    -1  
$EndComp
$Comp
L DC v2
U 1 1 52008BC4
P 8000 3200
F 0 "v2" H 7800 3300 60  0000 C CNN
F 1 "5" H 7800 3150 60  0000 C CNN
F 2 "R1" H 7700 3200 60  0000 C CNN
	1    8000 3200
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 52008B94
P 7400 3700
F 0 "R6" V 7480 3700 50  0000 C CNN
F 1 "10k" V 7400 3700 50  0000 C CNN
	1    7400 3700
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 52008B8B
P 6850 3400
F 0 "C2" H 6900 3500 50  0000 L CNN
F 1 "10u" H 6900 3300 50  0000 L CNN
	1    6850 3400
	0    -1   -1   0   
$EndComp
$Comp
L R R5
U 1 1 52008B80
P 6900 4750
F 0 "R5" V 6980 4750 50  0000 C CNN
F 1 "130" V 6900 4750 50  0000 C CNN
	1    6900 4750
	1    0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 52008B75
P 6900 4150
F 0 "C3" H 6950 4250 50  0000 L CNN
F 1 "10u" H 6950 4050 50  0000 L CNN
	1    6900 4150
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 52008B69
P 6250 4300
F 0 "R4" V 6330 4300 50  0000 C CNN
F 1 "6k" V 6250 4300 50  0000 C CNN
	1    6250 4300
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 52008B57
P 6250 3100
F 0 "R3" V 6330 3100 50  0000 C CNN
F 1 "10k" V 6250 3100 50  0000 C CNN
	1    6250 3100
	1    0    0    -1  
$EndComp
$Comp
L NPN Q1
U 1 1 52008B4C
P 6150 3650
F 0 "Q1" H 6150 3500 50  0000 R CNN
F 1 "NPN" H 6150 3800 50  0000 R CNN
	1    6150 3650
	1    0    0    -1  
$EndComp
$EndSCHEMATC
