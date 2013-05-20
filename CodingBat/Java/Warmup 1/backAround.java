public String backAround(String str) {
  char c = str.charAt(str.length()-1);
  return String.format("%c%s%c",c,str,c);
}
