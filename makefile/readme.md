# Makefile

## with g++ 
```cpp
g++ -Wall -Wextra -Werror -c main.cpp -o main.o
```

## with gcc
```cpp
gcc main.cpp -lstdc++ -o main.o
```

## with makefile
```cpp
CXX = g++

all: hello

my_executable : main.o
  $(CXX) -o my_executable main.o

util.o: util.cc
  $(CXX) -c -o util.o util.cc

main.o: main.cc
  $(CXX) -c -o main.o main.cc

// -lstd++ is after the *.o files
hello: main.o util.o
  $(CXX) -o hello main.o util.o -lstdc++

clean:
  -rm util.o main.o hello
```

- Use the ldd tool to find out the shared libraries required by each program 
```bash
ldd main
```

- linking
```bash
gcc <object files> -o <output file name>
```

## relocation
```bash
gcc -c reloc.c -o reloc.o
readelf --relocs reloc.o
objdump --disassemble reloc.o 
```

- [gcc linking](https://www.thegeekstuff.com/2011/10/gcc-linking/)
- [reverse engineer](https://jasonblog.github.io/note/Reversing/linux_ni_xiang_gong_cheng_de_gong_ju_jie_shao.html)