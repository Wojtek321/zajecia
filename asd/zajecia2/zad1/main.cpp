#include <iostream>
#include <fstream>

using namespace std;

void quick_sort(int *tab, int l, int r);
void swap(int *tab, int i, int j);

int main()
{
    int n;
    fstream file(R"(In0201.txt)");
    file >> n;
    int *tab = new int[n];
    for(int i=0; i<n; i++)
    {
        file >> tab[i];
    }
    file.close();

    quick_sort(tab, 0, n-1);

    ofstream output(R"(Out0201.txt)");
    for(int i=0; i<n; i++)
    {
        output<<tab[i]<<" ";
    }
    output.close();
}

void quick_sort(int *tab, int l, int r)
{
    if(l >= r)
    {
        return;
    }

    int pivot = tab[(l+r)/2];
    int i = l, j = r;

    while(true)
    {
        while(tab[i] < pivot)
        {
            i++;
        }
        while(tab[j] > pivot)
        {
            j--;
        }
        if(i <= j)
        {
            swap(tab, i, j);
        }
        else
        {
            break;
        }
        i++;
        j--;
    }

    quick_sort(tab, l, j);
    quick_sort(tab, i, r);
}

void swap(int *tab, int i, int j)
{
    int tmp = tab[i];
    tab[i] = tab[j];
    tab[j] = tmp;
}