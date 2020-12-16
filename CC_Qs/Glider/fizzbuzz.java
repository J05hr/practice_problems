// https://leetcode.com/problems/fizz-buzz/

public static class SalesPath {

    public List<String> fizzBuzz(int n) {
        List<String> anss = new ArrayList<String>();
        for (int idx = 1; idx <= n; idx++){
            String ans = "";
            if (idx % 3 == 0){
                ans = ans + "Fizz";
            }
            if (idx % 5 == 0){
                ans = ans + "Buzz";
            }
            if (ans.equals("")){
                ans = ans + Integer.toString(idx);
            }
            System.out.println(ans);
            anss.add(ans);
        }
        return anss;
    }
}


public static void main(String[] args) {
    n = 10
    ans = SalesPath.getCheapestCost(n)
    System.out.println(ans)
}
