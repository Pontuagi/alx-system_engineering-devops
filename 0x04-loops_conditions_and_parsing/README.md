0x04-loops_conditions_and_parsing
0-RSA_public_key.pub - file containing private ssh key
1-for_best_school - a Bash script that displays Best School 10 times using for loop
2-while_best_school - a Bash script that displays Best School 10 times using while loop
3-until_best_school - a Bash script that displays Best School 10 times using until loop
4-if_9_say_hi - a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.
5-4_bad_luck_8_is_your_chance - a Bash script that loops from 1 to 10 and:
	displays bad luck for the 4th loop iteration
	displays good luck for the 8th loop iteration
	displays Best School for the other iterations
6-superstitious_numbers - a Bash script that displays numbers from 1 to 20 and:
	displays 4 and then bad luck from China for the 4th loop iteration
	displays 9 and then bad luck from Japan for the 9th loop iteration
	displays 17 and then bad luck from Italy for the 17th loop iteration
7-clock - a Bash script that displays the time for 12 hours and 59 minutes:
	display hours from 0 to 12
	display minutes from 1 to 59
8-for_ls - a Bash script that displays:
	The content of the current directory
	In a list format
	Where only the part of the name after the first dash is displayed
9-to_file_or_not_to_file - a Bash script that gives you information about the school file.
	Requirements:
	You must use if and, else (case is forbidden)
	Your Bash script should check if the file exists and print:
	if the file exists: school file exists
	if the file does not exist: school file does not exist
	If the file exists, print:
	if the file is empty: school file is empty
	if the file is not empty: school file is not empty
	if the file is a regular file: school is a regular file
	if the file is not a regular file: (nothing)
10-fizzbuzz - a Bash script that displays numbers from 1 to 100.
	Requirements:
	Displays FizzBuzz when the number is a multiple of 3 and 5
	Displays Fizz when the number is multiple of 3
	Displays Buzz when the number is a multiple of 5
	Otherwise, displays the number
	In a list format
100-read_and_cut - a Bash script that displays the content of the file /etc/passwd.
	Script only displays:
	username
	user id
	Home directory path for the user
101-tell_the_story_of_passwd - a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.
	Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO
102-lets_parse_apache_logs - Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.
	Requirement:
	Format: IP HTTP_CODE
	in a list format
	You must use awk
	You are not allowed to use while, for, until and cut
103-dig_the-data - a Bash script that groups visitors by IP and HTTP status code, and displays this data.
	Requirements:
	The exact format must be:
	OCCURENCE_NUMBER IP HTTP_CODE
	In list format
	Ordered from the greatest to the lowest number of occurrences
	awk must be used
	You are not allowed to use while, for, until and cut

