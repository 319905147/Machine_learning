#define _CRT_SECURE_NO_WARNINGS 1

// ��дһ����������任�������,����ʾ���������
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



////switch ���
//#include<stdio.h>
//int main()
//{
//	int day = 0;
//	scanf("%d", &day);
//	switch(day)
//	{
//	case 1:
//		printf("����һ\n");
//		break;
//	case 2:
//		printf("���ڶ�\n");
//		break;
//	case 3:
//		printf("������\n");
//		break;
//	case 4:
//		printf("������\n");
//		break;
//	case 5:
//		printf("������\n");
//		break;
//	case 6:
//		printf("������\n");
//		break;
//	case 7:
//		printf("������\n");
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
//		{ // switch ����Ƕ��ʹ��
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




  //��дһ������, ���÷��ӱ�ʾ��ʱ��ת������Сʱ�ͷ��ӱ�ʾ��ʱ��, ʹ��#define ����const ����һ����ʾ 60�ķ��ų���, ���� const����
  // , ͨ��whileѭ�����û��ظ�����ֵ,
 //ֱ���û������ֵС�ڵ���0 ��ֹͣѭ��.
//#include <stdio.h>
//#define L 60
//int main()
//{
//	int minute,hour;
//	printf("�������÷��ӱ�ʾ��ʱ��: ");
//	while (scanf("%d", &minute))
//	{
//		if (minute > 0)
//		{
//			hour = minute / L;
//			printf("ת��֮���ʱ��Ϊ: ");
//			printf("%dСʱ%d����\n", hour, minute%L);
//			printf("�������÷��ӱ�ʾ��ʱ��: ");
//		}
//		else
//			break;
//	}
//	return 0;
//}



/*
//�� n�Ľ׳�
#include<stdio.h>
int main()
{
	int a = 0;
	int b = 1;
	int n;
	printf("������һ������ : ");
	scanf("%d", &n);
	for (a = 1; a <= n; a++)
	{
		b = b * a;
	}
	printf("n�Ľ׳�Ϊ %d", b);

	return 0;
}
*/


/*
// ˮ�ɻ���
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
			printf("ˮ�ɻ���Ϊ %d\n", i);

	}
	return 0;
}
*/



//// ʹ��Switch ��� ������Ӧ���·�����,�����Ӧ���·ݵ�Ӣ�ĵ���
//#include<stdio.h>
//int num;
//int  main()
//{
//	printf("�������·ݵ�����: ");
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
// ��дһ������,��ʾ�û�����һ������,Ȼ���ӡ�Ӹ������ȸ�����10����������,(����.�û�����5,���ӡ5~15����������,���� 5 15 ).
//Ҫ���ӡ�ĸ�ֵ֮����һ���ո�,�Ʊ�����з��ֿ�

#include<stdio.h>
int main()
{

	
	int n, m;
	printf("������һ������ : ");
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





// 1 ��дһ������,��ʾ�û���������,Ȼ����ת�������ں�����.����:�û�����18,��ת����2��4��.������ĸ�ʽ��ʾ���: 
//  18 days are 2 weeks ,4 days.
//ͨ��whileѭ�����û��ظ���������,���û�����һ������ֵʱ,(�� 0 �� -20),ѭ������
//#include<stdio.h>
//const int days_weeks = 7;
//int days, week;
//
//int main()
//{
//	printf("����������:  ");
//	while (scanf("%d", &days) == 1)
//	{
//		printf("%d days are %d weeks ,%d days.", days, days / days_weeks, days % days_weeks);
//	}
//	return 0;
//}


// 2 ��дһ������,��ʾ�û�����һ���˵����,(��λ����),���ֱ�������,Ӣ��,Ӣ��Ϊ��λ��ʾ��ֵ,������С������,
//���������û��ظ��������,ֱ���û���������һ������ֵʱ   
// 1 Ӣ�� = 2.54 ����    ;  1���� = 0.39370Ӣ��
//
//
//#include<stdio.h>
//#define In_cm 2.54
//#define in_cm 0.39370
//
//double CM, IN, in;  // ��Ӧ ���� Ӣ�� Ӣ�� 
//int main()
//{
//
//	printf("������һ���˵���� : ");
//	while(scanf("%lf", &CM)==1)
//	{
//		if (CM > 0)
//		{
//			printf("ת����Ӣ��Ϊ %lf\n", CM / In_cm);
//			printf("ת����Ӣ��Ϊ %lf\n", CM / in_cm);
//			printf("���ٴ�����һ���˵����\n");
//		}
//		else
//		{
//			printf("�������������ֲ�����Ҫ��,�����˳�\n");
//			break;
//		}
//	}
//	return 0;
//}


//// 3 ��дһ������,��ʾ�û�����һ�� double ���͵�����,����ӡ������������,
////�Լ����һ���������㲢��ӡ����ֵ,main()����Ҫ����û������ֵ���ݸ��ú���
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
//	printf("������һ��double���͵���: ");
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

// ��дһ������,����һ������16 Ԫ�ص�����,�������д洢16��СдӢ����ĸ,Ȼ���ӡ�������������
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


// �žų˷���

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
//// �Զ��庯��������������ֵ,��Ҫʹ��ָ�����,�ͽ����ò�����
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





// �������� :�ж���������Ӧ��ѭ��һ�����Ϊ:����һ�򣬰��겻���İ�������.
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





