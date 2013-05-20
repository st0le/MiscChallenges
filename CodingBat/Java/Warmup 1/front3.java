public String front3(String str) {
  String first3 = str.substring(0,Math.min(3,str.length()));
  return String.format("%s%s%s",first3,first3,first3);
}
