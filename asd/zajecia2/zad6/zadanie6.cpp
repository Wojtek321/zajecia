#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;


void DFS(int a, vector <vector<int>> &lista, bool *odwiedzony, vector <int> &kolejne_odwiedzone)
{
    kolejne_odwiedzone.push_back(a);
    odwiedzony[a-1] = true;

    for(int i=0; i<lista[a-1].size(); i++)
    {
        if(!odwiedzony[lista[a-1][i] - 1])
        {
            DFS(lista[a-1][i], lista, odwiedzony, kolejne_odwiedzone);
        }
    }
}

int main()
{
    int n;
    ifstream file(R"(In0206.txt)");
    string linia;

    getline(file, linia);
    istringstream line(linia);
    line>>n;

    vector <vector<int>> lista;
    vector <int> kolejne_odwiedzone;
    lista.clear();
    int a;

    while(getline(file, linia))
    {
        vector<int> dane;
        istringstream line(linia);

        while(line >> a)
        {
            dane.push_back(a);
        }
        lista.push_back(dane);
    }
    file.close();

    bool *odwiedzony = new bool[n];
    for(int i=0; i<n; i++)
    {
        odwiedzony[i] = false;
    }



    DFS(1, lista, odwiedzony, kolejne_odwiedzone);

    bool spojny = true;
    for(int i=0; i<n; i++)
    {
        if(!odwiedzony[i])
        {
            spojny = false;
        }
    }


    ofstream out(R"(Out0206.txt)");

    if(spojny)
        out<<"Graf spójny";
    else
        out<<"Graf niespójny";

    out<<endl;

    for(int i=0; i<kolejne_odwiedzone.size(); i++)
    {
        out<<kolejne_odwiedzone[i]<<" ";
    }
    out.close();
}

