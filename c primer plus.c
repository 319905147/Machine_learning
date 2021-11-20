#define _CRT_SECURE_NO_WARNINGS 1
// 1 编写一个程序将年龄换算成天数
//#include<stdio.h>
//int main(void)
//{
//	int age;
//	int age_days;
//	scanf("请输入你的年龄: %d", &age);
//	age_days = age * 365;
//	printf("年龄为%d年\n", age);
//	printf("年龄换算成天数为%d天\n", age_days);
//	return 0;
//}


// 2 如果函数的定义是在调用函数的后面（下面）则需要在调用之前声明函数的定义，否则不需要事先声明。
//自定义函数 jolly()  deny() 调用 
//#include <stdio.h>
////void jolly(void);
////void deny(void);
//void jolly(void)
//{
//	printf("For he's a jolly good fellow!\n");
//	printf("For he's a jolly good fellow!\n");
//	printf("For he's a jolly good fellow!\n");
//}
//void deny(void)
//{
//	printf("Which nobody can deny!\n");
//}
//int main(void)
//{
//	jolly();
//	//jolly();
//	//jolly();
//	deny();
//	return 0;
//}

// 3 除main函数外,自定义 br()调用一次打印 "Brazil, russia" ,ic()函数调用一次打印"India ,China" 
//
//#include<stdio.h>
//void br(void)
//{
//	printf("Brazil, Russia");
//}
//
//void ic(void)
//{
//	printf("India, China");
//}
//
//int main()
//{
//	br();
//	printf(",");
//	ic();
//	printf("\n");
//	ic();
//	printf("\n");
//	br();
//	return 0;
//}
//
//
//// 4 编写一个程序,创建一个整型变量 toes ,并将toes设置为 10 ,并计算toes的二倍,和toes的平方并描述打印三个值
//#include<stdio.h>
//int main()
//{
//	int toes = 10;
//	int toes_2 = 0;
//	int toes2= 0;
//	//toes_2 =2* toes;
//	//toes2 =toes* toes;
//	printf("toes = %d,twice = %d,square= %d", toes, 2*toes,toes* toes);
//
//	return 0;
//}

//编写一个程序,要求输入一个ASCII码值,然后打印输入的字符
//#include<stdio.h>
//int main()
//{
//	int ascii;
//	printf("请输入一个ASCII码值: ");
//	scanf("%d", &ascii);
//	printf("码值为%d对应的符号是%c", ascii, ascii);
//	return 0;
//}
//一个水分子质量约为3.0*10-23克,一夸克的水约为950克,编写一个程序,提示用户输入谁的夸克数,并显示谁的分子数
//
//#include<stdio.h>
//int main()
//{
//	float water_quality=950;
//	float water_quack;
//	scanf("请输入谁的夸克数: ",&water_quack);
//	float water_num;
//	water_quality = water_quack / 950;
//	water_num = water_quack / water_quack;
//	printf("%e有水分子数为%a", water_quack, water_num);
//	return 0;
//}
//#include <stdio.h>
//int main(void)
//{
//	float mass_mol = 3.0e-23; /* mass of water molecule in grams */
//	float mass_qt = 950; /* mass of quart of water in grams */
//	float quarts;
//	float molecules;
//	printf("Enter the number of quarts of water: ");
//	scanf("%f", &quarts);
//	molecules = quarts * mass_qt / mass_mol;
//	printf("%f quarts of water contain %e molecules.\n", quarts, molecules);
//	return 0;
//}
// 超过18岁的可以饮酒,否则不能饮酒
//
//#include<stdio.h>
//int main()
//{
//	int a;
//	scanf("%d", &a);
//	if (a > 18)
//		printf("获得一张饮酒卷");
//	else
//		printf("没有获得饮酒卷");
//	return 0;
//}
//
//
//

//#include<stdio.h>
//#define pi 3.14
//int main()
//{
//	int r;
//	float S,V;
//	scanf("%d", &r);
//	printf("球体的表面积为%0.2f\n",4 * pi * r * r);
//	printf("球体的体积为%0.2f\n",4 * pi * r * r * r/3);
//	return 0;
//}

//
//#include<stdio.h>
//int main()
//{
//	int a, b;
//	scanf("%d+%d", &a, &b);
//	printf("3+5=%d", 3 + 5);
//	return 0;
//}


//1  判断一个数是否是一个奇数
//2 输出1-100之间的奇数


//
//#include<stdio.h>
//int main()
//{
//	int i = 1;
//	for (i; i <= 100; i++)
//	{
//		if (i % 2 != 0)
//			printf("奇数 %d\n", i);
//	}
//	return 0;
//}
//// 求实际工资.实际工资= 工资-税收
//#include<stdio.h>
//int main()
//{
//	int a;  //工资 a
//	printf("请输入你的工资");
//	scanf("%d", &a);
//	if (a < 5000)
//		printf("实发工资为=%d\n", a);
//	else
//	{
//		double w;  // w 实发工资
//		w = a * 0.97;
//		printf("实发工资为%lf\n", w);
//	}
//	return 0;
//}

//#include<stdio.h>
//int main()
//{
//	int i;
//	for (i = 1; i <= 100; i++)
//	{
//		if (i % 2 != 0)
//			printf("%d\n", i);
//	}
//	return 0;
//}
//
//
//
