#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    // variables
    float letters = 0, words = 1, sentences = 0;

    string text = get_string("Enter text: ");

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
            letters++;
            {
            if (isspace(text[i]))
                words++;
            {
                if (text [i] == '.' || text[i] == '?' || text[i] == '!')
                    sentences ++;
            }
        }
    }

    float l = letters / words * 100;
    float s = sentences / words * 100;
    float index0 = .0588 * l;
    float index1 = 0.296 * s;
    float index_result = index0 - index1 - 15.8;

    if (index_result < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (index_result > 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %g\n", round(index_result));
    }
}