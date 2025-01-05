class Dict:
    def __init__(self):
        self.items = [None] * 8

    # hash는 언젠가 충돌이 발생할 수 밖에 없기 때문에
    # chaining 기법으로 해결 (linked list)



    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!