#include <iostream>
#include <string>
#include <fstream>

int main()
{
    std::string input;
    std::ofstream file;
    file.open("./log.txt", std::ios::out|std::ios::trunc);
    // file.clear();
    file.close();
    while (1)
    {
        std::getline(std::cin,input);
        std::cout<<input<<"\n"<<std::flush;
        file.open("./log.txt", std::ios::out|std::ios::app);
        file << input << "\n";
        file.close();
        
    }
    // file.close();
    return 0;
}