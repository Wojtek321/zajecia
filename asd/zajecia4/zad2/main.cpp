#include <iostream>
#include <fstream>
#include <sstream>


using namespace std;

struct el
{
    el * next;
    int v, w;
};

int MAXINT = 2147483647/2;

ofstream output("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia4\\zad2\\Out0402.txt");


void Johnson(el **list, int n);
int* Ford_Bellman(el **list, int n, int s);
int* Dijkstra(el **list, int n, int u);


void Johnson(el **list, int n)
{
    el ** list2 = new el * [n+1];
    el *pv;
    el *pz;

    for(int i=0; i<n+1; i++)
    {
        list2[i] = NULL;
    }

    for(int a=1; a<=n; a++)
    {
        pv = new el;
        pv->v = a;
        pv->w = 0;
        pv->next = list2[0];
        list2[0] = pv;
    }

    for(int i=0; i<n; i++)
    {
        pv = list [ i ];
        while(pv)
        {
            pz = new el;
            pz->v = pv->v;
            pz->v += 1;
            pz->w = pv->w;
            pz->next = list2[i+1];
            list2[i+1] = pz;
            pv = pv->next;
        }
    }




    int *h = Ford_Bellman(list2, n+1, 0);

    for(int i=0; i<n+1; i++)
    {
        output<<h[i]<<" ";
    }
    output<<endl;



    for(int i = 0; i < n+1; i++ )
    {
        output << "["<<i<<"] ";
        pv = list2 [ i ];
        while( pv )
        {
            pv->w = pv->w + h[i] - h[pv->v];
            output<<pv->v<<"("<<pv->w<<") ";
            pv = pv->next;
        }
        output << endl;
    }



    el ** list3 = new el * [n];
    for(int i=0; i<n; i++)
    {
        list3[i] = NULL;
    }

    for(int i = 0; i < n; i++ )
    {
        pv = list2 [ i+1 ];
        while( pv )
        {
            pz = new el;
            pz->v = pv->v-1;
            pz->w = pv->w;
            pz->next = list3[i];
            list3[i] = pz;
            pv = pv->next;
        }
    }


    for(int i=0; i<n; i++)
    {
        int *delta = Dijkstra(list3, n, i);


        output<<"Delta^["<<i+1<<"][";
        if(delta[0]>MAXINT-10000 || delta[0]<-MAXINT+10000)
            output<<"-";
        else
            output<<delta[0];

        for(int j=1; j<n-1; j++)
        {
            if(delta[j]>MAXINT-10000 || delta[j]<-MAXINT+10000)
                output<<" -";
            else
                output<<" "<<delta[j];
        }

        if(delta[n-1]>MAXINT-10000 || delta[n-1]<-MAXINT+10000)
            output<<" -";
        else
            output<<" "<<delta[n-1];





        output<<"], D["<<i+1<<"][";
        if(delta[0]>MAXINT-10000 || delta[0]<-MAXINT+10000)
            output<<"-";
        else
            output<<delta[0] + h[1] - h[i+1];

        for(int j=1; j<n-1; j++)
        {
            if(delta[j]>MAXINT-10000 || delta[j]<-MAXINT+10000)
                output<<" -";
            else
                output<<" "<<delta[j] + h[j+1] - h[i+1];;
        }

        if(delta[n-1]>MAXINT-10000 || delta[n-1]<-MAXINT+10000)
            output<<" -]";
        else
            output<<" "<<delta[n-1] + h[n] - h[i+1]<<"]";

        output<<endl;
    }
}

int* Dijkstra(el **list, int n, int v)
{
    int *d = new int[n];
    int *p = new int[n];
    bool *QS = new bool[n];
    el *pv;

    for(int i=0; i<n; i++)
    {
        d[i] = MAXINT;
        p[i] = -1;
        QS[i] = false;
    }

    d[v] = 0;
    int j, u;

    for(int i = 0; i < n; i++ )
    {
        for( j = 0; QS [ j ]; j++ );

        for( u = j++; j < n; j++ )
            if( !QS [ j ] && ( d [ j ] < d [ u ] ) ) u = j;

        QS [ u ] = true;

        for( pv = list[ u ]; pv; pv = pv->next )
            if( !QS [ pv->v ] && ( d [ pv->v ] > d [ u ] + pv->w ) )
            {
                d [ pv->v ] = d [ u ] + pv->w;
                p [ pv->v ] = u;
            }
    }

    return d;
}

int* Ford_Bellman(el **list, int n, int s)
{
    int *d = new int [n];
    int *p = new int [n];
    el *pv;

    for(int i=0; i<n; i++)
    {
        d[i] = MAXINT;
        p[i] = -1;
    }

    bool test;
    d[s] = 0;
    for(int i=1; i<n; i++)
    {
        test = true;
        for(int x=0; x<n; x++)
        {
            for(pv=list[x]; pv; pv=pv->next)
            {
                if(d[pv->v] > d[x] + pv->w)
                {
                    test = false;
                    d[pv->v] = d[x] + pv->w;
                    p[pv->v] = x;
                }
            }
        }
        if(test)
        {
            return d;
        }
    }
    return d;
}


int main()
{
    ifstream file("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia4\\zad2\\In0402.txt");

    string linia;
    int n;

    getline(file, linia);
    istringstream line(linia);
    line >> n;

    el **list = new el * [n];
    el *pv;
    int wierzcholek, waga;


    for(int i=0; i<n; i++)
    {
        list[i] = NULL;
    }


    int i = 0;
    while (getline(file, linia))
    {
        istringstream line(linia);

        while (line >> wierzcholek >> waga)
        {
            pv = new el;
            pv->v = wierzcholek-1;
            pv->w = waga;
            pv->next = list[i];
            list[i] = pv;
        }
        i++;
    }
    file.close();


//    Johnson(list, n);

    int *h = Dijkstra(list, 4, 1);

    for(int i=0; i<n; i++)
    {
        cout<<h[i]<<" ";
    }
    output<<endl;


    output.close();
}
