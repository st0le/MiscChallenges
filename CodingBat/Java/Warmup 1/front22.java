public String front22(String str) {
  String f2 = str.substring(0,Math.min(2,str.length()));
  return String.format("%s%s%s",f2,str,f2);
}
