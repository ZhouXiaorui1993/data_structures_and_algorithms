#include<iostream>
#include<cstring>
using namespace std;

void gen_pnext(const char p[], int pnext[]);
int kmp_matching(const char t[], const char p[], int pnext[]);

int main()
{
    // 目标字符串和模式串
    char t[]="zhouxiaoruizhljbzuizhljzh";
    char p[]="zhljzh";
	
	// 打印t和p
	cout<<"t:\n"<<t<<endl;
	cout<<"p:\n"<<p<<endl;
	
    // 部分匹配表
    int next_len = strlen(p);
    int pnext[next_len]={1};
    
    // 计算pnext
    // gen_pnext(p, pnext);

    // 计算匹配结果
    int res;
    res = kmp_matching(t, p, pnext);
    
     //打印pnext
    for(int i=0; i<next_len; i++)
    	cout<<pnext[i]<<'\t';
    cout<<endl;
    
    cout<<"matching result:"<<res<<endl;
}

void gen_pnext(const char p[], int pnext[])
{
    int q,k;  //q为模式串下标，k为最大前后缀长度，即部分匹配值
    int len_p = strlen(p);
    
    pnext[0]=0; // 模式串的第一个字符的最大相同前后缀长度为0
    for(q=1, k=0; q<len_p; q++)
    {
        // 已知上一部分的部分匹配值为k，判断下一个位置的字符是否与上一个前缀后面的字符匹配
        // 若不匹配，则比较上上一个前缀后面的字符和当前字符，即将待比较的下标设置为pnext[k-1]
        while(k>0 && p[k]!=p[q])
            k = pnext[k-1];
        if(p[k]==p[q])  // 若能够匹配，则跳出循环，并得到当前位置的部分匹配值为k+1
            k++;
        // 设置pnext[q]为k
        pnext[q]=k;
    }
}

int kmp_matching(const char t[], const char p[], int pnext[])
{
    int index_p, index_t;
    int len_t = strlen(t);
    int len_p = strlen(p);
    
    // 计算pnext
    gen_pnext(p, pnext);

    for(index_p=0, index_t=0; index_t<len_t; index_t++)
    {
        // 当模式串和目标串的字符不匹配时（设最后一个匹配的字符为p[index_p-1]），此时要移动目标串，进行下一次比较
        // 移动方法为，将目标串的前缀与已匹配的后缀对齐，比较前缀后一个字符与上一次模式串的失配字符，若匹配，则退出while循环，index_p++，进入下一次for循环继续比较下一个字符；若不匹配，则按此思路继续移动目标串
        while(index_p>0 && p[index_p]!=t[index_t])
            index_p = pnext[index_p-1];
        if(p[index_p]==t[index_t])  //若匹配
            index_p++;
        if(index_p == len_p)  // 若模式串比较结束，证明已经找到匹配的子串，返回其首字符下标
            return index_t-index_p+1;
    }

    // 若目标串遍历完都没找到，证明没有匹配的字符串，返回-1
    return -1;
}
