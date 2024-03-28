#include <iostream>
#include <cstring>
using namespace std;

#define MAX_LEN 250

int main(){
    char plainText[MAX_LEN] = "";
    char cipherText[MAX_LEN] = "";

    cout << "Your plain text: ";
    cin.getline(plainText, MAX_LEN);

    for(int i = 0; i < strlen(plainText); i++){
        char letter = plainText[i];

        // if (int(letter) >= "A" && int(letter) <= "Z") {
        //     cipherText[i] = char("Z" - (int(letter) - "A"));

        // } else if (int(letter) >= "a" && int(letter) <= "z") {
        //     cipherText[i] = char("z" - (int(letter) - "a"));

        // } else if (int(letter) >= "0" && int(letter) <= "9") {
        //     cipherText[i] = char("9" - (int(letter) - "0"));

        // } else {
        //     cipherText[i] = char(letter);

        // }

        // With Gemini Assist
        if (isalpha(letter)) {
            int oppositeIndex = isupper(letter) ? 'Z' - letter : 'z' - letter;
            cipherText[i] = oppositeIndex + (isupper(letter) ? 'A' : 'a');

        } else {
            cipherText[i] = letter;
        }
    }

    cout << "Ciphered plain text: " << cipherText << endl;

    return 0;
}