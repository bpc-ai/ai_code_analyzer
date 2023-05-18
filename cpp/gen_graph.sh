clang++ -S -emit-llvm app.cpp -o app.ll
opt -p dot-callgraph app.ll
cat app.ll.callgraph.dot | c++filt | sed 's,>,\\>,g; s,-\\>,->,g; s,<,\\<,g' | gawk '/external node/{id=$1} $1 != id' | dot -Tpng -oapp.png

