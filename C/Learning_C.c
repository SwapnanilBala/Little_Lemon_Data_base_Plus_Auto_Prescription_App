// # include <stdio.h>

// int main() {

// 	char line[1000];
// 	FILE *read_only;
// 	read_only = fopen("C:\\Users\\GOGOL\\Documents\\My Projects\\Tableau_Viz\\OhMaGwad.txt", "r");

// 	if (read_only == NULL) {
// 		printf("No file Detected");
// 	}

// 	else
// 		{ while (fgets(line, 1000, read_only) != NULL) {
// 		printf("%s", line);
// 		}
// 	}
// 	fclose(read_only);
// }

// # include <stdio.h>

// int main() {
// 	int integer;
// 	for(integer = 1; integer < 11; integer++) {
// 		printf("one by one: %d\n",integer );
// 	}
// }

// #include <stdio.h>

// int main() {
//     int number_of_tries;
//     int min_value;
//     int max_value;
//     int user_input;

//     // Get user inputs
//     printf("How many tries do you want? ");
//     scanf("%d", &number_of_tries);
//     printf("\nSet your maximum number: ");
//     scanf("%d", &max_value);
//     printf("\nSet your minimum value: ");
//     scanf("%d", &min_value);

//     // Main loop
//     while (number_of_tries > 0) {
//         printf("\nType a random number: ");
//         scanf("%d", &user_input);

//         if (user_input > max_value) {
//             max_value = user_input; // Update max_value
//             printf("max_value has been updated to %d\n", max_value);
//         }
//         else if (user_input < min_value) {
//             min_value = user_input; // Update min_value
//             printf("min_value has been updated to %d\n", min_value);
//         }
//         else {
//             printf("Nothing has been altered\n");
//         }

//         number_of_tries -= 1; // Decrement the tries
//     }

//     // Final output
//     printf("\nYour max value is: %d\n", max_value);
//     printf("Your min value is: %d\n", min_value);

//     return 0;
// }

// # include <stdio.h>

// int main() {
//     int first = 1;
//     int val,maxval,minval;

//     while(scanf("%d"&val) != EOF) {
//         if (first || val > maxval) maxval = val;
//         if (first || val < minval) minval = val;
//         first = 0;
//     }

//     printf("maximum %d\n",maxval );
//     printf("minimum %d\n",minval );
// }


//# include <stdio.h>
//
//int main() {
//   int guess;
//   printf("Guess the mysterious number: " );
//   while(scanf("%d",&guess) != EOF)
//    {
//        if (guess == 100) {
//            printf(" Yes you found it\n");
//            break;
//        }
//        else if (guess > 100) {
//            printf("The number you chose is too big,  again?\n ");
//        }
//        else {
//            printf("The number is too low, again?\n");
//        }
//
//    }
//
//
//}

# include <stdio.h>


// int main() {
//     int mymult();
//     int retval;

//     retval = mymult(5,6);
//     printf("the answer is : %d ", retval);
// }

// int mymult(a,b)
//     int a,b;
// {
//     int c = a*b;
//     return c;
// }


// // 1. #include is a preprocessor directive that tells the compiler to include
//  the contents of another file before compiling the program.

// // 2. <stdio.h> stands for Standard Input Output Header.
//  This file contains functions that allow us to perform input and output operations, such as printf() (for displaying output) and scanf() (for taking user input).

// // 3. main() is the starting point of any C program.
//  The execution of the program begins from this function.

// // 4. int before main() means that the function returns an integer value.
//  A return value of 0 generally indicates successful execution.

// // 5. printf: This is a function in C used for printing or displaying information on the screen.

// // 6. "%d": This is a format specifier. It tells printf how to interpret the data it's given.
//  In this case, %d is used for integers (whole numbers).

// // 7. 12: This is the actual data you want to print. Here, it's the number 12.

// "%d" stands for decimal integer like 10 100 1 etc.
// "%f" stands for float or double
// "%c" stands for char like ""G"
// "%s" stands for (char array) like "Gogol"
// "%x" or "%X" stands for hexadecimal like ff

// #include <stdio.h>

// int main() {
//     printf("%d", 12);
// }

// #include <stdio.h>

// int main() {
//     printf("%d", 21+40);
// }


// #include <stdio.h>

// int main() {

//   // Replace the _ (underscores) with the correct value
//   printf("%s", "I love C");

// }

// #include <stdio.h>

// int main() {
//     printf("%d",3+4);
//     printf("%d",2+1);
// }

// #include <stdio.h>

// int main() {
//     printf("%d\n", 3+4);
//     printf("%d\n", 1+2);

// }


// #include <stdio.h>

// int main() {
//     printf("%d\n",11*13);
//     printf("%d", 2*(11+13));
// }

// #include <stdio.h>

// int main() {
//     printf("%d %d", 2, 3);
// }

// #include <stdio.h>

// int main() {
// 	// Add printf to output "7 and 3"
// 	printf("%d and %d",2,3);
// }


// #include <stdio.h>: This line is including the Standard Input Output header file. In simple terms, it tells the compiler to include a set of standard input/output functions (like printf) that you can use in your program.

// int main() { ... }: This is the main function of your C program. Every C program starts executing from the main function. It's the entry point. The int before main indicates that this function will return an integer value. In short, when the main function in a C program returns a value (either 0 for success or a non-zero value for failure), it returns this value to the operating system. The operating system can then use this return value for error checking, automation, or other purposes.

// Inside the main function, we have:

// printf("%d", 12 + 7);: We have already learned about this in a previous lesson.
// Curly Braces {}: The opening curly brace { after main() indicate the start of main function. The closing curly braces } indicate the end of main function block.

// This code, when run, will simply display 19 on the screen, which is the sum of 12 and 7.

// #include <stdio.h>

// int main() {
//     int age  = 25;
//     printf("%d", age);
// }


// int num = 100000;
// long long large_num = 100000000000000;
// float pi = 3.14;
// double euler_number = 2.718281828459045;
// char c = 'A';
// bool check = true;


// Data Type  	Description	Range(of values they can store)	Size(in Bytes)

// int	        Stores integers	-2,147,483,648 to 2,147,483,647	4
// long long	Stores large integers	-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807	8
// float	    Stores decimal numbers	1.2e-38 to 3.4e38	4
// double	    Stores large decimal numbers	2.3e-308 to 1.7e308	8
// char	        Stores single character	-128 to 127	1
// bool	        Stores true or false	true or false	1

// #include <stdio.h>

// int main() {
//     int num = 131;
//     printf("%d", num);
//     scanf("%d", &num);
// }


// scanf("%d", &num);
// %d tells scanf() that you are expecting an integer input.
// &num (the address-of operator &)
// tells scanf() where to store the input.

// #include <stdio.h>

// int main() {
//     int num = 0;
//     printf("The current number is: %d\n", num);

//     printf("Enter your number: "); // Prompt the user correctly
//     scanf("%d", &num); // Corrected format string

//     printf("\nYour number is: %d\n", num); // Display user input
//     return 0;
// }

// #include <stdio.h>

// int main() {
//     int a = 23;
//     int b = 20;
//     printf("%d",a+b);
// }


// #include <stdio.h>

// int main() {
//     int length = 76;
//     int width = 45;
//     int area = (length * width);
//     printf("The Area of the given rectangle is %d", area);
// }

// #include <stdio.h>
// int main() {
//     char word[] = "Vegeta";
//     printf("The Special character from the word is: %c",word[2]);
//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// int main () {
//   char num1[] = "2";
//   char num2[] = "3";
//   strcat(num1,num2);
//   printf("%s", num1);
// }

// #include <stdio.h>
// int main() {
//     char mystring[] = "Chaf";
//     mystring[2]= 'e';
//     printf("%s",mystring);
// }

// #include <stdio.h>

// int main() {
//     int number;
//     scanf("%d",&number);
//     printf("Your number is: %d", number);
// }


// #include <stdio.h>

// int main() {
//     int a, b;
//     int sum;
//     int diff;
//     scanf("%d", & a);
//     scanf("%d", & b);
//     // Complete the code
//     printf("The sum is: %d\n",a+b);
//     printf("The sum is: %d",a-b);
// }

#include <stdio.h>

int main() {
    
    char x[10];
    
    // Take user input in variable x
    scanf("%s", x);
    
    // Print greeting
    printf("Hello %s", x);
}