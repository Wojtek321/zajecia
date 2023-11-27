#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

typedef struct Edge{
    int weight;
    int beg;
    int end;
};

int main() {
    int n;
    ifstream file(R"(C:\Users\Wojtek\Desktop\zajecia\asd\zajecia3\zad3\In0303.txt)");
    string linia;

    getline(file, linia);
    istringstream line(linia);
    line>>n;

    vector <vector<Edge>> lista(n);
    lista.clear();
    int beg = 1, end, weight;

    while(getline(file, linia))
    {
        istringstream line(linia);

        while(line >> end >> weight)
        {
            Edge krawedz;
            krawedz.beg = beg;
            krawedz.end = end;
            krawedz.weight = weight;
            lista[beg-1].push_back(krawedz);
        }
        beg++;
    }
    file.close();


//    for(int i=0; i<n; i++)
//    {
//        for(int j=0; j<lista[i].size(); j++)
//        {
//            cout<<lista[i][j].end<<" "<<lista[i][j].weight<<", ";
//        }
//        cout<<endl;
//    }

}

void Kruskal (int n, int m, Edge E[], Edge F[])
{
    Edge e; int p, q, j=0;
    HeapSort(m, E); //sortowanie w porządku niemalejącym ze względu na wagi

    for (int i=1; i<=n; i++)
        X[i]=i; //początkowy podział zbioru wierzchołków,

    while(card(F)<n-1)
    {
        e = min(E);
        p = Find(X, e->beg);
        q = Find(X, e->end);

        if(!Equal(p, q))
        {
            Union(X, p, q);
            F[++j]=e;
        }
    }
}
