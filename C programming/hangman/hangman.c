#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include "hangman.h"
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <ctype.h>
void print_string(const char string[]);

int get_word(char secret[]){
    // check if file exists first and is readable
    FILE *fp = fopen(WORDLIST_FILENAME, "rb");
    if( fp == NULL ){
        fprintf(stderr, "No such file or directory: %s\n", WORDLIST_FILENAME);
        return 1;
    }

    // get the filesize first
    struct stat st;
    stat(WORDLIST_FILENAME, &st);
    long int size = st.st_size;

    do{
        // generate random number between 0 and filesize
        long int random = (rand() % size) + 1;
        // seek to the random position of file
        fseek(fp, random, SEEK_SET);
        // get next word in row ;)
        int result = fscanf(fp, "%*s %20s", secret);
        if( result != EOF )
            break;
    }while(1);

    fclose(fp);

    return 0;
}

int is_word_guessed(const char secret[], const char letters_guessed[])
{
    for(int i = 0; secret[i]!= '\0'; i++)
    {
        bool found = false;
        for(int j = 0; letters_guessed[j]!= '\0'; j++)
        {
            if(secret[i] == letters_guessed[j])
            {
                found = true;
                break;
            }
        }
        if (!found)
        {
            return 0;
        }
    }
    return 1;
}

void get_guessed_word(const char secret[], const char letters_guessed[], char guessed_word[])
{
    int len = strlen(secret);
    for(int i = 0; secret[i] != '\0'; i++)
    {
        bool match = false;
        for(int j = 0; letters_guessed[j] != '\0'; j++)
        {
            if(secret[i] == letters_guessed[j])
            {
                guessed_word[i] = letters_guessed[j];
                match = true;
                break;
            }
        }
        if (!match)
        {
            guessed_word[i] = '_';
        }
    }

    guessed_word[len] ='\0';
}

void get_available_letters(const char letters_guessed[], char available_letters[])
{
    int count = 0;
    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    
    
    for(int i = 0; alphabet[i] != '\0'; i++)
    {
        bool match = false;
        for(int j = 0; letters_guessed[j] != '\0'; j++)
        {
            if (alphabet[i] == letters_guessed[j])
            {
                match = true;
                break;
            }
        }
        if (!match)
        {
            available_letters[count] = alphabet[i];
            count++;
            
        }
    }

    available_letters[count] = '\0';
}


void hangman(const char secret[])
{
    int chance = 8;
    char available_letters[30] = "";
    char guess[30] = "";
    char correct_guess[30] = "";
    char update_guessed[30] = "";
    int i = 0;

    printf("%s\n", secret);
    printf("Welcome to the game, Hangman!\n");
    printf("I am thinking of a word that is %d letters long.\n", (int) strlen(secret));
    printf("-------------\n");

    

    while (chance > i)
    {
        if(is_word_guessed(secret, correct_guess))
        {
            printf("Congratulations, you won!\n");
            return ;
        }        

        printf("You have %d guesses left.\n", chance-i);
        get_available_letters(correct_guess, available_letters);
        printf("Available letters: %s\n", available_letters);
        printf("Please guess a letter: ");
        scanf("%s", guess);

        for(int j = 0; j[guess]!= '\0'; j++)
        {
            guess[j] = tolower(guess[j]);
        }
        
        if(strlen(guess) == 1)
        {
            if (!is_word_guessed(guess, secret))
            {
                if(guess[0] < 'a' || guess[0] > 'z')
                {
                printf("Oops! %s is not a valid letter: ", guess);
                get_guessed_word(secret, correct_guess, update_guessed);
                print_string(update_guessed);
                }
                else
                {
                    printf("Oops! That letter is not in my word: ");
                    get_guessed_word(secret, correct_guess, update_guessed);
                    print_string(update_guessed);
                    i++;
                }
            }

            else if (!is_word_guessed(guess, available_letters))
            {
                printf("Oops! You've already guessed that letter: ");
                get_guessed_word(secret, correct_guess, update_guessed);
                print_string(update_guessed);
            }
            else
            {
                printf("Good guess: ");
                strcat(correct_guess, guess);
                get_guessed_word(secret, correct_guess, update_guessed);
                print_string(update_guessed);
            }
        }
        
        else
        {
            if(strcmp(guess, secret)==0)
            {
                printf("Congratulations, you won!\n");
                return ;
            }
            else
            {
                printf("Sorry, bad guess. The word was %s.\n", secret);
                return;
            }
        }


        printf("-------------\n");

    }

    if (chance == i)
    {
        printf("Sorry, you ran out of guesses. The word was %s.\n", secret);
    }
}

    
void print_string(const char string[])
{
    for(int i = 0; string[i]!= '\0'; i++)
    {
        printf("%c ", string[i]);
    }
    printf("\n");
}
