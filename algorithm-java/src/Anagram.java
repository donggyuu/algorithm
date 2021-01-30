import java.util.Arrays;

public class Anagram {

    /*
    Anagram인지를 판별하는 함수를 구하기.
    Anagram : 두 문자열을 재배열하였을때 같은 단어 혹은 문장.
        ex. apple과 ppale, abcd와 acdb
     */
    public static void main(String[] args) {

        System.out.println(isAnagram("apple", "ppale"));

    }

    private static boolean isAnagram(String firstWord, String secondWord) {

        // 비교를 위해 공백 제거
        firstWord.replaceAll("\\s", "");
        secondWord.replaceAll("\\s", "");

        // 문자 길이 확인
        if (firstWord.length() != secondWord.length()) {
            return false;
        }

        // 문자 비교를 위해 모두 소문자로 변경
        char[] firstCharList = firstWord.toLowerCase().toCharArray();
        char[] secondCharList = secondWord.toLowerCase().toCharArray();

        // 정렬
        Arrays.sort(firstCharList);
        Arrays.sort(secondCharList);

        // 비교
        for (int i=0; i<firstCharList.length; i++) {
            if (firstCharList[i] != secondCharList[i]) {
                return false;
            }
        }

        return true;

//        // 문자열로 변환하는 방법도 가능
//        String tempFirst = new String(firstCharList);
//        String tempSecond = new String(secondCharList);
//        return tempFirst.equals(tempSecond);

    }

}
