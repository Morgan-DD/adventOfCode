#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROCKS 1000
#define MAX_LENGTH 100

char* addToKeyValueArray(char results[][2][MAX_LENGTH], int *size, const char *key, const char *value) {
    for (int i = 0; i < *size; i++) {
        if (strcmp(results[i][0], key) == 0) {
            return results[i][1];
        }
    }
    strcpy(results[*size][0], key);
    strcpy(results[*size][1], value);
    (*size)++;
    return results[*size - 1][1];
}

void numberOfRock(const char *rocks, int blink, char results[][2][MAX_LENGTH], int *size, int *rockCount) {
    int blinkCounter = 0;
    while (blinkCounter <= blink) {
        char tempRocks[MAX_LENGTH] = "";
        char *rock = strtok((char *)rocks, " ");
        while (rock != NULL) {
            int rockDone = 0;
            for (int i = 0; i < *size; i++) {
                if (strcmp(results[i][0], rock) == 0) {
                    strcat(tempRocks, " ");
                    strcat(tempRocks, results[i][1]);
                    rockDone = 1;
                    break;
                }
            }
            if (strlen(rock) % 2 == 0 && !rockDone) {
                char newNumer[MAX_LENGTH];
                snprintf(newNumer, sizeof(newNumer), "%d %d", atoi(rock) / 2, atoi(rock) / 2);
                strcat(tempRocks, " ");
                strcat(tempRocks, newNumer);
                addToKeyValueArray(results, size, rock, newNumer);
                rockDone = 1;
            } else if (!rockDone) {
                char newNumer[MAX_LENGTH];
                snprintf(newNumer, sizeof(newNumer), "%d", atoi(rock) * 2024);
                strcat(tempRocks, " ");
                strcat(tempRocks, newNumer);
                addToKeyValueArray(results, size, rock, newNumer);
            }
            rock = strtok(NULL, " ");
        }
        blinkCounter++;
        strcpy((char *)rocks, tempRocks + 1); // Skip the leading space
    }
    *rockCount = strlen((char *)rocks) > 0 ? (int)(strlen((char *)rocks) - strlen(strchr((char *)rocks, ' '))) : 0;
}

int main() {
    char lineFilePath[MAX_LENGTH];
    char rocksLine[MAX_LENGTH] = "1 2 3 4 5"; // Placeholder for file content
    char results[MAX_ROCKS][2][MAX_LENGTH] = {{"0", "1"}};
    int size = 1;

    int blinkNeeded = 25;
    int blinkCounter = 1;
    int nbRocks = 0;
    int counter = 1;

    printf("Starting...\n");

    char *singleRock = strtok(rocksLine, " ");
    while (singleRock != NULL) {
        int nbRocksForRun = 0;
        numberOfRock(singleRock, blinkNeeded, results, &size, &nbRocksForRun);
        nbRocks += nbRocksForRun;
        counter++;
        printf("%d/%d\n", counter, (int)(strlen(rocksLine) - strlen(strchr(rocksLine, ' '))));
        singleRock = strtok(NULL, " ");
    }

    printf("Number of blink: %d\n", blinkNeeded);
    printf("number of rocks: %d\n", nbRocks);
    printf("expected result:  183435\n");

    return 0;
}

