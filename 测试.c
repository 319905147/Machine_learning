#define _CRT_SECURE_NO_WARNINGS 1

//#include<stdio.h>
//int main()
//{
//	int X;
//	scanf("%d", &X);
//	if (X < 0)
//		printf("%d", -2 * X);
//	else if (20 <= X  )
//		printf("%d", X * X - 2 * X + 10);
//	else
//		printf("%d", 2 * X - 8);
//	return 0;
//}

//
//int main()
//{
//	int n,i;
//	scanf("%d", &n);
//	
//	return 0;
//}

//#include<stdio.h>
//int main()
//{
//    int m=0, i;
//    scanf("%d", &m);
//    for (i = 1; i <= m; i++)
//    {
//        int a, j=2;
//        scanf("%d\n", &a);
//        if (a!=1)
//        {
//            if (a % j++ == 0) 
//                printf("YES\n");
//            else
//                printf("NO\n");
//        }
//        else
//            printf("NO\n");
//    }
//    return 0;
//}
//





//int is_prime(int n)
//{
//	int j;
//	for (j = 1; j < n; j++)
//	{
//		if (n % j == 0)
//			return 0;
//	}
//	return 1;
//}
//#include <stdio.h>
//int main()
//{
//	int i = 0, m;
//	scanf("%d", &m);
//	for (i = 2; i <= m; i++)
//	{
//		int a;
//		scanf("%d",&a);
//		if (a == 1)
//			printf("NO\n");
//		else if (is_prime(a) == 1)
//			printf("YES\n");
//		else
//			printf("NO\n");
//	}
//	return 0;
//}






//#include<stdio.h>
//int main()
//{
//	int n,i,a=0,b=0,c=0;
//	scanf("%d", &n);
//	for (i = 1; i < n; i++)
//	{
//	
//		printf("%d", a * b * c);
//	}
//	//printf("%d", a * b * c);
//	return 0;
//}
//
//


//
//#include<stdio.h>
//int main()
//{
//	int n,m,i,j;
//	scanf("%d", &n);
//	m = 2*n - 1;
//	int arr[] = {0};
//	for (i = 0; i <= m; i++)
//	{
//		scanf("%d", &arr[i]);
//	}
//	for (j = 0; j <= m - 1; j+2)
//	{
//		if (arr[j] != arr[j + 1])
//			printf("%d", arr[j]);
//	}
//	return 0;
//}
//





#include <stdio.h>
int main() 
{
    int num = 0;  
    scanf("%d", &num);
    for (int l = 1; l <= num; l++)
    {
        int a = 0;
        for (int j = 1; j < a; j++)
        {  scanf("%d", &a);
            	if (a % j == 0)
                    printf("YES");
            }
        printf("NO\n");
        }
    }
    return 0;
}