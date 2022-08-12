#include <stdio.h>

#define YEARS_OLD 12

#undef YEARS_OLD

int main(int argc, char const *argv[])
{
    #ifdef YEARS_OLD
    printf("YEARS_OLD\n");
    #endif

    printf("YEARS_NEW\n");

    return 0;
}
