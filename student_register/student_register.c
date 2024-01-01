/**
 * A program for managing a student register.
 *
 * This program allows users to add students to an array, update their points, print the register,
 * write the register into a file, and override the register with data from a file.
 * The program uses a struct to represent each student, which includes their name, student number,
 * and an array of points. The program also includes various helper functions for manipulating the register.
 *
 * @note This program assumes that the maximum length of a student's name is 20 characters,
 * and that there are 6 exercises for which points can be recorded.
 * The program dynamically allocates memory for the student array as needed.
 */
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

/*
Projektiin on käytetty pohjana TIM-materiaalista esimerkkiä 1.5 (6. kierros). Sen pohjalta on rakennettu 
funktiot oppilaan lisäämiseen, tilanteen tulostamiseen ja lukemiseen. Loput funktiot ovat oikeastaan 
apufunktioita syötteen lisäämiseen tai tiedostonkäsittelyfunktioita, joihin löytyy TIMistä ohjeet.
*/

struct student {
	char *std_name;			
	int opnro;
	int points[6];						//Student: has name, student number, and 6-number array of points.								
};

struct student *add_student(struct student *arr, int op_nro, char *name) {			//add a student (name,op_nro) into array of students (arr).

    int i;
    for (i = 0; arr[i].std_name != NULL; i++);		
    struct student *newarray = realloc(arr, sizeof(struct student) * (i + 2));		//Allocating memory for new student.

    if (newarray == NULL) {
    	printf("Allocating memory did not work.\n");
        return NULL; // allocating memory did not work
    }

    //char *name_set = malloc((strlen(name))*sizeof(char)+1);			
    //strcpy(name_set, name);									//Cannot assign string name directly into std_name -> must copy it to a separate variable first.

    newarray[i].std_name = name; 
    newarray[i].opnro = op_nro;													
    memset(newarray[i].points, 0, sizeof(int) * 6);									
    
    newarray[i+1].std_name = NULL;			// Set the new NULL member at end
    printf("Successfully added %s to the array!\n", newarray[i].std_name);										
    return newarray;
}

int count_sum(int *list) {		//Summing up points in array

	int sum = 0;
	for (int i = 0; i < 6; i++ ) {
		sum = sum + list[i];
	}

	return sum;
}

void print_array(struct student *a){			//Printing contents of array

	int sum;
    for (int i = 0; a[i].std_name != NULL; i++) {		
        printf("Name: %s\nStudent Number: %d\n", a[i].std_name, a[i].opnro);
        printf("Points: ");
        for (int j = 0; j < 6; j++) {												
            printf("%d  ", a[i].points[j]);
            sum = count_sum(a[i].points);
        }
        printf("\nTotal points: %d\n\n", sum);

    }
}

int get_student_number(const char *text, int start) {	//Searching the student number from a text with a start index given.
	
	int std_n = 0;
	int student_number;
			
	for (int i = start; text[i] != ' '; i++) {			//Calculating the length of the student number
		std_n++;
	}

	if (strlen(text)+2 < std_n) {		//invalid input (there is no name given for student, etc)
		return 0;																	
	}

	char student_num[6*sizeof(int)] = "";
	strncpy(student_num, text + 2, std_n);

	int ret = sscanf(student_num, "%d", &student_number);
	if (ret != 1) {			//reading student number from text failed
		return 0;
	}
	return student_number;
}

int get_digits(int number) {	//count digits in a number 
	int ret = number/10;
	int digs = 1;
	while (ret != 0) { 	
		digs++;
		ret = ret/10;
	}
	return digs;
}


int find_student(struct student *arr, int stdnum) { 	//searching a student number (stdnum) from student array (arr)
	int i;
	int found = 0;

	for (i = 0; arr[i].std_name != NULL; i++) {
		if (arr[i].opnro == stdnum) {
			found++;
			break;
		}
	}

	if (found == 0) {
		return -1;
	}
	else {
		return i;	//index at which found
	}
}

const struct student *reorder(struct student *arr) {	//Reordering the array purpose of printing array

	int i, j;
	struct student a;

	for (i = 0; arr[i].std_name != NULL; i++) {
		for (j = i+1; arr[j].std_name != NULL; j++) {
			int sum1 = count_sum(arr[i].points);
			int sum2 = count_sum(arr[j].points);		//Which student has biggest amount of points
			if (sum2 > sum1) {
				a = arr[i];
				arr[i] = arr[j];
				arr[j] = a;
			}
		}
	}
	return arr;
}

void write_into_file(struct student *arr, const char *filename) {	//Save info into file

	FILE *file = fopen(filename, "w");

	if (!file) {
		fprintf(stderr, "Could not open file\n");
		exit(EXIT_FAILURE);
	}

	int sum;
	for (int i = 0; arr[i].std_name != NULL; i++) {					//Writing into file without formatting (for simpler reading).
		fprintf(file, "%s %d ", arr[i].std_name, arr[i].opnro); 	//Structure: 1 student per line, on one line "Name opnro points sum"
		for (int j = 0; j < 6; j++) {
            fprintf(file, "%d  ", arr[i].points[j]);
            sum = count_sum(arr[i].points);
        }
        fprintf(file,"%d\n", sum);
	}
	fclose(file);
	printf("Successfully wrote the situation into file '%s'.\n", filename);
}

struct student *override(struct student *arr, const char *filename) {  //Loading info from file and treating that as the current situation

	FILE *file = fopen(filename, "r");

	if (!file) {
		fprintf(stderr, "Could not open file\n");
		return NULL;
	}

	char row[50*sizeof(char)];
	char name[20*sizeof(char)];
	int opnumero;
	int sum;
	int pisteita[6] = {0};
	int n;
	free(arr);
	arr = realloc(arr, sizeof(struct student));
	for (n = 0; fgets(row, 50, file); n++) {		//reading while there are rows of student information
		arr = realloc(arr, (n+2)*sizeof(struct student));

		sscanf(row, "%s %d %d %d %d %d %d %d %d", name, &opnumero, &pisteita[0], &pisteita[1] ,&pisteita[2], &pisteita[3], &pisteita[4], &pisteita[5], &sum);
		for (int i = 0; i < 6; i++) {
			arr[n].points[i] = pisteita[i];
		}

		char *name_set = malloc(20*sizeof(char));		//Reading info into variables
		strcpy(name_set, name);
		arr[n].std_name = name_set;
		arr[n].opnro = opnumero;						//Saving the variable information into struct student variables, saving into array.
	}
	
	arr[n+1].std_name = NULL;
	printf("The new situation is that of loaded from the file '%s'\n",filename );

	return arr;

}

int main() {

	int success = 0;
	struct student *arr = malloc(sizeof(struct student)); 		//Initializing array of students.
	arr[0].std_name = NULL;
	int student_number, digits;
	size_t name_length;
	char filename[20*sizeof(char)] = "";

	while (success == 0) {
		printf("Give text (press enter when done)\n");
		char text[30];
		fgets(text, sizeof(text), stdin);		//Saving user input into _text_
		char command = toupper(text[0]);		//command = first letter of input

		switch(command) {

			case 'A':		//add student

			student_number = get_student_number(text, 2);

			if (student_number == 0) {
				printf("give real number\n");
				break;
			}

			else {
				name_length = 0;
				digits = get_digits(student_number);	//length of student number for knowing index where name starts
				for (int i = 3 + digits; text[i] != '\n'; i++ ) {	//+3 == spaces within text
					name_length++; 
				}
				if (name_length > 20) {
					printf("The given name is too long (20 characters).\n");
					break;
				}

				char name[20*sizeof(char)] = "";
				strncpy(name, text + 3 + digits, name_length);

				arr = add_student(arr,student_number, name);
			}			
			break;


			case 'U':		//Update points

			student_number = get_student_number(text, 2);
			digits = get_digits(student_number);

			const char *dig = text + 3 + digits;		//Excersice number (1 < dig < 6)
			int kierros = atoi(dig);

			char ps[2*sizeof(char)];					//Points-string
			strncpy(ps, text + 5 + digits, 2);
			int pisteet = atoi(ps);						//atoi: number (string) -> number (int), e.g. '45' -> 45

			int ind = find_student(arr, student_number);
			
			if (student_number == 0) {					//Checking for incorrect excercise, points inputs.
				printf("give real number\n");
				break;
			}

			else if (ind == -1) {
				printf("The number you stated cannot be found.\n");
				break;			
			}

			else if (kierros == 0 || kierros > 6) {
				printf("The round number you gave is invalid.\n");
				break;
			}

			else if (pisteet == 0) {
				printf("Give a proper amount of points (more than zero or an integer).\n");
				break;
			}
			else {
				arr[ind].points[kierros-1] = pisteet;
				printf("Added %d points for student number %d in excercise %d!\n", pisteet, student_number, kierros );

			}
			break;



			case 'L': 	//Print array

			reorder(arr);
			print_array(arr);
			break;



			case 'W':	//Write into file
			
			name_length = 0;
			for (int i = 2; text[i] != '\n'; i++ ) {
				name_length++; 
			}
			
			strncpy(filename, text + 2, name_length);		//read filename from text
			write_into_file(arr, filename);
			break;


			case 'O': 	//Override from file

			name_length = 0;
			for (int i = 2; text[i] != '\n'; i++ ) {
				name_length++; 
			}
			char filename[20*sizeof(char)] = "";
			strncpy(filename, text + 2, name_length);
			filename[name_length+1] = '\0';
			

			struct student *arr = override(arr, filename); 
			if (arr == NULL) {
				printf("File not found. Do not quit process.\n");
			}

			break;


			case 'Q':		//Quit
			printf("Quitting\n");
			success++;
			break;

			default:
			printf("Invalid input! Give a proper first command!\n");

		}

	}
	for (int i = 0; arr[i].std_name != NULL; i++) { 		//Freeing allocated memory
		free(arr[i].std_name);
	}
	free(arr);
	return 0;
}