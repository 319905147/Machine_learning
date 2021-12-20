#define _CRT_SECURE_NO_WARNINGS 1

// 编写一个程序把年龄换算成天数,并显示年龄和天数
//#include<stdio.h>
//int main()
//{
//
//	int age;
//	int age_days;
//	scanf("%d", &age);
//	age_days = age * 365;
//	printf("%d\n", age);
//	printf("%d\n", age_days);
//	return 0;
//}
//#include<stdio.h>
//int main()
//{
//	int a = 0;
//	int b = ~a;
//	printf("%d", b);
//	return 0;
// }



//#include<stdio.h>
//int main()
//{
//	int a = 100;
//	int b = 20;
//	int max = 0;
//	max = (a > b ? a : b);
//	/*if (a > b)
//		max = a;
//	else
//		max = b;*/
//	
//	printf("%d", max);
//	return 0;
//}



////switch 语句
//#include<stdio.h>
//int main()
//{
//	int day = 0;
//	scanf("%d", &day);
//	switch(day)
//	{
//	case 1:
//		printf("星期一\n");
//		break;
//	case 2:
//		printf("星期二\n");
//		break;
//	case 3:
//		printf("星期三\n");
//		break;
//	case 4:
//		printf("星期四\n");
//		break;
//	case 5:
//		printf("星期五\n");
//		break;
//	case 6:
//		printf("星期六\n");
//		break;
//	case 7:
//		printf("星期日\n");
//	}
//	return 0;
//}

//#include<stdio.h>
//
//int main()
//{
//	int n = 1;
//	int m = 2;
//	switch(n)
//	{
//	case 1:
//		m++;  
//	case 2:
//		n++;
//	case 3:
//		switch (n)
//		{ // switch 允许嵌套使用
//		case 1:
//			n++;
//		case 2:
//			m++;
//			n++;
//			break;
//		}
//	case 4:
//		m++;
//		break;
//	default:
//		break;
//	}
//	printf("%d %d", m,n);
//	return 0;
//
//}
//
//#include<stdio.h>
//int main()
//{
//	int i, j;
//	for (i = 1; i < 10; i++)
//	{
//		for (j = 1; j < i+1; j++)
//		{
//			printf("%d*%d=%-4d", i, j, i * j);
//		}
//		printf("\n");
//	}
//	return 0;
//}




  //编写一个程序, 把用分钟表示的时间转换成是小时和分钟表示的时间, 使用#define 或这const 创建一个表示 60的符号常量, 或者 const变量
  // , 通过while循环让用户重复输入值,
 //直到用户输入的值小于等于0 是停止循环.
//#include <stdio.h>
//#define L 60
//int main()
//{
//	int minute,hour;
//	printf("请输入用分钟表示的时间: ");
//	while (scanf("%d", &minute))
//	{
//		if (minute > 0)
//		{
//			hour = minute / L;
//			printf("转换之后的时间为: ");
//			printf("%d小时%d分钟\n", hour, minute%L);
//			printf("请输入用分钟表示的时间: ");
//		}
//		else
//			break;
//	}
//	return 0;
//}



/*
//求 n的阶乘
#include<stdio.h>
int main()
{
	int a = 0;
	int b = 1;
	int n;
	printf("请输入一个整数 : ");
	scanf("%d", &n);
	for (a = 1; a <= n; a++)
	{
		b = b * a;
	}
	printf("n的阶乘为 %d", b);

	return 0;
}
*/


/*
// 水仙花数
#include<stdio.h>
int i;
int main()
{
	for (i = 100; i <= 999; i++)
	{
		int b = i % 10;
		int c = i / 10 % 10;
		int d = i / 100 % 10;

		if (b * b * b + c * c * c + d * d * d == i)
			printf("水仙花数为 %d\n", i);

	}
	return 0;
}
*/



//// 使用Switch 语句 输入相应的月份数字,输出对应的月份的英文单词
//#include<stdio.h>
//int num;
//int  main()
//{
//	printf("请输入月份的数字: ");
//	scanf("%d", &num);
//	switch (num)
//	{
//		case 1:
//			printf("January");
//			break;
//		case 2:
//			printf("February");
//			break;
//		case 3:
//			printf("March");
//			break;
//		case 4:
//			printf("April");
//			break;
//		case 5:
//			printf("May");
//			break;
//		case 6:
//			printf("June");
//			break;
//		case 7:
//			printf("July");
//			break;
//		case 8:
//			printf("August");
//			break;
//		case 9:
//			printf("September");
//			break;
//		case 10:
//			printf("October");
//			break;
//		case 11:
//			printf("November");
//			break;
//		case 12:
//			printf("October");
//			break;
//	}
//	return 0;
//}
//
//


/*
// 编写一个程序,提示用户输入一个整数,然后打印从该数到比该数大10的所有整数,(例如.用户输入5,则打印5~15的所欲整数,包括 5 15 ).
//要求打印的各值之间用一个空格,制表符或换行符分开

#include<stdio.h>
int main()
{

	
	int n, m;
	printf("请输入一个整数 : ");
	scanf("%d", &n);
	m = n;
	while (n <= m + 10) {
		printf("%d ", n++);
	}
	
	//int n, m;
	//scanf("%d", &n);
	//for (m = n; m <= n + 10; m++)
	//	printf("%d ", m);
	return 0;
}
*/





// 1 编写一个程序,提示用户输入天数,然后将其转换成周期和天数.列如:用户输入18,则转换成2周4天.以下面的格式显示结果: 
//  18 days are 2 weeks ,4 days.
//通过while循环让用户重复输入天数,当用户输入一个非正值时,(如 0 或 -20),循环结束
//#include<stdio.h>
//const int days_weeks = 7;
//int days, week;
//
//int main()
//{
//	printf("请输入天数:  ");
//	while (scanf("%d", &days) == 1)
//	{
//		printf("%d days are %d weeks ,%d days.", days, days / days_weeks, days % days_weeks);
//	}
//	return 0;
//}


// 2 编写一个程序,提示用户输入一个人的身高,(单位厘米),并分别以厘米,英尺,英寸为单位显示该值,允许有小数部分,
//程序能让用户重复输入身高,直到用户输入输入一个非正值时   
// 1 英尺 = 2.54 厘米    ;  1厘米 = 0.39370英寸
//
//
//#include<stdio.h>
//#define In_cm 2.54
//#define in_cm 0.39370
//
//double CM, IN, in;  // 对应 厘米 英尺 英寸 
//int main()
//{
//
//	printf("请输入一个人的身高 : ");
//	while(scanf("%lf", &CM)==1)
//	{
//		if (CM > 0)
//		{
//			printf("转换成英尺为 %lf\n", CM / In_cm);
//			printf("转换成英尺为 %lf\n", CM / in_cm);
//			printf("请再次输入一个人的身高\n");
//		}
//		else
//		{
//			printf("你输入的身高数字不符合要求,程序退出\n");
//			break;
//		}
//	}
//	return 0;
//}


//// 3 编写一个程序,提示用户输入一个 double 类型的数字,并打印该数的立方数,
////自己设计一个函数计算并打印立方值,main()函数要求把用户输入的值传递给该函数
//
//#include<stdio.h>
//#include<math.h>
//void cube(double n)
//{
//	double w;
//	w = pow(n, 3.0);
//	printf("%lf", w);
//}
//
//double n;
//int main()
//{
//	printf("请输入一个double类型的数: ");
//	scanf("%lf", &n);
//	cube(n);
//	return 0;
//}



//
//
//#include <stdio.h>
//int  main()
//{
//	char num[11][10] = { "ling","yi","er","san","si","wu","liu","qi","ba","jiu" };
//	char str[1024] = { 0 };
//	int  i = 0, sum = 0;
//	gets(str);
//	while (str[i] != '\0')
//	{
//		sum += (str[i++] - 48);
//	}
//	if (sum > 99) {
//		printf("%s %s %s", num[sum / 100], num[sum % 100 / 10], num[sum % 100 % 10]);
//	} 
//	else if (sum > 9) {
//		printf("%s %s %s", num[sum % 100 / 10], num[sum % 100 % 10]);
//	}
//	else {
//		printf("%s", num[sum % 100 % 10]);
//	}
//	return 0;
//}

// 编写一个程序,创建一个包含16 元素的数组,并在其中存储16个小写英文字母,然后打印数组的所有内容
//#include<stdio.h>
//#define SIZE 26
//int main(void)
//{
//	char lcase[SIZE];
//	int i;
//	for (i = 0; i < SIZE; i++)
//	{
//		lcase[i] = 'a' + i;
//		//for (i = 0; i < SIZE; i++)
//		printf("%c", lcase[i]);
//	}
//	printf("\n");
//	return 0;
//}
//
//


// 九九乘法表

//#include<stdio.h>
//int main()
//{
//	int i, j;
//	for (i = 1; i < 10; i++)
//	{
//		for (j = 1; j <= i; j++)
//			printf(" %d*%d=%2d", i, j, i * j);
//		printf("\n");
//	}
//		return 0;
//}
//
//
//// 自定义函数交换两个数的值,需要使用指针变量,和解引用操作符
//funcaton(int* pa, int* pb)
//{
//	int tmp = 0;
//	tmp = *pa;
//	*pa = *pb;
//	*pb = tmp;
//}
//#include<stdio.h>
//int  main()
//{
//	int a = 10;
//	int b = 20;
//	printf("a=%d b=%d\n", a, b);
//
//	funcaton(&a, &b);
//
//	printf("a=%d b=%d\n", a, b);
//
//	return 0;
//}

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
//
//#include <stdio.h>
//int main()
//{
//	int i = 0;
//	for(i=100;i<=200;i++)
//	{
//	
//		if (is_prime(i) == 1)
//			printf("%d\n", i);
//	}
//	return 0;
//}





// 计算闰年 :判定公历闰年应遵循的一般规律为:四年一闰，百年不闰，四百年再闰.
//int is_leap_year(int n) {
//
//	if ((n % 4 == 0 && n % 100 != 0) || (n % 400 == 0))
//		return 1;
//}
//#include<stdio.h>
//int main()
//{
//	int year;
//	for (year = 1000; year < 2000; year++)
//	{
//		if (1 == is_leap_year(year))
//			printf("%d  ", year);
//	}
//	return 0;
//}
//





