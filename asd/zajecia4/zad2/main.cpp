#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>

using namespace std;

void johnson();
void ford_bellman(int n);
void dijkstry();

struct el
{
    el * next;
    int v, w;
};

el ** list;
long long *d;
int *p;
el * pv;
el * pz;
int MAXINT = 2147483647;

void ford_bellman(int n)
{
    el ** list2 = new el * [n+1];
    long long *d2;
    int *p2;
    d2 = new long long [n+1];
    p2 = new int [n+1];

    for(int i=0; i<n+1; i++)
    {
        d2[i] = MAXINT;
        p2[i] = -1;
        list2[i] = NULL;
    }

    for(int a=1; a<n+1; a++)
    {
        pv = new el;
        pv->v = a;
        pv->w = 0;
        pv->next = list2[0];
        list2[0] = pv;
    }

    for(int i=0; i<n+0; i++)
    {
        pv = list [ i ];
        while(pv)
        {
            pz = new el;
            pz->v = pv->v;
            pz->w = pv->w;
            pz->next = list2[i+1];
            list2[i+1] = pz;
            pv = pv->next;
        }
    }

//    for(int i = 0; i < n+1; i++ )
//    {
//        cout << "A [ " << i << " ] =";
//        pv = list2 [ i ];
//        while( pv )
//        {
////            cout <<setw ( 3 ) <<  pv->v;
//            cout<<" wierzcholek: "<<pv->v<<", waga: "<<pv->w<<", next: "<<pv->next;
//            pv = pv->next;
//        }
//        cout << endl;
//    }
    bool test;
    d[0] = 0;
    for(int i=1; i<n+1; i++)
    {

    }
}

int main()
{
    ifstream file("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia4\\zad2\\In0402.txt");

    string linia;
    int n;

    getline(file, linia);
    istringstream line(linia);
    line >> n;

    list = new el * [n];
    d = new long long [n];
    p = new int [n];
    int wierzcholek, waga;


    for(int i=0; i<n; i++)
    {
        list[i] = NULL;
        p[i] = -1;
        d[i] = MAXINT;
    }


    int i = 0;
    while (getline(file, linia))
    {
        istringstream line(linia);

        while (line >> wierzcholek >> waga)
        {
            pv = new el;
            pv->v = wierzcholek;
            pv->w = waga;
            pv->next = list[i];
            list[i] = pv;
        }
        i++;
    }
    file.close();




    for( i = 0; i < n; i++ )
    {
        cout << "A [ " << i << " ] =";
        pv = list [ i ];
        while( pv )
        {
//            cout <<setw ( 3 ) <<  pv->v;
            cout<<" wierzcholek: "<<pv->v<<", waga: "<<pv->w<<", next: "<<pv->next;
            pv = pv->next;
        }
        cout << endl;
    }
    cout<<endl;

    ford_bellman(n);
}
