#define _CRT_SECURE_NO_WARNINGS 1
// 1 ��дһ���������任�������
//#include<stdio.h>
//int main(void)
//{
//	int age;
//	int age_days;
//	scanf("�������������: %d", &age);
//	age_days = age * 365;
//	printf("����Ϊ%d��\n", age);
//	printf("���任�������Ϊ%d��\n", age_days);
//	return 0;
//}


// 2 ��������Ķ������ڵ��ú����ĺ��棨���棩����Ҫ�ڵ���֮ǰ���������Ķ��壬������Ҫ����������
//�Զ��庯�� jolly()  deny() ���� 
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

// 3 ��main������,�Զ��� br()����һ�δ�ӡ "Brazil, russia" ,ic()��������һ�δ�ӡ"India ,China" 
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
//// 4 ��дһ������,����һ�����ͱ��� toes ,����toes����Ϊ 10 ,������toes�Ķ���,��toes��ƽ����������ӡ����ֵ
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

//��дһ������,Ҫ������һ��ASCII��ֵ,Ȼ���ӡ������ַ�
//#include<stdio.h>
//int main()
//{
//	int ascii;
//	printf("������һ��ASCII��ֵ: ");
//	scanf("%d", &ascii);
//	printf("��ֵΪ%d��Ӧ�ķ�����%c", ascii, ascii);
//	return 0;
//}
//һ��ˮ��������ԼΪ3.0*10-23��,һ��˵�ˮԼΪ950��,��дһ������,��ʾ�û�����˭�Ŀ����,����ʾ˭�ķ�����
//
//#include<stdio.h>
//int main()
//{
//	float water_quality=950;
//	float water_quack;
//	scanf("������˭�Ŀ����: ",&water_quack);
//	float water_num;
//	water_quality = water_quack / 950;
//	water_num = water_quack / water_quack;
//	printf("%e��ˮ������Ϊ%a", water_quack, water_num);
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
// ����18��Ŀ�������,����������
//
//#include<stdio.h>
//int main()
//{
//	int a;
//	scanf("%d", &a);
//	if (a > 18)
//		printf("���һ�����ƾ�");
//	else
//		printf("û�л�����ƾ�");
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
//	printf("����ı����Ϊ%0.2f\n",4 * pi * r * r);
//	printf("��������Ϊ%0.2f\n",4 * pi * r * r * r/3);
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


//1  �ж�һ�����Ƿ���һ������
//2 ���1-100֮�������


//
//#include<stdio.h>
//int main()
//{
//	int i = 1;
//	for (i; i <= 100; i++)
//	{
//		if (i % 2 != 0)
//			printf("���� %d\n", i);
//	}
//	return 0;
//}
//// ��ʵ�ʹ���.ʵ�ʹ���= ����-˰��
//#include<stdio.h>
//int main()
//{
//	int a;  //���� a
//	printf("��������Ĺ���");
//	scanf("%d", &a);
//	if (a < 5000)
//		printf("ʵ������Ϊ=%d\n", a);
//	else
//	{
//		double w;  // w ʵ������
//		w = a * 0.97;
//		printf("ʵ������Ϊ%lf\n", w);
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
