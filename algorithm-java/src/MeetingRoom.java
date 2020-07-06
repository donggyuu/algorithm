import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

// TODO : delete "static"
// TODO : make solution using array(not list)

public class MeetingRoom {

    /**
     * Given an array of meeting time intervals consisting of start and ent times [[s1,e1],[s2,e2],...] ) (si < ei),
     * determine if a person could attend all meetings.
     *
     * -Input: [[0,30], [5,10], [15,20]]
     * -Output : flase
     *
     * -Input: [[7,10],[2,4]]
     * -Output : true
     *
     * ------------------------------------
     *
     * 회의실에는 하나의 팀만 회의가 가능하다.
     * 주어진 것 : 회의의 시작 시간과 종료 시간이 주어짐
     * 결과 :
     * - true  : 회의 시간이 겹치지 않고 모든 회의를 끝낼 수 있다.
     * - false : 회의 시간이 겹쳐서 회의를 끝낼 수 없다.
     *
     */

    public static void main(String[] args) {

        // 회의 시작시간 기준 오름차순 정렬
        // n번째 회의가 끝나는 시간 < n+1번째 회의가 시작하는 시간.

        // 배열을 입력받는다
        // 첫 것을 빼서 오름차순으로 재정렬.
        // for를 돌면서, n의 1번쨰, n+1의 0번째를 비교한다.


        List<Interval> intervals = new ArrayList<Interval>();
        intervals.add(new Interval(2, 4));
        intervals.add(new Interval(7, 10));
        intervals.add(new Interval(11, 20));

        // another way - use array
        // Interval[] intervals = {interval_1, interval_2, interval_3};

        List<Interval> sortedIntervalsByStartTime = intervals.stream()
                .sorted((x, y) -> x.getStart() - y.getStart())
                .collect(Collectors.toList());

        // check sorted list
        for (int i=0; i<3; i++) {
            System.out.println(sortedIntervalsByStartTime.get(i).getStart());
        }

        // solution
        System.out.println(solution(sortedIntervalsByStartTime));

    }


    public static boolean solution(List<Interval> sortedIntervalsByStartTime) {

        // for를 돌면서, n의 1번쨰, n+1의 0번째를 비교한다.
        for (int i=0; i<2; i++) {

            int endValueOfN = sortedIntervalsByStartTime.get(i).getEnd();
            int startValueofNplusOne = sortedIntervalsByStartTime.get(i + 1).getStart();

            if (endValueOfN >= startValueofNplusOne) {
                return false;
            }

        }

        return true;
    }

    static class Interval {

        int start;
        int end;

//        // 지정 안해도 어차피 0으로 초기화됨
//        Interval() {
//            this.start = 0;
//            this.end = 0;
//        }

        Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }

        // Getter
        public int getStart() {
            return start;
        }

        public int getEnd() {
            return end;
        }

    }


}
