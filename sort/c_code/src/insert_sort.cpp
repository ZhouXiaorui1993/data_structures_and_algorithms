#include <iostream>
using namespace std;

void print_arr(const int *arr, int len);


// 简单插入排序算法
// 核心思想：选择一个元素（视为已排序组），将它和其他元素分开来看，然后从其他元素中逐个取出元素来插入到已排序组中。关键是如何确定插入位置，采用尝试法，从已排序组的最右边元素开始尝试，若待插入值大于元素值，则该值直接放在后面即可；若小于，则往前移动比较，确定插入位置。

int main()
{
    int a[]={12,3,4,2,26,17,0,1};
    int len_a;
    len_a = sizeof(a)/sizeof(a[0]);
    // 打印原数组
    cout<<"before:"<<endl;
    print_arr(a, len_a);
    
    // 首先将第一个元素视为已排序组，故共需要插入n-1次
    for(int i=1; i<len_a; i++)
    {
    	// 待插入的数
    	int x = a[i];
    	int j=i;
    	for(; j>0; j--)
    	{
    		if(x<a[j-1])  //小于，则逐项后移，为插入空出位置
    		{
    			a[j] = a[j-1];
    		}
    		
    		else
    			break;
    	}
    	// 退出内循环时的j即为要插入的位置
    	a[j] = x;
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
