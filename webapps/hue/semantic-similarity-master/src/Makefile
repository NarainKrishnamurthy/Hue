###################################################################
### Variables
###################################################################
SRC := ../lib/wn/
SOURCES := $(wildcard ../lib/wn/*.c)
OBJS := $(patsubst ../lib/wn/%,build/%,$(SOURCES:.c=.o))
CC = g++
CFLAGS = -fpermissive -O2 -std=c++11 -I../include/ -I../include/wn/ -I../../similarity


###################################################################
### Targets
###################################################################
all: similar

similar: $(OBJS)
	$(CC) $(CFLAGS) -o similar $(OBJS) ../lib/sentence_similarity.cpp ../lib/wordnet_extended.cpp similar.cpp

build/%.o: $(SRC)/%.c build
	$(CC) $(CFLAGS) -c $< -o $@

build: 
	mkdir -p $@

clean:
	rm -rf similar build
