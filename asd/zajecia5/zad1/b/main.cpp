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
    string key;
    Node* wsk = NULL;
    int w = 0;

    Node(string a)
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
    cout<<"IL"<<endl;
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
                        cout<<"0"<<endl;
                    } break;
                    case 1:
                    {
                        p->left->w = 0;
                        p->right->w = -1;
                        cout<<"1"<<endl;
                    } break;
                    case -1:
                    {
                        p->left->w = 1;
                        p->right->w = 0;
                        cout<<"-1"<<endl;
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

bool balanceIR(Node *&p)
{
    cout<<"IR"<<endl;
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
                        cout<<"0"<<endl;
                        p->left->w = 0;
                        p->right->w = 0;
                    } break;
                    case 1:
                    {
                        cout<<"1"<<endl;
                        p->left->w = 0;
                        p->right->w = -1;
                    } break;
                    case -1:
                    {
                        cout<<"-1"<<endl;
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

bool insert(string a, Node *&p)
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

Node *& znajdz(string a, Node *&p)
{
    if(a > p->key)
    {
        return znajdz(a, p->right);
    }
    else if(a < p->key)
    {
        return znajdz(a, p->left);
    }
    else
    {
        return p;
    }
}

bool szukaj(string a, Node *&p)
{
    if(!p)
    {
        return false;
    }
    if(a > p->key)
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
        out<<p->key<<" "<<p->wsk->key<<endl;
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

bool delete_(string a, Node*& p)
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

void insert(string pesel, string numer, Node *&pesele, Node *&numery)
{
    if(szukaj(pesel, pesele))
    {
        cout<<"Numer pesel znajduje sie juz w drzewie."<<endl;
        return;
    }
    if(szukaj(numer, numery))
    {
        cout<<"Numer telefonu znajduje sie juz w drzewie."<<endl;
        return;
    }


    insert(pesel, pesele);
    insert(numer, numery);

    Node *p = znajdz(pesel, pesele);
    Node *q = znajdz(numer, numery);
    p->wsk = q;
    q->wsk = p;
}

int main()
{
    Node* pesele = NULL;
    Node* numery = NULL;

    srand(time(NULL));


    bool dziala = true;

    while (dziala)
    {
        cout<<endl<<endl;
        cout<<"1 - Plik -> Wczytaj"<<endl;
        cout<<"2 - Plik -> Zapisz"<<endl;
        cout<<"3 - Wstaw -> numer pesel"<<endl;
        cout<<"4 - Wstaw -> numer telefonu"<<endl;
        cout<<"5 - Wyszukaj -> numer pesel"<<endl;
        cout<<"6 - Wyszukaj -> numer telefonu"<<endl;
        cout<<"7 - Usun -> numer pesel"<<endl;
        cout<<"8 - Usun -> numer telefonu"<<endl;
        cout<<"Numer: ";

        int wybor;
        cin>>wybor;

        switch (wybor)
        {
            case 1:
            {
                string linia;
                string pesel, numer;

                ifstream file("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia5\\zad1\\b\\InTest20501.txt");

                while(getline(file, linia))
                {
                    istringstream line(linia);
                    line >> pesel >> numer;
                    insert(pesel, numer, pesele, numery);
                }
                file.close();
                break;
            }
            case 2:
            {
                int x;
                cout<<endl;
                cout<<"Kolejnosc czytania:"<<endl;
                cout<<"1 - pesle"<<endl;
                cout<<"2 - numery telefonow"<<endl;
                cout<<"Numer: ";
                cin>>x;

                ofstream out("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia5\\zad1\\b\\OutTest20501.txt");
                switch(x)
                {
                    case 1:
                    {
                        KLP(pesele, out);
                        break;
                    }
                    case 2:
                    {
                        KLP(numery, out);
                        break;
                    }
                }
                out.close();
                break;
            }
            case 3:
            {
                string pesel, numer;
                cout<<"Numer pesel: ";
                cin>>pesel;
                cout<<"Numer telefonu: ";
                cin>>numer;

                insert(pesel, numer, pesele, numery);
                break;
            }
            case 4:
            {
                string pesel, numer;
                cout<<"Numer telefonu: ";
                cin>>numer;
                cout<<"Numer pesel: ";
                cin>>pesel;

                insert(pesel, numer, pesele, numery);
                break;
            }
            case 5:
            {
                string numer;
                cout<<"Numer telefonu: ";
                cin>>numer;

                if(!szukaj(numer, numery))
                {
                    cout<<"Brak numeru pesel w drzewie."<<endl;
                }
                else
                {
                    Node *p = znajdz(numer, numery);
                    cout<<"Numer pesel: "<<p->wsk->key<<endl;
                }

                break;
            }
            case 6:
            {
                string pesel;
                cout<<"Numer pesel: ";
                cin>>pesel;

                if(!szukaj(pesel, pesele))
                {
                    cout<<"Brak numeru telefonu w drzewie."<<endl;
                }
                else
                {
                    Node *p = znajdz(pesel, pesele);
                    cout<<"Numer telefonu: "<<p->wsk->key<<endl;
                }

                break;
            }
            case 7:
            {
                string pesel;
                cout<<"Numer pesel: ";
                cin>>pesel;

                if(!szukaj(pesel, pesele))
                {
                    cout<<"Brak numeru pesel w drzewie."<<endl;
                }
                else
                {
                    Node *p = znajdz(pesel, pesele);
                    delete_(p->wsk->key, numery);
                    delete_(p->key, pesele);
                }

                break;
            }
            case 8:
            {
                string numer;
                cout<<"Numer telefonu: ";
                cin>>numer;

                if(!szukaj(numer, numery))
                {
                    cout<<"Brak numeru telefonu w drzewie."<<endl;
                }
                else
                {
                    Node *p = znajdz(numer, numery);
                    delete_(p->wsk->key, pesele);
                    delete_(p->key, numery);
                }

                break;
            }
        }
    }
}
