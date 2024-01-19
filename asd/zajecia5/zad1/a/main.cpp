#include <iostream>
#include <fstream>
#include <sstream>
#include <conio.h>
#include <random>

using namespace std;



class Node{
public:
    Node* left = NULL;
    Node* right = NULL;
    int key;
    int w = 0;

    Node(int a)
    {
        this->key = a;
    }
};



void BR1(Node *&p)
{
    Node* pl = p->left;
    p->left = pl->right;
    pl->right = p;
    p = pl;
}

void BL1(Node *&p)
{
    Node* pr = p->right;
    p->right = pr->left;
    pr->left = p;
    p = pr;
}

bool balanceIL(Node *&p)
{
//    cout<<"IL"<<endl;
    switch (p->w)
    {
        case -1:
        {
//            cout<<"-1"<<endl;
            if (p->right->w == -1)
            {
                BL1(p);
                p->left->w = 0;
            }
            else
            {
                BR1(p->right);
                BL1(p);
                switch (p->w)
                {
                    case 0:
                    {
                        p->left->w = 0;
                        p->right->w = 0;
//                        cout<<"0"<<endl;
                    } break;
                    case 1:
                    {
                        p->left->w = 0;
                        p->right->w = -1;
//                        cout<<"1"<<endl;
                    } break;
                    case -1:
                    {
                        p->left->w = 1;
                        p->right->w = 0;
//                        cout<<"-1"<<endl;
                    } break;
                }
            }
            p->w = 0;
            return true;
        } break;

        case 0:
        {
            p->w = -1;
//            cout<<"0"<<endl;
            break;
        }
        case 1:
        {
            p->w = 0;
//            cout<<"1"<<endl;
            return true;
        } break;
    }
    return false;
}

bool balanceIR(Node *&p)
{
//    cout<<"IR"<<endl;
    switch (p->w)
    {
        case 1:
        {
//            cout<<"1"<<endl;
            if (p->left->w == 1)
            {
                BR1(p);
                p ->right->w = 0;
            }
            else
            {
                BL1(p->left);
                BR1(p);
                switch (p->w)
                {
                    case 0:
                    {
//                        cout<<"0"<<endl;
                        p->left->w = 0;
                        p->right->w = 0;
                    } break;
                    case 1:
                    {
//                        cout<<"1"<<endl;
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
//                        cout<<"-1"<<endl;
                        p->left->w = 1;
                        p->right->w = 0;
                    } break;
                }
            }
            p->w = 0;
            return true;
        }
            break;

        case 0:
        {
            p->w = 1;
//            cout<<"0"<<endl;
            break;
        }
        case -1:
        {
            p->w = 0;
//            cout<<"-1"<<endl;
            return true;
        } break;
    }
    return false;
}

bool insert(int a, Node *&p)
{
    if (!p)
    {
        p = new Node(a); return false;
    }
    if (p->key > a)
    {
        if (!insert(a, p->left))
            return balanceIR(p);
    }
    else if (p->key < a)
    {
        if (!insert(a, p->right))
            return balanceIL(p);
    }
    return true;
}

bool szukaj(int a, Node *&p, int poziom)
{
    if(!p)
    {
        cout<<"Brak elementu w drzewie"<<endl;
        return false;
    }
    else if(a > p->key)
    {
        return szukaj(a, p->right, ++poziom);
    }
    else if(a < p->key)
    {
        return szukaj(a, p->left, ++poziom);
    }
    else
    {
        cout<<"Waga: "<<p->w<<", poziom: "<<poziom<<endl;
        return true;
    }
}

void KLP(Node *&p, ofstream &out)
{
    if(p != NULL)
    {
        out<<p->key<<" ("<<p->w<<"), ";
        KLP(p->left, out);
        KLP(p->right, out);
    }
}

void KLP(Node *&p)
{
    if(p != NULL)
    {
        cout<<p->key<<" ("<<p->w<<"), ";
        KLP(p->left);
        KLP(p->right);
    }
}

bool balanceDL(Node *&p)
{
//    cout<<"DL"<<endl;
    switch (p->w)
    {
        case -1:
        {
//            cout<<"-1"<<endl;
            if(p->right->w == -1)
            {
                BL1(p);
                p->left->w = 0;
            }
            else if (p->right->w == 0)
            {
//                cout<<"AA"<<endl;
                BL1(p);
                p->w = 1;
                return true;
            }
            else
            {
                BR1(p->right);
                BL1(p);
                switch (p->w)
                {
                    case 0:
                    {
//                        cout<<"0"<<endl;
                        p->left->w = 0;
                        p->right->w = 0;
                    } break;
                    case 1:
                    {
//                        cout<<"1"<<endl;
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
//                        cout<<"-1"<<endl;
                        p->left->w = 1;
                        p->right->w = 0;
                    } break;
                }
            }
            p->w = 0;
        } break;

            // case 0 jest dobry
        case 0:
        {
//            cout<<"0"<<endl;
            p->w = -1;
            return true;
        } break;
            // case 1 jest dobry
        case 1:
        {
//            cout<<"1"<<endl;
            p->w = 0;
        } break;
    }
    return false;
}

bool balanceDR(Node *&p)
{
//    cout<<"DR"<<endl;
    switch (p->w)
    {
        case 1:
        {
//            cout<<"1"<<endl;
            if(p->left->w == 1)
            {
                BR1(p);
                p->right->w = 0;
            }
            else if (p->left->w == 0)
            {
//                cout<<"AA"<<endl;;
                BR1(p);
                p->w = -1;
                return true;
            }
            else
            {
                BL1(p->left);
                BR1(p);
                switch (p->w)
                {
                    case 0:
                    {
//                        cout<<"0"<<endl;
                        p->left->w = 0;
                        p->right->w = 0;
                    } break;
                    case 1:
                    {
//                        cout<<"1"<<endl;
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
//                        cout<<"-1"<<endl;
                        p->left->w = 1;
                        p->right->w = 0;
                    } break;
                }
            }
            p->w = 0;
            return false;
        } break;

            // case 0 jest dobry
        case 0:
        {
//            cout<<"0"<<endl;
            p->w = 1;
            return true;
        } break;

            // case -1 jest dobry
        case -1:
        {
//            cout<<"-1"<<endl;
            p->w = 0;
        } break;
    }
    return false;
}

bool del(Node*& q, Node* p)
{
    if (q->right)
    {
        if (!del(q->right, p))
            return balanceDR(q);
    }
    else
    {
        p->key = q->key;
        Node* q1 = q;
        q = q->left;
        delete q1;
        return false;
    }
    return true;
}

bool delete_(int a, Node*& p)
{
    if(p)
    {
        if (p->key > a)
        {
            if (!delete_(a, p->left))
                return balanceDL(p);
        }
        else if (p->key < a)
        {
            if (!delete_(a, p->right))
                return balanceDR(p);
        }
        else
        {
            Node* q = p;
            if (!q->left)
            {
                p = p->right;
                delete q;
                return false;
            }
            else if (!q->right)
            {
                p = p->left;
                delete q;
                return false;
            }
            else
            {
                if (!del(q->left, p))
                    return balanceDL(p);
            }
        }
    }
    return true;
}


int main()
{
    Node* root = NULL;


    bool dziala = true;


    srand(time(NULL));

    while (dziala)
    {
        cout<<endl<<endl;
        cout<<"1 - Wczytaj elementy z pliku InTest1.txt"<<endl;
        cout<<"2 - Wczytaj wylosowane elementy"<<endl;
        cout<<"3 - Zapisz drzewo do pliku OutTest3.txt w kolejnosci KLP"<<endl;
        cout<<"4 - Podaj wage i poziom wybranego elementu"<<endl;
        cout<<"5 - Dodaj element do drzewa"<<endl;
        cout<<"6 - Usun element z drzewa"<<endl;
        cout<<"7 - Wypisz drzewo na ekran"<<endl;
        cout<<"Numer: ";

        int wybor;
        cin>>wybor;

        switch (wybor)
        {
            case 1:
            {
                string linia;
                int a;

                ifstream file("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia5\\zad1\\a\\InTest1.txt");
                getline(file, linia);
                file.close();
                istringstream line(linia);


                while (line >> a)
                {
                    insert(a, root);
                }

                break;
            }
            case 2:
            {
                int a, b, n;
                cout<<"Podaj dolne ograniczenie zakresu: ";
                cin>>a;
                cout<<"Podaj gorne ograniczenie zakresu: ";
                cin>>b;
                cout<<"Podaj liczbe losowanych elementow: ";
                cin>>n;

                int range = b - a + 1;


                ofstream out("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia5\\zad1\\a\\OutTest2.txt");
                for(int i=0; i<n; i++)
                {
                    int x = rand() % range + a;
                    insert(x, root);
                    out<<x<<" ";
                }
                out.close();

                break;
            }
            case 3:
            {
                ofstream out("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia5\\zad1\\a\\OutTest3.txt");
                KLP(root, out);
                out.close();

                break;
            }
            case 4:
            {
                int a;
                cout<<"Podaj numer elementu: ";
                cin>>a;

                szukaj(a, root, 0);

                break;
            }
            case 5:
            {
                int a;
                cout<<"Podaj liczbe: ";
                cin>>a;

                insert(a, root);

                break;
            }
            case 6:
            {
                int a;
                cout<<"Podaj liczbe: ";
                cin>>a;

                delete_(a, root);

                break;
            }
            case 7:
            {
                KLP(root);
                break;
            }
        }
    }
}
