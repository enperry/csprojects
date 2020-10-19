#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
// annoying ass implicit function declaration error-fixer
bool is_cycle(int, int, int);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);
        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // check if candidate name is valid and update ranks array
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    bool duplicate;

    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            duplicate = false;
            // if more prefer i to j than j to i, i is winner and j is loser
            if (preferences[i][j] > preferences[j][i])
            {
                for (int k = 0; k < pair_count; k++)
                {
                    // check duplicate
                    if (pairs[k].winner == i && pairs[k].loser == j)
                    {
                        duplicate = true;
                    }
                }
                if (duplicate == false)
                {
                    pairs[pair_count].winner = i;
                    pairs[pair_count].loser = j;
                    pair_count++;
                }
            }
            // if more prefer j to i than i to j, j is winner and i is loser
            else if (preferences[j][i] > preferences[i][j])
            {
                // check duplicate
                for (int k = 0; k < pair_count; k++)
                {
                    if (pairs[k].winner == j && pairs[k].loser == i)
                    {
                        duplicate = true;
                    }
                }
                if (duplicate == false)
                {
                    pairs[pair_count].winner = j;
                    pairs[pair_count].loser = i;
                    pair_count++;
                }
            }
        }
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    pair temp;
    int i = 0;

    for (i = 0; i < pair_count - 1; i++)
    {
        for (int j = i + 1; j < pair_count; j++)
        {
            if (preferences[pairs[j].winner][pairs[j].loser] > preferences[pairs[i].winner][pairs[i].loser])
            {
                //swap the two values
                temp = pairs[i];
                pairs[i] = pairs[j];
                pairs[j] = temp;
            }
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // step through the sorted_pairs array
    for (int i = 0; i < pair_count; i++)
    {
        // if no cycle will be created, lock the pairs in
        if (!is_cycle(pairs[i].winner, pairs[i].loser, i))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
}

// recursively check for cycle between node and pair at index pair_n
bool is_cycle(int winner, int loser, int pair_n)
{
    // base case (current node is locked and connected to the starting node)
    if (locked[winner][loser] && loser == pairs[pair_n].winner)
    {
        return true;
    }
    // recursive case
    // try to build path from another node in locked matrix to starting node at pair_n
    for (int i = 0; i < candidate_count; i++)
    {
        // if current node locked, check for path that continues to pair_n
        if (locked[loser][i])
        {
            // ex-tra check
            bool check = is_cycle(loser, i, pair_n);
            if (check)
            {
                return true;
            }
        }
    }
    return false;
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        int rank = 0;
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == false)
            {
                rank++;
            }
        }

        if (rank == candidate_count)
        {
            printf("%s\n", candidates[i]);
        }
    }
    return;
}