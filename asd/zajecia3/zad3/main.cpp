#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge{
    int weight;
    int beg;
    int end;
};

bool porownaj_krawedzie(const Edge &a, const Edge &b)
{
    return a.weight < b.weight;
}

int findParent(vector<int> &parent, int vertex)
{
    if (parent[vertex] == -1)
        return vertex;
    return findParent(parent, parent[vertex]);
}

void unionSets(vector<int> &parent, int x, int y)
{
    int xSet = findParent(parent, x);
    int ySet = findParent(parent, y);
    parent[xSet] = ySet;
}

void kruskal(vector<vector<Edge>> &lista, int n, ofstream &output)
{
    vector<Edge> krawedzie;
    for (int i = 0; i < n; i++)
    {
        for (const Edge &edge : lista[i])
        {
            krawedzie.push_back(edge);
        }
    }

    sort(krawedzie.begin(), krawedzie.end(), porownaj_krawedzie);

    vector<int> parent(n, -1);

    int liczba_wierzcolkow = 0;
    vector<Edge> MDR;
    int waga = 0;

    for (const Edge &edge : krawedzie) {
        if (liczba_wierzcolkow == n - 1)
            break;

        int begSet = findParent(parent, edge.beg - 1);
        int endSet = findParent(parent, edge.end - 1);

        if (begSet != endSet) {
            MDR.push_back(edge);
            waga += edge.weight;
            unionSets(parent, begSet, endSet);
            liczba_wierzcolkow++;
        }
    }


    for (const Edge &edge : MDR)
    {
        output<<edge.end<< " "<<edge.beg<<" ["<<edge.weight<<"], ";
    }
    output << endl << waga << endl;
}

int main() {
    int n;
    ifstream file("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia3\\zad3\\In0303.txt");
    ofstream output("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia3\\zad3\\Out0303.txt");

    string linia;

    getline(file, linia);
    istringstream line(linia);
    line >> n;

    vector<vector<Edge>> lista(n);
    lista.clear();
    int beg = 1, end, weight;

    while (getline(file, linia)) {
        istringstream line(linia);

        while (line >> end >> weight) {
            Edge krawedz;
            krawedz.beg = beg;
            krawedz.end = end;
            krawedz.weight = weight;
            lista[beg - 1].push_back(krawedz);
        }
        beg++;
    }
    file.close();

    kruskal(lista, n, output);

    output.close();

    return 0;
}