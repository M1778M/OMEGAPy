#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

void // VoidType/(raise)</msg:char[]/></obj_name:char[]/></type_error:char[]/>
raise
(char msg[],char obj_name[],char type_error[]) /* Just For Debuging (print but like showing error without exit-1) */
{
  printf("\n%s in %s :\n\t # %s\n",type_error,obj_name,msg);
}

/* 'Initial eyes' Functions */
int // IntegerType/(int_arraylen)</arr:int[]/>
int_arraylen
(int arr[]); /* return's Lenght Of Integer Array */
/* ------- */
int // IntegerType/(char_arraylen)</arr:char[]/>
char_arraylen
(char arr[]); /* return's Lenght Of Character or Strings Array */
/* -------- */
void // VoidType/(syscode)</code:char[]/>
syscode
(char code[]); /* return's Output Of Command From Code */
/* --------- */
bool // BooleanType/(strcheck)</fstr:char[]/></sstr:char[]/>
strcheck
(char fstr[],char sstr[]); /* Check's FStr == SStr -> bool(true||false)*/
/* --------------------- */
bool // BooleanType/(intcheck)</fint:int/>&&</sint:int/>
intcheck 
(int fint,int sint); /* Check's FInt == SInt -> bool(true||false)*/
/* --------------- */
bool // BooleanType/(intarraycheck)</fintarray:int[]/>&&</sintarray:int[]/>
intarraycheck
(int fintarray[],int sintarray[]); /*Check's FIntArray[] == SIntArray[] -> bool(true||false) */
/* ------------------------------*/
char // CharacterType/(tfcheck)</tof:bool/> 
tfcheck
(bool tof);

/* Functions */
int 
int_arraylen
(int arr[])
{
  return sizeof(arr) / sizeof(int);
}

int
char_arraylen
(char arr[])
{
  return sizeof(arr) / sizeof(char);
}

void
syscode
(char code[])
{
  system(code);
}

bool
strcheck
(char fstr[],char sstr[])
{if (!fstr!=sstr) {return true;}else {return false;}}


bool
intcheck
(int fint,int sint)
{if (!fint!=sint) {return true;}else {return false;}}

bool
intarraycheck
(int fintarray[],int sintarray[])
{if (!fintarray!=sintarray) {return true;}else {return false;}}

char
tfcheck
(bool tof)
{if (tof) {return "true";}else {return "false";}}

/* Debug */
int main()
{
	int integer_array[] = {10,30,70,80,90000,-100000,5-5};
	if (int_arraylen(integer_array)!=7){
		raise ("(integer_array len) = 7 , but it is'nt","main()","AssertError");
		printf("integer_array = %d\n" , (int)int_arraylen(integer_array));
	}
	char array[] = "OMEGAPy";
	if (char_arraylen(array)!=7){
		raise ("(array len) = 7 , but it is'nt","main()","AssertError");
		printf("array = %d\n",(int)char_arraylen(array));
	}

	char fname[] = "raw", sname[] = "raw";
	if (strcheck(fname,sname)!=true){
		raise ("(string compare) its == but it is'nt","main()","AssertError");
		printf("strcheck('raw','raw') = %s\n",tfcheck(strcheck(fname,sname)));
	}


	printf("\n");
	syscode("echo omg");
	printf("\n");
	/* Full Check
	printf("'123'=='321': %s\n'666'=='666': %s",
	tfcheck(strcheck("123","321")),tfcheck(strcheck("666","666")));
	*/
	

}
