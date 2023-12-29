#include <iostream>
#include <fstream>
#include <sstream>
#include <conio.h>

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
                    } break;
                    case 1:
                    {
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
                        p->left->w = 1;
                        p->right->w = 0;
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
                        p->left->w = 0;
                        p->right->w = 0;
                    } break;
                    case 1:
                    {
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
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

bool szukaj(int a, Node *&p)
{
    if(!p)
    {
        return false;
    }
    else if(a > p->key)
    {
        return szukaj(a, p->right);
    }
    else if(a < p->key)
    {
        return szukaj(a, p->left);
    }
    else
    {
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

void wypisz(const Node* node, int odstep = 0, char kierunek = ' ')
{
    if (node != nullptr) {

        int odstep_pom = 3;

        odstep += odstep_pom;

        wypisz(node->right, odstep, 'P');

        for (int i = odstep_pom; i < odstep; i++)
            std::cout << " ";

        if (kierunek == 'P')
            cout << "+--- " << node->key <<" ("<<node->w<<")"<<" (P)" << std::endl;
        else if (kierunek == 'L')
            std::cout << "+--- " << node->key <<" ("<<node->w<<")"<< " (L)" << std::endl;
        else
            std::cout << node->key <<" ("<<node->w<<")"<< std::endl;

        wypisz(node->left, odstep, 'L');

    }
}

//bool balanceDL(Node *&p)
//{
//    cout<<"DL"<<endl;
//    switch (p->w)
//    {
//        case 1:
//        {
//            cout<<"1"<<endl;
//            if (p->left->w == 1)
//            {
//                BR1(p);
//                p->right->w = 0;
//            }
//            else
//            {
//                BL1(p->left);
//                BR1(p);
//                switch (p->w)
//                {
//                    case 0:
//                    {
//                        p->left->w = 0;
//                        p->right->w = 0;
//                    } break;
//                    case 1:
//                    {
//                        p->left->w = 0;
//                        p->right->w = -1;
//                    } break;
//                    case -1:
//                    {
//                        p->left->w = 1;
//                        p->right->w = 0;
//                    } break;
//                }
//            }
//            p->w = 0;
//            return true;
//        } break;
//
//        case 0:
//        {
//            cout<<"0"<<endl;
//            p->w = -1;
//            break;
//        }
//        case -1:
//        {
//            cout<<"-1"<<endl;
//            p->w = 0;
//            return true;
//        } break;
//    }
//    return false;
//}
//
//bool balanceDR(Node *&p)
//{
//    cout<<"DR"<<endl;
//    switch (p->w)
//    {
//        case -1:
//        {
//            cout<<"-1"<<endl;
//            if (p->right->w == -1)
//            {
//                BL1(p);
//                p->left->w = 0;
//            }
//            else
//            {
//                BR1(p->right);
//                BL1(p);
//                switch (p->w)
//                {
//                    case 0:
//                    {
//                        p->left->w = 0;
//                        p->right->w = 0;
//                    } break;
//                    case 1:
//                    {
//                        p->left->w = -1;
//                        p->right->w = 0;
//                    } break;
//                    case -1:
//                    {
//                        p->left->w = 0;
//                        p->right->w = 1;
//                    } break;
//                }
//            }
//            p->w = 0;
//            return true;
//        } break;
//
//        case 0:
//        {
//            cout<<"0"<<endl;
//            p->w = 1;
//            break;
//        }
//        case 1:
//        {
//            cout<<"1"<<endl;
//            p->w = 0;
//            return true;
//        } break;
//    }
//    return false;
//}

bool balanceDL(Node *&p)
{
    cout<<"DL"<<endl;
    switch (p->w)
    {
        case -1:
        {
            cout<<"-1"<<endl;
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
                    } break;
                    case 1:
                    {
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
                        p->left->w = 1;
                        p->right->w = 0;
                    } break;
                }
            }
            p->w = 0;
            return true;
        } break;

        case 0:
        {
            p->w = -1;
            cout<<"0"<<endl;
            break;
        }
        case 1:
        {
            p->w = 0;
            cout<<"1"<<endl;
            return true;
        } break;
    }
    return false;
}

bool balanceDR(Node *&p)
{
    cout<<"DR"<<endl;
    switch (p->w)
    {
        case 1:
        {
            cout<<"1"<<endl;
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
                        p->left->w = 0;
                        p->right->w = 0;
                    } break;
                    case 1:
                    {
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
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
            cout<<"0"<<endl;
            break;
        }
        case -1:
        {
            p->w = 0;
            cout<<"-1"<<endl;
            return true;
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
            else
            if (!q->right)
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

    string linia;
    int a;
    bool dziala = true;

    ifstream file("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia5\\zad1\\InTest1.txt");
    getline(file, linia);
    file.close();
    istringstream line(linia);


    while (line >> a)
    {
//        cout<<"nowa liczba - "<<a<<endl;
        insert(a, root);
    }

    while (dziala)
    {
        cout<<endl<<endl;
        cout<<"1 - Insert"<<endl;
        cout<<"2 - Usun"<<endl;
        cout<<"3 - Szukaj"<<endl;
        cout<<"4 - Wypisz"<<endl;
        cout<<"Numer: ";

        int wybor;
        cin>>wybor;

        switch (wybor)
        {
            case 1:
            {
                cout<<"Podaj liczbe: ";
                cin>>a;
                insert(a, root);
                break;
            }
            case 2:
            {
                cout<<"Podaj liczbe do usuniecia: ";
                cin>>a;
                delete_(a, root);
                break;
            }
            case 3:
            {
                cout<<"Szukana liczba: ";
                cin>>a;
                if(szukaj(a, root))
                {
                    cout<<"Liczba jest w drzewie AVL";
                }
                else
                {
                    cout<<"Brak danej liczby w drzewie";
                }
                break;
            }
            case 4:
            {
                ofstream out("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia5\\zad1\\OutTest3.txt");
                KLP(root, out);
                out.close();
            }
        }
    }
}
