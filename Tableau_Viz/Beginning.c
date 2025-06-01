//#include <stdio.h>
//
//int main() {
//    char name[100];
//    printf("Kindly state your name: ");
//    scanf("%s", name);
//    printf("Mr. %s, its a pleasure to make your acquintance \n", name);
//    int age;
//    int cut;
//    printf("Care to tell us your age: ");
//    scanf("%d", &age);
//    cut = (age - 10);
//    printf("So you are %d years younger than me",cut);
//}


//# include <stdio.h>
//
//int main() {
//    char line[15];
//    printf("Insert a line and we will return 5 less: ");
//    fgets(line, 8, stdin);
//    printf("\nYour modified line is : %s\n", line);
//
//}

// #include <stdio.h>

// int main() {
//     char line[500];
//     FILE *target_file;
//     target_file = fopen("C:\\Users\\GOGOL\\Documents\\My Projects\\Tableau_Viz\\OhMaGwad.txt", "r");

//     if (fgets(line, 500, target_file) == NULL) {
//         printf("File path Problem,\ncannot detect the file");
//         }

    
//     while (fgets(line, 500,target_file) != NULL) {
//         printf("%s",line);
//     }
//     fclose(target_file);
// }

//#include <stdio.h>
//
//int main() {
//    char line[500];
//    FILE *target_file;
//
//    // Use double backslashes for the file path
//    target_file = fopen("C:\\GOGOL\\Downloads\\Mammamia.txt", "r");
//
//    if (target_file == NULL) {
//        // Handle the case where the file cannot be opened
//        printf("Error: Could not open the file.\n");
//        return 1;
//    }
//
//    // Read and print the lines
//    while (fgets(line, 500, target_file) != NULL) {
//        printf("%s", line);
//    }
//
//    fclose(target_file); // Close the file
//    return 0;
//}


# include <stdio.h>

int main() {
   int guess;
   printf("Guess the mysterious number: \n" );
   while(scanf("%d",guess) != EOF) {
        if (guess == 100) {
            printf(" Yes you found it ");
        }
        else if (guess > 100) {
            printf("The number you chose is too big,  again?  ");
        }
        else {
            printf("The number is too low, again?");
        }

        }


   }

