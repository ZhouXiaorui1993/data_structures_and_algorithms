//
//  main.cpp
//  second_biggest_num
//  找出一个数组中第二大的数字
//  Created by zhouxiaorui on 2018/10/5.
//  Copyright © 2018年 zhouxiaorui. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int find_second_big(vector<int> arr)
{
    unsigned long len_arr = arr.size();
    if(len_arr==0)
        return -1;  // 返回-1，表示查找失败
    if(len_arr==1)
        return arr[0];
    if(len_arr==2)
        return arr[0]>arr[1]?arr[1]:arr[0];
    // 找出数组中第二大的数字
    int n1, n2;  // n1保存当前最大值，n2保存当前第二大的值
    if(arr[0]>=arr[1])
    {
        n1=arr[0];
        n2=arr[1];
    }
    else
    {
        n1=arr[1];
        n2=arr[0];
    }
    for(int i=2; i<len_arr; i++)
    {
        if(arr[i]>=n1)
            n1=arr[i];
        else if(arr[i]>n2)
            n2=arr[i];
    }
    return n2;
}
int main(int argc, const char * argv[]) {
    // 数组
    vector<int> arr_test={12, 3, 5, 12, 6, 11, 10, 8};
    int n2 = find_second_big(arr_test);
    cout<<n2<<endl;
    return 0;
}
