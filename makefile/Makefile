#return = $(functionname arg1,arg2,arg3)
#echo $(return)
SHELL := /bin/sh
SRC01 = $(wildcard *.c ./foo/*.c)
SRC02 = 2

ifeq ($(SRC02), 2)
	SRC02=3
else
	SRC02 ?=@
endif

wildcard_test:
	echo $(SRC01)
test:
	echo $(SRC02)
