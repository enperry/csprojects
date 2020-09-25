#include <stdio.h>
#include <cs50.h>

void repeat(char c, int times)
{
    while (--times >= 0)
    {
        printf("%c", c);
    }
}

int main()
{
    int height, width;

    do
    {
        height = get_int("Height: ");
        width = height;
    }
    while (height < 1 || height > 8);

    for (int i = 1; i <= height; i++)
    {
        int num_hashes = i;
        int num_spaces = width - num_hashes;

        repeat(' ', num_spaces);
        repeat('#', num_hashes);

        printf("  ");

        repeat('#', num_hashes);

        printf("\n");
    }
}
