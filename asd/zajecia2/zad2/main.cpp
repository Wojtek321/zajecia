#include <iostream>
#include <fstream>

using namespace std;

void tree(ofstream &output, int n, int a);


int main()
{
    int n;
    ifstream input(R"(In0202.txt)");
    input>>n;
    input.close();

    ofstream output(R"(Out0202.txt)");
    tree(output, n, 0);
    output.close();
}

void tree(ofstream &output, int n, int a)
{
    if(n==1)
    {
        for(int i=0; i<a; i++)
        {
            output<<" ";
        }
        output<<"*"<<endl;
    }
    else
    {
        tree(output, n-2, a+1);

        for(int i=0; i<a; i++)
        {
            output<<" ";
        }

        for(int i=0; i<n; i++)
        {
            output<<"*";
        }
        output<<endl;
    }
}
