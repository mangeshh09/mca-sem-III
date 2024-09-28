#include <stdio.h>
int main()
{
      int first, middle,last, n, i, search, a[100];
      setbuf(stdout, NULL);
      printf("ENTER THE SIZE OF ARRAY:");
      scanf("%d", &n);
      printf("ENTER %d ELEMENT IN ASCENDING ORDER:\n",n);
      for(i=0; i<n; i++)
          scanf("%d", &a[i]);
          printf("ENTER THE VALUE TO BE SEARCH:\n");
          scanf("%d", &search);
          first=0;
          last=n-1;
          middle=(first+last)/2;
          while(first <= last)
          {
                if(a[middle]<search)
                first = middle + 1;
                else if(a[middle] == search)
                {
                      printf("ELEMENT FOUND AT INDEX %d.\n",middle);
                      break;
                }
                else
                    last = middle - 1;
                    middle = (first + last)/2;
           }
                 if(first > last)
                 printf("ELEMENT NOT FOUND IN THE LIST.\n");
                 return 0;
}
