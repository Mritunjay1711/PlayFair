#include <bits/stdc++.h>
using namespace std;

// Add your functions like this
void keyMatrix(char arr[5][5], string key)
{
    vector<int> alpha(26, 0);
    queue<char> q;
    // cout << "RUn";
    for (int i = 0; i < key.size(); i++)
    {
        int temp = key[i] - 'A';
        // cout << temp << endl;
        // cout << "RUN";
        if (key[i] != 'J' && alpha[temp] != 1)
        {
            alpha[temp] = 1;
            q.push(key[i]);
        }
    }
    for (int i = 0; i < alpha.size(); i++)
    {
        if (alpha[i] == 0)
        {
            char temp = i + 'A';
            if (temp != 'J')
                q.push(temp);
        }
    }

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            char temp = q.front();
            q.pop();
            arr[i][j] = temp;
        }
    }
}

void printMatrix(char arr[5][5])
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}


pair<int, int> findIndex(char arr[5][5], char ch)
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

string encrypt(char arr[5][5], string plainText)
{
    int i = 0;
    pair<int, int> ind1, ind2;
    string cypherText = "";
    while(i < plainText.length())
    {
        ind1 = findIndex(arr, plainText[i]);
        i++;
        if(i == plainText.length())
        {
            ind2 = findIndex(arr, 'X');
        }
        else
        {
            ind2 = findIndex(arr, plainText[i]);
            i++;
        }
        if(ind1.first == ind2.first)
        {
            cypherText += arr[ind1.first][(ind1.second+1)%5];
            cypherText += arr[ind2.first][(ind2.second+1)%5];
        }
        else if(ind1.second == ind2.second)
        {
            cypherText += arr[(ind1.first + 1)%5][ind1.second];
            cypherText += arr[(ind2.first + 1)%5][ind2.second];
        }
        else
        {
            cypherText += arr[ind1.first][ind2.second];
            cypherText += arr[ind2.first][ind1.second];
        }
    }
    return cypherText;
}

string filterPlainText(string plainText)
{
    string ans = "";
    for(int i = 0; i <  plainText.length(); i++)
    {
        if(plainText[i] >= 'A' && plainText[i] <= 'Z')
            ans += plainText[i];
    }
    return ans;
}

int main()
{
    int j = 0, i, k;
    string plainText, key;
    cout << "Enter the Plain Text:" << endl;
    getline(cin, plainText);
    cout << "Enter the key:" << endl;
    cin >> key;
    transform(plainText.begin(), plainText.end(), plainText.begin(), ::toupper);
    transform(key.begin(), key.end(), key.begin(), ::toupper);
    plainText = filterPlainText(plainText);
    cout << plainText << endl;
    cout << key << endl;
    char arr[5][5];

    keyMatrix(arr, key);
    cout << "The matrix is:" << endl;
    printMatrix(arr);
    cout << encrypt(arr, plainText);
    return 0;
}