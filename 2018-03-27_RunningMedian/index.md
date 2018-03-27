## 변화하는 중간값

문제: https://algospot.com/judge/problem/read/RUNNINGMEDIAN

**중간값(Median)**: 주어진 수열을 주어졌을 때, 가운데 오는 값 <br/>
  ex. {3, 1, 5, 4, 2} => 3
- 수열의 길이가 짝수일 때: 가운데 있는 두 값 중 작은 값

### 입력

주어진 a, b 를 이용하여 아래와 같은 규칙으로 생성
- ```A[0] = 1983```
- ```A[i] = (A[i-1] * a + b) % 20090711```

#### 입력 포맷

> C
>
> N a b
>
> ...

- ```C```: 테스트 케이스의 수 (1 <= C <= 20)
- ```N```: 수열의 길이 (1 <= N <= 200,000)
- ```a```, ```b```: 수열 생성에 필요한 파라미터 (0 <= a, b <= 10,000)

### 출력
각 테스트 케이스마다 N개의 중간값의 합을 20090711로 나눈 나머지

----
### Solution #1) Balanced Binary Tree
구현하기 귀찮아...

----
### Solution #2) using heap

들어가기 전에 [Heap](#Heap)을 알아봅시다.

Heap - "루트에 가장 큰(max heap) 값이 있음" 만 보장됨

Index | Sequence | Sorted
------|----------|-------
0 | 3 | 1
1 | 1 | 2
2 | 5 | **3**
3 | 4 | 4
4 | 2 | 5

중간값(Median)을 경계로 min-heap + max-heap의 2 heap 사용
```
1. 최대 힙(max-heap)의 크기는 최소 힙(min-heap)의 크기와 같거나, 하나 더 크다.
2. 최대 힙(max-heap)의 최대 원소는 최소 힙(min-heap)의 최소 원소보다 작거나 같다. 
```

[python heapq](https://docs.python.org/2/library/heapq.html)
- min heap

----

### Heap

![heap is subset of priority queue](http://latex.codecogs.com/gif.latex?heap%20%5Csubset%20priority%5C_queue)

- 대소 관계 규칙(Heap property): 부모 노드가 가진 원소는 항상 자식 노드보다 크다
    - 가장 큰 원소는 루트에 저장
    - Skewed Tree <br/>
       ![skewed tree](https://www.tutorialride.com/images/data-structures/skewed-binary-tree.jpeg)
- 모양 규칙(Shape Property): Complete Binary Tree 여야 함.
    1. 마지막 레벨을 제외하면 모든 레벨에 노드가 꽉 차 있어야 함.
    1. 마지막 레벨에 노드가 있다면, 항상 가장 왼쪽부터 순서대로 채워져 있어야 함.

#### 배열을 이용한 힙의 구현

##### 인덱스

- ```A[i]``` 의 왼쪽 자손: ```A[2 * i + 1]```
- ```A[i]``` 의 오른쪽 자손: ```A[2 * i + 2]```
- ```A[i]``` 의 부모: ```A[int((i-1)/2)]``` 

##### 삽입

모양 규칙 -> 대소관계 규칙

```
1. Add the element to the bottom level of the heap.
2. Compare the added element with its parent; if they are in the correct order, stop.
3. If not, swap the element with its parent and return to the previous step.
```

###### Ex. adding 15
![insertion_1](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Heap_add_step1.svg/250px-Heap_add_step1.svg.png)

![insertion_2](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Heap_add_step2.svg/250px-Heap_add_step2.svg.png)

![insertion_3](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Heap_add_step3.svg/250px-Heap_add_step3.svg.png)

- Time Complexity: ```O(log n)```

##### 제거

제거 -> 모양 규칙 -> 대소관계 규칙

```
1. Replace the root of the heap with the last element on the last level.
2. Compare the new root with its children; if they are in the correct order, stop.
3. If not, swap the element with one of its children and return to the previous step. (Swap with its smaller child in a min-heap and its larger child in a max-heap.)
```

###### Ex. 루트 제거
![extraction_1](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Heap_delete_step0.svg/250px-Heap_delete_step0.svg.png)

![extraction_2](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Heap_remove_step1.svg/250px-Heap_remove_step1.svg.png)

![extraction_3](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Heap_remove_step2.svg/250px-Heap_remove_step2.svg.png)

- Time Complexity: ```O(log n)```
