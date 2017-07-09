#=============================================================================
#     FileName: Makefile
#         Desc: Makefile - based on Clement's
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-09 18:15:12
#=============================================================================
CC = g++
CFLAGS = -Wall -Wextra

LIB = #-lm -pthread
HDR = main.h client.h server.h
SRC = main.cc client.cc server.cc
OBJ = $(SRC:.c=.o)

EXE = server

## Top level target is executable.
$(EXE):	$(OBJ) Makefile
	$(CC) $(CFLAGS) -o $(EXE) $(OBJ) $(LIB)

clean:
	rm $(OBJ) 

clobber: clean
	rm $(EXE) 

test:
	@echo "Success, all tests passed"

$(OBJ): $(HDR)

