public boolean loneTeen(int a, int b) {
  return isTeen(a) ^ isTeen(b);
}

public boolean isTeen(int n){
   return n >= 13 && n <= 19;
}