#include <QString>
#include <QHash>
#include <QTextStream>
#include <iostream>

using namespace std;

int main(int argc, char *params[]){

QTextStream qtin(stdin); 
quint16 hash;

QString path; 

path = params[1];

//std::cout << "Vas-y pour voir" << std::endl;
//qtin >> path;

hash = qChecksum(path.toUtf8().data(), path.length());

std::cout << hash << std::endl;
return 0;
}
