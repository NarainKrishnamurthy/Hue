###################################################################
### Variables
###################################################################
SRC := ../lib/wn/
SOURCES := $(wildcard ../lib/wn/*.c)
OBJS := $(patsubst ../lib/wn/%,build/%,$(SOURCES:.c=.o))
CC = g++
CFLAGS = -fpermissive -O2 -std=c++11 -I../include/ -I../include/wn/ 


###################################################################
### Targets
###################################################################
all: test

test: $(OBJS)
	$(CC) $(CFLAGS) -o test $(OBJS) ../lib/sentence_similarity.cpp ../lib/wordnet_extended.cpp demo.cpp

build/%.o: $(SRC)/%.c build
	$(CC) $(CFLAGS) -c $< -o $@

build: 
	mkdir -p $@

clean:
	rm -rf test build


## zjbanks@gmail.com - Zach  
