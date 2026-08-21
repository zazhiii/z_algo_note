# ✅第 406 场周赛

[3216. 交换后字典序最小的字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/description/)

给你一个仅由数字组成的字符串 `s`，在最多交换一次 **相邻** 且具有相同 **奇偶性** 的数字后，返回可以得到的字典序最小的字符串。

> 贪心

> 因为只能操作一次，那么交换靠左侧的数一定能让字典序尽可能地小，从左往右遍历，遇到第一对相同奇偶且交换后能使字典序更小地数对时，交换这两个数即可。

> $O(n)$

```java
class Solution {
    public String getSmallestString(String s) {
        char c[] = s.toCharArray();
        for(int i = 0; i < c.length - 1; i ++){
            if(c[i] % 2 == c[i + 1] % 2 && c[i] > c[i + 1]){
                char t = c[i];
                c[i] = c[i + 1];
                c[i + 1] = t;
                break;
            }
        }
        return String.valueOf(c);
    }
}
```

[3217. 从链表中移除在数组中存在的节点](https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/)

给你一个整数数组 `nums` 和一个链表的头节点 `head`。从链表中**移除**所有存在于 `nums` 中的节点后，返回修改后的链表的头节点。

> 数据结构

> 添加一个头部哨兵节点，**删除某个元素只能通过前面一个节点改变其下一个指向来删除**，从哨兵节点开始遍历判断下一个节点是否需要删除。

> $O(n)$

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < nums.length; i ++) set.add(nums[i]);
        ListNode hh = new ListNode(0, head);
        ListNode cur = hh;
        while(cur.next != null){
            if(set.contains(cur.next.val)){
                cur.next = cur.next.next;
            }else{
                cur = cur.next;
            }
        }
        return hh.next;
    }
}
```

[3219. 切蛋糕的最小总开销 II](https://leetcode.cn/problems/minimum-cost-for-cutting-cake-ii/)

有一个 `m x n` 大小的矩形蛋糕，需要切成 `1 x 1` 的小块。

给你整数 `m` ，`n` 和两个数组：

- `horizontalCut` 的大小为 `m - 1` ，其中 `horizontalCut[i]` 表示沿着水平线 `i` 切蛋糕的开销。
- `verticalCut` 的大小为 `n - 1` ，其中 `verticalCut[j]` 表示沿着垂直线 `j` 切蛋糕的开销。

一次操作中，你可以选择任意不是 `1 x 1` 大小的矩形蛋糕并执行以下操作之一：

1. 沿着水平线 `i` 切开蛋糕，开销为 `horizontalCut[i]` 。
2. 沿着垂直线 `j` 切开蛋糕，开销为 `verticalCut[j]` 。

每次操作后，这块蛋糕都被切成两个独立的小蛋糕。

每次操作的开销都为最开始对应切割线的开销，并且不会改变。

请你返回将蛋糕全部切成 `1 x 1` 的蛋糕块的 **最小** 总开销。

> 贪心

> 注意到切割次数是不变的，那么让开销大的少切，开销小的多切。每次考虑一切到底，每次**横/竖**一切到底需要切的次数和**竖/横**已经切了几次有关。用两个变量记录横竖已经切了几次，再用当前没切过的最大开销的切法计算当前一步的开销。

> $O(n)$

```java
class Solution {
    public long minimumCost(int m, int n, int[] h, int[] v) {
        Arrays.sort(h);Arrays.sort(v);
        int hh = 0, vv = 0;
        long ans = 0;
        int i, j;
        for(i = m - 2, j = n - 2; i >= 0 && j >= 0;){
            if(h[i] > v[j]){
                hh ++;
                ans += (vv + 1) * h[i];
                i --;
            }else{
                vv ++;
                ans += (hh + 1) * v[j];
                j --;
            }
        }
        if(j >= 0){
            for(int k = j; k >= 0; k --) ans += (hh + 1) * v[k];
        }
        if(i >= 0){
            for(int k = i; k >= 0; k --) ans += (vv + 1) * h[k];
        }
        return ans;
    }
}
```

