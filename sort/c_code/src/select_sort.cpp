#include<iostream>
using namespace std;

// 打印数组中的数
void print_arr(const int *arr, int len)
{
    for(int i=0; i<len; i++)
    {
        cout<<arr[i]<<'\t';
    }
    cout<<endl;
}

// 选择排序
// 核心思想：选择最小的放在前面，只交换n-1次

int main()
{
	int a[]={12,3,4,2,26,17,0,1};
    int tmp;
    int min_index;
    int len_a;
    len_a = sizeof(a)/sizeof(a[0]);
    
    // 打印原数组
    cout<<"before:"<<endl;
    print_arr(a, len_a);
    
	for(int i=0; i<len_a; i++)
	{	
		a[min_index] = a[i];  // 假设最小的是第一个元素
		for(int j=i; j<len_a; j++)
		{
			//选出最小值
			if(a[j]<a[min_index])
			{
				min_index = j; //存储较小的一个
			}
		}
		// 遍历结束，如果最小值发生改变，则交换
		if(a[min_index] != a[i])
		{
			tmp = a[min_index];
			a[min_index] = a[i];
			a[i] = tmp;
		}
	}
	
	// 打印数组
    cout<<"after:"<<endl;
    print_arr(a, len_a);
}
