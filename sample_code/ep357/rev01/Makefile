.PHONY: all
all: main

main: main.o lib.o
	gcc -o main main.o lib.o

main.o: main.c
	gcc -c main.c -o main.o

lib.o: lib.c
	gcc -c lib.c -o lib.o

.PHONY: clean
clean:
	rm -f *.o main
