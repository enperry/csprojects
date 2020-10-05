#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // initialise variables
    string cipher_text = "";
    string plain_text = "";
    int key;

    // check argument count
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // check key length (26)
    else if (argc == 2 && strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // check key validity (duplicates, non-alphabetical letters)
    else if (argc == 2 && strlen(argv[1]) == 26)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (!isalpha(argv[1][i]))
            {
                printf("Key must have all alphabetical letters.\n");
                return 1;
            }

            for (int j = i + 1, m = strlen(argv[1]); j < m; ++j)
            {
                if (argv[1][i] == argv[1][j])
                {
                    printf("Key cannot have duplicate letter.\n");
                    return 1;
                }
            }
        }

        // input for plain text to be encrypted
        plain_text = get_string("plaintext: ");
        cipher_text = plain_text;

        // cipher plaintext
        for (int i = 0, n = strlen(plain_text); i < n; ++i)
        {
            if (plain_text[i] >= 'A' && plain_text[i] <= 'Z')
            {
                key = plain_text[i] - 'A';
                cipher_text[i] = toupper(argv[1][key]);
            }
            else if (plain_text[i] >= 'a' && plain_text[i] <= 'z')
            {
                key = plain_text[i] - 'a';
                cipher_text[i] = tolower(argv[1][key]);
            }
            else if (isdigit(plain_text[i]))
            {
                cipher_text[i] = plain_text[i];
            }
        }
    }

    // print ciphered text
    printf("ciphertext: %s\n", cipher_text);
    return 0;
}