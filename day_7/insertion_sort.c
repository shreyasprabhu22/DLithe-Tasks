// Online C compiler to run C program online
#include <stdio.h>
void sort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
 
int main() {
    int i,n,a[20];
    printf("enter the number of elements\n");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    sort(a,n);
    printf("sorted elements are\n");
    for(i=0;i<n;i++){
        printf("%d",a[i]);
    }
    

    return 0;
}