#include <stdio.h>
int main() 
{
    int a, b, c;

    
    printf("Enter three sides of a triangle (1-10): ");
    if (scanf("%d %d %d", &a, &b, &c) != 3) 
	{
        printf("Invalid input: Please enter three valid integers.\n");
        return 1;
    }

    
    if (a <= 0 || b <= 0 || c <= 0) 
	{
        printf("Sides must be positive integers.\n");
        return 1;
    }
    if (a > 10 || b > 10 || c > 10) 
	{
        printf("Sides must be less than or equal to 10.\n");
        return 1;
    }
  
    if (a == b && b == c) 
	{
        printf("Equilateral triangle\n");
    }
  
    else if (a == b || b == c || a == c) 
	{
        printf("Isosceles triangle\n");
    }
    
    else {
        printf("Scalene triangle\n");
    }

    return 0;
}

