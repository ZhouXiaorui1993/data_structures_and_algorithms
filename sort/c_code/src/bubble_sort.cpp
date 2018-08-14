#include <iostream>
using namespace std;

void print_arr(const int *arr, int len);


// 简单的冒泡排序算法

int main()
{
    int a[]={12,3,4,2,26,17,0,1};
    int tmp;
    int len_a;
    len_a = sizeof(a)/sizeof(a[0]);
    // 打印原数组
    cout<<"before:"<<endl;
    print_arr(a, len_a);
    
    for(int i=0; i<len_a-1; i++)  //需要比较n-1轮
        for(int j=0; j<len_a-i-1; j++)  //每轮两两比较，从0至已排序的位置（冒泡到最后面）
        {
            if(a[j]>a[j+1])  // 如果前面的数比后面的大，则交换位置
            {
                tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
            }
        }
    // 打印数组
    cout<<"after:"<<endl;
    print_arr(a, len_a);
}

// 打印数组中的数
void print_arr(const int *arr, int len)
{
    for(int i=0; i<len; i++)
    {
        cout<<arr[i]<<'\t';
    }
    cout<<endl;
}
