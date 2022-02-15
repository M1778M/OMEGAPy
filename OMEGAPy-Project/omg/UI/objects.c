#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <Python.h>

#ifdef PYTHON_HEADERS
    #define FOUNDED true
#else
    #define PYTHON_HEADERS
    #define FOUNDED true



int arraylen(int arr[]){
    return sizeof(arr) / sizeof(int);
}

class io {
    public void print(char[] str,char[] end='\n') {
        printf ("%s%s",str,end);
    }
    public void input(char[] str)
    {
        this->print("%s",str);
        return fgets();
    }
}

class pyquery {
    private int Userroototal = 1;
    public void cquery (char[] code) {
        /* Here For Exec Codes */
        Python_Excution_Code (code);
        return true;
    }
    public void fquery (char[] filename) {
        FILE *pyfptr;pyfptr = fopen(filename,"r");
        char[] code = pyfptr;
        fclose(pyfptr);
        /* Here For Exec Codes */
        Python_Excution_Code (code);
        return true;
    }
}

class IReturn {
    public int Ax0[];
    public bool key = false;
    public int start;
    public int step;
    
    public void __constroctor(int Ax0[], int start=0, int step=1) {
        int ot[];
        int lf = arraylen(Ax0);
        for (int i=0; i < arraylen(Ax0);i++) {
            for (int j=0; j < Ax0[i];j++) {
                for (int it = start; it < j;it=it+step) {
                    lf++;
                    ot[lf+1] = it;
                    printf("%d\t",it);
                }
                printf('\n');
            }
            printf('\n');
    
        }
        }
    }
}

int main()
{
    io myObj = new io;
    myObj.print("Hello");
    return 0;
}

