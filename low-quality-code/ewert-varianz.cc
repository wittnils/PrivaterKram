// Code für Erwartungswert & Varianz auf Whtheo Blatt 10   
#include <cmath>
#include <iostream>
#include <fstream>



double mean(int n, int m){
    return (std::pow(m-1,n))/(std::pow(m,n-1));
}

double varianz(double n, double m, double mu){
    return mu*(1-m*mean(n,m));
}

int main(){
    std::ofstream out("file.dat"); 
    out << "Jaeger" << " " << "Enten" << " " << "mu" << " " << "sigma^2" << std::endl;
    for(int i = 1; i <= 200; ++i){
        for(int j = 10; j <= 10; ++j){
            out << i << " " << j << " " << mean(i,j) << " " << varianz(i,j,mean(i,j)) << " " << std::endl; 
        }
    }
    out.close();
    return 0; 
}