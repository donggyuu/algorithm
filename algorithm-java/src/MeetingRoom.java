import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

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

        // ==== solution ====
        // 회의 시작시간 기준 오름차순 정렬
        // Sort by ascend order by MeetingStartTime

        // n번째 회의가 끝나는 시간 < n+1번째 회의가 시작하는 시간.
        // End time of "n" < Start time of n+1
        // ===================

        // dummy data
        List<Interval> intervals = new ArrayList<Interval>();
        intervals.add(new Interval(2, 4));
        intervals.add(new Interval(7, 10));
        intervals.add(new Interval(11, 20));

        List<Interval> intervalsSortedByStartTime = intervals.stream()
                .sorted((x, y) -> x.getStart() - y.getStart())
                .collect(Collectors.toList());

        System.out.println(solution(intervalsSortedByStartTime));

    }

    public static boolean solution(List<Interval> sortedIntervalsByStartTime) {

        int nMeeting = sortedIntervalsByStartTime.size();
        for (int i = 0; i < nMeeting - 1; i++) {

            int endTimeBeforeMeeting = sortedIntervalsByStartTime.get(i).getEnd();
            int startTimeNextMeeting = sortedIntervalsByStartTime.get(i + 1).getStart();

            if (endTimeBeforeMeeting >= startTimeNextMeeting) {
                return false;
            }
        }

        return true;
    }

    static class Interval {

        int start;
        int end;

        Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public int getStart() {
            return start;
        }

        public int getEnd() {
            return end;
        }

    }

}
