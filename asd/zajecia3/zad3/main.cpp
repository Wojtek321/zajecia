#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int weight;
    int beg;
    int end;
};

bool compareEdges(const Edge &a, const Edge &b) {
    return a.weight < b.weight;
}

int findParent(vector<int> &parent, int vertex) {
    if (parent[vertex] == -1)
        return vertex;
    return findParent(parent, parent[vertex]);
}

void unionSets(vector<int> &parent, int x, int y) {
    int xSet = findParent(parent, x);
    int ySet = findParent(parent, y);
    parent[xSet] = ySet;
}

void kruskalMST(vector<vector<Edge>> &lista, int n, ofstream &outputFile) {
    vector<Edge> edges;
    for (int i = 0; i < n; ++i) {
        for (const Edge &edge : lista[i]) {
            edges.push_back(edge);
        }
    }

    sort(edges.begin(), edges.end(), compareEdges);

    vector<int> parent(n, -1);
    int edgeCount = 0;
    vector<Edge> minimumSpanningTree;
    int totalWeight = 0;

    for (const Edge &edge : edges) {
        if (edgeCount == n - 1)
            break;

        int begSet = findParent(parent, edge.beg - 1);
        int endSet = findParent(parent, edge.end - 1);

        if (begSet != endSet) {
            minimumSpanningTree.push_back(edge);
            totalWeight += edge.weight;
            unionSets(parent, begSet, endSet);
            edgeCount++;
        }
    }


    for (const Edge &edge : minimumSpanningTree)
    {
        outputFile<<edge.end<< " "<<edge.beg<<" ["<<edge.weight<<"], ";
    }
    outputFile << endl << totalWeight << endl;
}

int main() {
    int n;
    ifstream file("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia3\\zad3\\In0303.txt");
    ofstream outputFile("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia3\\zad3\\Out0303.txt");

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

    kruskalMST(lista, n, outputFile);

    outputFile.close();

    return 0;
}