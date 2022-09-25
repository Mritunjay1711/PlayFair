#include<bits/stdc++.h>
using namespace std;


//Add your functions like this
void initArray(int arr[5][5], string key)
{

}

pair<int, int> findIndex(int arr[5][5], char ch)
{
    pair<int, int> index;
    if(ch == 'J')
        ch == 'I';

    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            if(ch == arr[i][j])
            {
                index = make_pair(i, j);
                break;
            }
        }
    }
    return index;
}

int main(){
    
    return 0;
}