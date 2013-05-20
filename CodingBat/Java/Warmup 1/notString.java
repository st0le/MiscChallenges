public String notString(String str) {
  return str.startsWith("not") ? str : String.format("not %s",str);
}
