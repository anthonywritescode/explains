#include <locale.h>
#include <stdio.h>

int main(void) {
    printf("default locale: %s\n", setlocale(LC_ALL, ""));
}
