class Person:

    # 인스턴스 변수를 정의 (예: self.name)
    def __init__(self, name):
        print('test output own data info:', self)
        self.name = name
    # pass

    # instance method
    # self를 통해 인스턴스 변수에 접근 가능
    #  필요할 떄 호출
    def talk(self):
        print("Hi my name is", self.name)


#  person_1의 메모리 주소가 출력됨
#  Person()
#  은 힙 메모리에 공간 할당 및 객체 초기화 그리고 메모리 주소를 참조하는 변수를 생성한다.
# Stack                    Heap
# +-------------+         +------------------+
# |person_1     |  -----> |Person Object     |
# |(reference)  |         |name: "Alice"     |
# +-------------+         |@0x...B235550     |
# |person_2     |  -----> |Person Object     |
# |(reference)  |         |name: "Bob"       |
# +-------------+         |@0x...CD61450     |
# +-------------+         +------------------+
person_1 = Person("Alice")
print(person_1)      # 출력: <__main__.Person object at 0x...B235550>
print(person_1.name) # 출력: "Alice" 문자열은 heap에 저장
print(person_1.talk())
#  person_2의 메모리 주소가 출력됨
person_2 = Person('Bob')
print(person_2)
print(person_2.name)

# // Java
# public class Person {
#     private String name;
#
#     public Person(String name) {
#         this.name = name;
#     }
# }
#
# // Stack                    Heap
# // +---------------+       +------------------+
# // |person1        | ----> |Person Object     |
# // |(reference)    |       |name: "Alice"     |
# // +---------------+       |@0x...B235550     |
# // |person2        | ----> |Person Object     |
# // |(reference)    |       |name: "Bob"       |
# // +---------------+       |@0x...CD61450     |
# // |int x = 5      |       |                  |
# // |(primitive)    |       |                  |
# // +---------------+       +------------------+
#
# Person person1 = new Person("Alice");
# Person person2 = new Person("Bob");
# int x = 5;  // primitive type은 stack에 직접 저장


# Python vs Java Memory Management
# ------------------------------

#  Stack, Heap 모두 RAM(Random Access Momery)에 저장됨 관리 방식에서 좀 차이가 있음
# [Stack 특징]
# - FILO (First In Last Out) 구조
# - 함수 호출과 함께 자동으로 할당/해제
# - 정해진 크기, 빠른 액세스
# - 지역 변수, 함수 호출 정보 저장

# [Heap 특징]
# - 동적 메모리 할당 영역
# - 크기 제한 없음 (시스템 메모리 한도 내)
# - Stack보다 느린 액세스
# - 객체, 동적 할당 데이터 저장
# - Garbage Collection으로 관리

# RAM (Physical Memory)
# +--------------------------------+
# |          Stack 영역             | ← 높은 주소값
# |    - 함수 호출 스택             |
# |    - 지역 변수                  |
# |    - 컴파일 타임에 크기 결정     |
# +--------------------------------+
# |            ↓↑                  | ← Stack과 Heap이 서로를 향해 자람
# +--------------------------------+
# |          Heap 영역             |
# |    - 동적 할당 메모리           |
# |    - 객체들                    |
# |    - 런타임에 크기 변동         | ← 낮은 주소값
# +--------------------------------+

# Stack (위에서 아래로)
# +------------------+
# | function1 stack  | ← 함수 종료 시 깔끔하게 제거
# +------------------+
# | function2 stack  |
# +------------------+
#
# Heap (아래에서 위로)
# +------------------+
# | object3          | ← 객체들이 임의로 생성/제거되어
# | [free space]     |    단편화 발생 가능
# | object1          |
# +------------------+

# Stack은 호출 순서대로 정리되어 단편화가 거의 없음
# Heap은 중간에 빈 공간이 생길 수 있음
# Before:
# Stack ↓        ↑ Heap
# [......]  Gap  [......]
#
# After (메모리 부족 임박):
# Stack ↓  Gap↓  ↑ Heap
# [......]    [......]

# 8GB RAM = 8,589,934,592 bytes (8 * 1024 * 1024 * 1024)
#
# 메모리 주소 범위:
# 0x00000000 ~ 0xFFFFFFFF (32비트 시스템의 경우)
# 또는
# 0x0000000000000000 ~ 0xFFFFFFFFFFFFFFFF (64비트 시스템의 경우)
#
# RAM 구조:
# 0xFFFFFFFFFFFFFFFF (가장 높은 주소)
# +------------------------+
# |     Stack 영역         | ← 높은 주소부터 아래로 성장
# |         ↓             |
# +------------------------+
# |    사용 가능한 공간     |
# |                        |
# +------------------------+
# |         ↑             |
# |     Heap 영역          | ← 낮은 주소부터 위로 성장
# +------------------------+
# 0x0000000000000000 (가장 낮은 주소)

# Stack과 Heap이 만나면:
#
# Stack Overflow나 Heap Overflow 발생
# 'Out of Memory' 에러 발생
# 프로그램 충돌












