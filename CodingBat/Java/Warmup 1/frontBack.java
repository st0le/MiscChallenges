public String frontBack(String str) {
  char [] arr = str.toCharArray();
  if(arr.length > 0)
  {
  char hold = arr[0];
  arr[0] = arr[arr.length-1];
  arr[arr.length-1] = hold;
  str = new String(arr);
  }
  return str;
}