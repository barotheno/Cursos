#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{

    int numeros, suma = 0;

    do
    {
        cout<<"Digite un numero: ";cin>>numero;

        if(numero>0){
            suma = suma + numero;
        }
    } while (((numero<20) || (numero>30)) && numero != 0);

    cout<<"\nLa suma es: "<<suma<<endl;
    
    return 0;
}
