#include<iostream>
using namespace std;
void print_arr(const int arr[], int);
int partition(int arr[], int start, int end); //分组函数，返回分组完成后基准元素的索引
void quick_sort(int arr[], int start, int end); //快速排序函数

// 快速排序
// 核心思想：分治思想，选择一个基准元素pivot，每次以它为界限将数组分为两组，递归完成两组排序

int main()
{
	int a[]={12,3,4,2,26,17,0,1};
    int len_a;
    len_a = sizeof(a)/sizeof(a[0]);
    
    // 打印原数组
    cout<<"before:"<<endl;
    print_arr(a, len_a);
    	
	quick_sort(a, 0, len_a-1);  // 对a进行快排
	
	// 打印数组
    cout<<"after:"<<endl;
    print_arr(a, len_a);
}

// 打印数组中的数
void print_arr(const int arr[], int len)
{
    for(int i=0; i<len; i++)
    {
        cout<<arr[i]<<'\t';
    }
    cout<<endl;
}

// 输入数组和要排序的起始位置索引
int partition(int arr[], int start, int end)
{
	int pivot = arr[start];  //这里选择第一个元素作为基准元素
	
	int left=start;  // 可以看出left指向基准值，因此，若基准值取出，则left处是一个坑
	int right=end;
	
	int tmp; // 用于交换元素
	
	// 外循环，当左右指针重合时退出
	while(left < right)
	{
		// 从右边开始遍历，如果元素数值比基准值大，则右指针左移
		while(left<right && arr[right]>=pivot)
			right--;
		// 当遇到小于基准值的元素，将其填入左指针的坑中，同时将坑中的元素（基准元素）取出放入新坑中，即交换元素（保证基准元素永远在坑中）
		if(left<right)
		{
			tmp = arr[left];
			arr[left] = arr[right];
			arr[right] = tmp;
		}
		
		// 切换到左指针处进行遍历，（初始时左坑中是上一次放入的比基准值小的元素），如果元素值比基准值小，则左指针右移
		while(left < right && arr[left] <= pivot)
			left++;
		
		// 当遇到大于基准值的元素，将其和右边坑中的元素进行交换，即将其放入坑中，顺便将基准元素放入挖出的新坑
		if(left<right)
		{
			tmp = arr[right];
			arr[right] = arr[left];
			arr[left] = tmp; 
		}
	}
	
	// 当上述循环退出时，左右指针重合，基准元素位于其中，返回left或right都可以得到基准元素当前的索引
	return left;
}

// 排序函数
void quick_sort(int arr[], int start, int end)
{
	// 递归结束判断
	if(start<end)
	{
		int pivot_index;
		pivot_index = partition(arr, start, end);
	
		// 对左右分组递归排序
		quick_sort(arr, start, pivot_index-1);
		quick_sort(arr, pivot_index+1, end);
	}
}
















