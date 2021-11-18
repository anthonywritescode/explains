.PHONY: all
all: main

main: main.o lib.o
	gcc -o $@ $^

%.o: %.c
	gcc -c $< -o $@

.PHONY: clean
clean:
	rm -f *.o main
