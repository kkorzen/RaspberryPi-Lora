#include "rgb_file.h"

int main(){
    char msg[100];
    CreateMessegeFromRGB(msg);
    printf("%s", msg);
    return 0;
}

int readline(FILE* f, char line[]){
    int len = 0;
    char c = 0;

    while((c=fgetc(f))!='\n' && c!=EOF){
        line[len] = c;
        len++;
    }
    line[len] = '\0';
    return len;
}

void CreateMessegeFromRGB(char msg[]){
    FILE* f;
    f = fopen("rgbs.txt", "r");

    char line[128];
    int len = 0;
    unsigned char rgbs[3]; int i = 0;

    while((len = readline(f, line))>0){
         rgbs[i] = ScanStringForRGBValue(line);
         i++; 
    }
    fclose(f);
    sprintf(msg, "%d %d %d", rgbs[0], rgbs[1], rgbs[2]);  
}

int ScanStringForRGBValue(char str[]){
    strrev(str);
    int i = 0;
    char* value = malloc(strlen(str) * sizeof(char) + 1);
    while(str[i]!=':'){
        value[i] = str[i];
        i++;
    }
    value[i] = '\0';
    strrev(str);
    return atoi(strrev(value));
}