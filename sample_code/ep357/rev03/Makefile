.PHONY: all
all: main

main: main.o lib.o
	gcc -o $@ main.o lib.o

main.o: main.c
	gcc -c $< -o $@

lib.o: lib.c
	gcc -c $< -o $@

.PHONY: clean
clean:
	rm -f *.o main
