#2941
import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    word = input().strip()
    specialCharacter = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for character in specialCharacter :
        word = word.replace(character, '*')
    print(len(word))