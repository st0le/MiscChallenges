public boolean hasTeen(int a, int b, int c) {
  return isTeen(a) || isTeen(b) || isTeen(c);
}

public boolean isTeen(int n){
   return n >= 13 && n <= 19;
}