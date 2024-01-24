#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
void Plecak(int *p, int *w, int n, int W);

int main()
{
    ifstream plik("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia3\\zad2\\In0302.txt");
    int n, W;
    plik>>n>>W;

    int* w = new int[n];
    int* p = new int[n];

    for(int i=0; i<n; i++)
    {
        plik>>p[i]>>w[i];
    }
    plik.close();

    Plecak(p, w, n, W);
}

void Plecak(int *p, int *w, int n, int W)
{
    int** S1 = new int*[W+1];
    int** S2 = new int*[W+1];
    for(int i = 0; i < W+1; i++)
    {
        S1[i] = new int[n+1] {};
        S2[i] = new int[n+1] {};
    }


    for(int i=0; i<W+1; i++)
    {
        for(int j=0; j<n+1; j++)
        {
            if(i==0 || j==0)
            {
                S1[i][j] = S2[i][j] = 0;
            }
            else if(i-w[j-1] >= 0)
            {
                int pom = S1[i-w[j-1]][j-1] + p[j-1];

                if(pom < S1[i][j-1])
                {
                    S1[i][j] = S1[i][j-1];
                }
                else
                {
                    S1[i][j] = pom;
                    S2[i][j] = 1;
                }
            }
            else
            {
                S1[i][j] = S1[i][j-1];
            }
        }
    }


//    for(int i=0; i<W+1; i++)
//    {
//        for(int j=0; j<n+1; j++)
//            cout<<S1[i][j]<<" ";
//        cout<<endl;
//    }
//    cout<<endl;
//    for(int i=0; i<W+1; i++)
//    {
//        for(int j=0; j<n+1; j++)
//            cout<<S2[i][j]<<" ";
//        cout<<endl;
//    }


    std::vector<int> kombinacje;
    int i;
    int j;
    int maks = S1[W][n];
    ofstream out("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia3\\zad2\\Out0302.txt");

    for(int a=n; a>0; a--)
    {
        j = a;
        i = W;

        if(S1[i][j] == maks)
        {
            kombinacje.push_back(j);
            i -= w[j-1];
            while(j>0)
            {
                if(S2[i][j])
                {
                    kombinacje.push_back(j);
                    break;
                }
                j--;
            }
        }

        if(kombinacje.size() != 0)
        {
            for (int b = kombinacje.size() - 1; b >= 0; b--)
            {
                out << kombinacje[b] << " ";
            }
            kombinacje.clear();
            out << endl;
        }
    }

    delete []S1;
    delete []S2;
    out.close();
}