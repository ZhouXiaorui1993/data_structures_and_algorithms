// 顺序线性表的实现---结构体
#include <iostream>
#include <vector>
using namespace std;

#define SUCCESS 0
#define ERROR 1

#define MAXSIZE 20  // 线性表的长度

typedef int Status; // 定义状态值
typedef int ElemType;  // 线性表存储的数据类型
// 用结构体实现
struct Sqlist  // 结构体描述
{
    ElemType *data;  // 存储空间的基地址
    int length;  // 线性表的当前长度
    int list_size;  // 分配给线性表的容量，以sizeof(ElemType)为单位
};

//函数声明
Status InitList(Sqlist &L, int);
Status InsertList(Sqlist &L, int i, ElemType);


// 创建一个顺序线性表
// Sqlist create_sqlist()
//{
//    Sqlist* sqlist = new Sqlist;
//    return *sqlist;
//}

// 初始化一个线性表
Status InitList(Sqlist &L, int size)
{
    L.list_size = size;
    L.data = new ElemType[size];
    L.length = 0;

    return SUCCESS;
}

// 检查是否为空

// 插入操作
Status ListInsert(Sqlist &L, int i, ElemType elem)
{

    // 在索引i处插入数据元素elem
    if(L.length == L.list_size)
    {
        cout<<"list is full, cannot insert numer.\n";
        return ERROR;
    }
    // 遍历i以后的元素，顺序后移
    for(int j=L.length; j>=i; j--)
    {
        L.data[j] = L.data[j-1];
    }
    // 将elem插入i位置
    L.data[i] = elem;
    L.length++;

    //返回成功
    return SUCCESS;
}


// 打印线性表中的内容
void PrintList(const Sqlist &L)
{
    for(int i=0; i<L.length; i++)
    {
        cout<<L.data[i]<<"\t";
    }
    cout<<endl;
}

// 主函数
int main()
{
    Sqlist list;
    int a;
    a = InitList(list, 10); //初始化一个顺序表
    ListInsert(list, 0, 2);
//    cout<<list.data[0]<<endl;
    PrintList(list);

    ListInsert(list,0,3);

    PrintList(list);
    
    // 删除创建的内存
    delete []list.data;
    return 0;
}

