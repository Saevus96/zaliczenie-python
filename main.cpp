#include <iostream>
#include <fstream>
#include <vector>
#include<string>
#include<cctype>

std::vector<char> alphabet = { 'A','B','C','D','E','F','G','H','I','J','K','L'
		,'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
		'0','1','2','3','4','5','6','7','8','9' };

void crypt(int move, std::string word, std::fstream &fileInOut) {

	std::vector<char>cryptedWord(word.size());	
	//char singleChar;

	for (int i = 0; i < word.size(); i++) {
		
		for (int j = 0; j < alphabet.size(); j++) {
			int difference = 0;

			if (word[i] <= 64 || word[i] >= 91 || word[i] <= 96 || word[i] >= 123 && word[i]=='–') {
				cryptedWord[i] = word[i];				
			}					
			/*if (word[i] != alphabet[j]) {
				singleChar = word[i];
				char upperChar = toupper(singleChar);				

				if (upperChar == alphabet[j] && j < (alphabet.size() - move)){
					cryptedWord[i] = tolower(alphabet[j + move]);
					break;
				}
				else if(upperChar == alphabet[j] && j >= (alphabet.size() - move)) {
					difference = j + move - alphabet.size();
					cryptedWord[i] = tolower(alphabet[difference]);
					break;
				}				
			}*/
			if (toupper(word[i]) == alphabet[j] && j<(alphabet.size() - move)) {				
				cryptedWord[i] = alphabet[j + move];
				break;
			}	
			else if (toupper(word[i]) ==alphabet[j] && j>=(alphabet.size()-move)) {
				difference = j + move - alphabet.size();				
				cryptedWord[i] = alphabet[difference];										
				break;
			}
		}		
		fileInOut << cryptedWord[i];		
	}	
	cryptedWord.clear();
}
void encrypt(int move, std::string word, std::fstream &fileOut) {

	std::vector<char>uncryptedWord(word.size());

	for (int i = 0; i < word.size(); i++) {

		for (int j = 0; j < alphabet.size(); j++)
		{
			int difference = 0;
			if (word[i] <= 64 || word[i] >= 92 || word[i] <= 95 || word[i] >= 123 && word[i] == '–') {
				uncryptedWord[i] = word[i];
			}
			if (word[i] == alphabet[j] && j-move>=0) {
				uncryptedWord[i] = alphabet[j - move];
				break;
			}
			else if (word[i] == alphabet[j] && j-move < 0) {
				difference = j - move + alphabet.size();
				uncryptedWord[i] = alphabet[difference];
				break;
			}			
		}
		fileOut << uncryptedWord[i];
	}	
	uncryptedWord.clear();
}
int main(){

	std::fstream fileIn;
	fileIn.open("plik.txt", std::ios::in | std::ios::out);

	std::fstream fileInOut;
	fileInOut.open("poszyfrowaniu.txt", std::ios::out |std::ios::in | std::ios::app);

	std::fstream fileOut;
	fileOut.open("poodkodowaniu.txt", std::ios::in | std::ios::out | std::ios::app);

	int move;
	std::string line ="";	
	int operation = 0;
	
	std::cout << "Podaj przesuniecie" << std::endl;	
	std::cin >> move;
	std::cout << "Podaj typ operacji: 1 - crypt, \n 2 - encrypt" << std::endl;
	std::cin >> operation;

	switch (operation)
	{
	case 1:
		std::cout << "szyfrowanie pliku plik.txt" << std::endl;
		while (!fileIn.eof()) {
			line = "";
			std::getline(fileIn, line); 			
			crypt(move, line, fileInOut);	
			
			if(!fileIn.eof())
				fileInOut << std::endl;
		} 	
		std::cout << "Sprawdz plik poszyfrowaniu.txt " << std::endl;
		break;

	case 2:
		std::cout << "deszyfrowanie pliku" << std::endl;
		while (!fileInOut.eof()) {
			line = "";
			std::getline(fileInOut, line);
			encrypt(move, line, fileOut);

			if (!fileInOut.eof())
				fileOut << std::endl;
		}
		std::cout << "Sprawdz plik poodkodowaniu.txt" << std::endl;
		break;			
	}

	fileIn.close();
	fileInOut.close();
	fileOut.close();
	
	std::cout << std::endl;
	system("pause");
	return 0;
}