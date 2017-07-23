#=============================================================================
#     FileName: Makefile
#         Desc: Makefile - based on Clement's Makefile
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-09 18:15:12
#=============================================================================
CC = g++
CFLAGS = -Wall -Wextra -std=c++11

LIB = #-lm -pthread
HDR = logger.h	client.h	server.h	main.h	common.h
SRC = logger.cc	client.cc	server.cc	main.cc
OBJ = $(SRC:.cc=.o)

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

