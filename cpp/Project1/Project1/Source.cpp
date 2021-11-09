#include<iostream>

int F(int x)
{
	return 19 * (x - 1) * (x - 1);
}

using namespace std;

int main()
{
	int a, b, t, M, R;
	a = -10; b = 20;
	M = a; R = F(a);
	for (t = a; t <= b; t++)
	{
		//cout << "IF:   " << F(t) << "  " << R << endl;
		if (F(t) > R)
		{
			M = t; R = F(t);
		}
		//cout << M << endl;
	}

	printf("%d", M);
}