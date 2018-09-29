//
//  main.cpp
//  heap_sort
//  堆排序
//  Created by zhouxiaorui on 2018/9/29.
//  Copyright © 2018年 zhouxiaorui. All rights reserved.
//

#include <iostream>
using namespace std;

void heap_sort(int arr[], int len_arr);  // 排序函数
void build_heap(int arr[], int len_arr);  // 将无序数组调整为最大堆
void shift_down(int arr[], int elem, int begin, int end);  // 下沉函数
void print_arr(const int arr[], int len_arr);

void print_arr(const int arr[], int len_arr)
{
    for(int i=0; i<len_arr; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
}

void shift_down(int arr[], int elem, int begin, int end)
{
    /*
     不交换，拿着元素寻找合适的插入位置
     function：将堆顶的元素下沉，为构建最大堆（堆顶元素最大），需要将小元素下移
     end：表示最多能下沉到的位置
     */
    int current_index = begin; // elem当前所在位置
    int current_son_index = 2*current_index+1;  // elem孩子所在的位置，初始化为左孩子
    int current_left_index, current_right_index;
    while (current_son_index <= end)
    {
        current_left_index = current_son_index;
        current_right_index = current_left_index + 1;
        if(current_right_index <= end && arr[current_right_index] > arr[current_left_index])
        {
            current_son_index = current_right_index;
        }
        if(elem > arr[current_son_index])  // 如果elem是最大的元素
            break;
        else
        {
            arr[current_index] = arr[current_son_index];  // 将较大的孩子放到上面
            current_index = current_son_index;  // 更新current_index
            current_son_index = 2*current_index+1;
        }
    }
    // 循环结束，将元素放入current_index
    arr[current_index] = elem;
}

void build_heap(int arr[], int len_arr)  // 将一个无序数组，调整为最大堆
{
    // 从叶结点的上一层最右边的结点开始，通过下沉的方式向左、逐层调整最大堆，直到得到一个完整的最大堆
    for(int i=len_arr/2; i>=0; i--)
    {
        shift_down(arr, arr[i], i, len_arr-1);
    }
}

void heap_sort(int arr[], int len_arr)
{
    /*利用调整后的最大堆进行排序，每次取出堆顶元素放在最后，将最后的元素从堆顶开始下沉，重新调整出一个最大堆（堆的长度每次循环都会变小），直到将所有的元素排序完成*/

    // 调整为最大堆
    build_heap(arr, len_arr);
    // 开始排序
    int max_elem, end_elem;
    for(int i=len_arr-1; i>=0; i--)
    {
        max_elem = arr[0];
        end_elem = arr[i];
        arr[i] = max_elem;  // 放入堆底
        shift_down(arr, end_elem, 0, i-1);
    }
}

int main(int argc, const char * argv[]) {
    // 待排序的数组
    int arr[] = {2, 23, 12, 5, 6, 5, 22, 34, 1, 9};
    int len_arr = sizeof(arr)/sizeof(arr[0]);
    
    cout<<"before sort:"<<endl;
    print_arr(arr, len_arr);
    
    // 堆排序
    heap_sort(arr, len_arr);
    cout<<"after sort:"<<endl;
    print_arr(arr, len_arr);
    
    
    return 0;
}
