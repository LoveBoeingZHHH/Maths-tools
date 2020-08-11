#include <stdio.h>
#include<stdlib.h>
 
int main()
{
    int z1;
    int z2;
    int m1;
    int m2;
 
    printf("Please input two num:(a/b c/d):");
    scanf("%d/%d %d/%d",&z1,&m1,&z2,&m2);
 
    if(m1 == m2)
    {
        if(z1 > z2)
        {
            printf("%d/%d > %d/%d\n",z1,m1,z2,m2);
        }
        if(z1 < z2)
        {
            printf("%d/%d < %d/%d\n",z1,m1,z2,m2);
        } 
        if(z1 == z2)
        {
                printf("%d/%d = %d/%d\n",z1,m1,z2,m2);
        }
        
    }
    else
    {
        if(m1 > m2)
        {
            if(z1 > z2)
            {
                if(z1 * m2 > z2 * m1)
                {
                    printf("%d/%d < %d/%d\n",z2,m2,z1,m1);
                }
                else
                {
                    printf("%d/%d > %d/%d\n",z1,m2,z2,m2);
                }
            }
            else if(z1 < z2)
            {
                printf("%d/%d < %d/%d\n",z1,m1,z2,m2);
            }
        }
        else if(m1 < m2)
        {
            if(z1 * m2 > z2 * m1)
            {
                printf("%d/%d > %d/%d\n",z1,m1,z2,m2);
            }
            else if(z1 * m2 < z2 * m1)
            {
                printf("%d/%d < %d/%d\n",z1,m1,z2,m2);
            }
            else
            {
                printf("%d/%d = %d/%d\n",z1,m1,z2,m2);
            }
        }
    }
    system("pause");
    return 0;
}

