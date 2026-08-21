# 单调队列

## 原理

双端队列保存候选元素的下标，并维持对应值单调。队首始终是当前窗口的最优值；新元素入队前，从队尾删除不可能再成为答案的元素。

## Java 模板

```java
Deque<Integer> deque = new ArrayDeque<>();
for (int i = 0; i < n; i++) {
    while (!deque.isEmpty() && deque.peekFirst() < i - windowSize + 1) {
        deque.pollFirst();
    }
    while (!deque.isEmpty() && values[deque.peekLast()] >= values[i]) {
        deque.pollLast();
    }
    deque.addLast(i);
    // 当 i >= windowSize - 1 时，values[deque.peekFirst()] 是窗口最小值。
}
```

求窗口最大值时，将队尾比较改为 `<=`。

## 复杂度

- 时间：$O(n)$，每个下标至多入队、出队各一次。
- 空间：$O(k)$，其中 $k$ 为窗口大小。

## 注意事项

- 队列保存下标而不是值，才能判断元素是否离开窗口。
- 先删除过期队首，再维护队尾单调性。
- 明确相等元素保留策略；使用 `>=` 会保留更新的相等元素。
