// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int a[5][5];
    int b[5][5],n,i,j,m;
    printf("enter the value of n");
    scanf("%d",&n);
    printf("enter the value of %d X %d matrix",n,n);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        b[i][j]=a[i][j];

        }

    }
     for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d \t",b[i][j]);
        }
        printf("\n");

    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if (a[i][j]==0)
            {
                for(m=0;m<n;m++)
                {
                     b[i][m]=0;
                     b[m][j]=0;
                }
            }
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d \t",b[i][j]);
        }
        printf("\n");

    }





    return 0;
}
