#include<fstream>
#include<queue>
#include<string>
using namespace std;

int main(){
    ifstream in("A.in"); ofstream out("A.out");
    int N;
    in>>N;
    char c;
    string s;
    for(int i=0;i<N;i++){
        in>>s;
        char prev='D'; int numpush=0; char init[3]; int stacksize=0;
        for(int j=0;(s[j]=='A')||(s[j]=='B')||(s[j]=='C');j++){
            if (s[j]!=prev){
                prev=s[j];
                if (stacksize==0) {init[0]=prev; stacksize=1;numpush++;}
                else if (stacksize==1){
                    init[1]=prev; stacksize=2; numpush++;
                }
                else if (stacksize==2){
                    if (prev==init[0]) stacksize=1;
                    else {stacksize=3; init[2]=prev; numpush++;}
                }
                else {
                    if (prev==init[0]) stacksize=1;
                    else stacksize=2;
                }
            }
        }
        out<<"Case #"<<i+1<<": "<<2*numpush+s.length()<<"\n";
        s.clear();
    }
    return 0;
}