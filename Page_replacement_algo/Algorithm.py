class Page:
    def __init__(self, page_num: int, ref_bit: bool = False):
        self.page_num = page_num
        self.ref_bit = ref_bit
        self.next_page = None

    def get_page_num(self) -> int:
        return self.page_num

    def get_ref_bit(self) -> bool:
        return self.ref_bit

    def set_ref_bit(self, flag: bool):
        self.ref_bit = flag

    def get_next_page(self) -> "Page":
        return self.next_page

    def set_next_page(self, page: "Page"):
        self.next_page = page

    def set_page_num(self, page_num: int):
        self.page_num = page_num


class LRU:
    def __init__(self, cache_size: int = 5):
        self.page_list = None
        self.cache_size = cache_size
        self.current_size = 0

    def page_in_cache(self, page_num) -> [bool, Page]:
        start = self.page_list
        if start is None:
            return [False, None]

        curr = start
        while True:
            if curr.get_page_num() == page_num:
                return [True, curr]
            curr = curr.get_next_page()
            if curr == start:
                break
        return [False, None]

    def find_page_to_replace(self) -> Page:
        start = self.page_list
        while True:
            if start.get_ref_bit():
                start.set_ref_bit(False)
                start = start.get_next_page()
            else:
                return start

    def add_page(self, page_num):
        if self.page_list is None:
            self.page_list = Page(page_num, False)
            self.page_list.set_next_page(self.page_list)
            self.current_size += 1 
            return

        flag, page = self.page_in_cache(page_num)

        if flag:
            page.set_ref_bit(True)
            return
        elif self.current_size < self.cache_size:
            new_page = Page(page_num, False)
            curr = self.page_list
            while curr.get_next_page() != self.page_list:
                curr = curr.get_next_page()
            curr.set_next_page(new_page)
            new_page.set_next_page(self.page_list)
            self.current_size += 1
        else:
            victim = self.find_page_to_replace()
            victim.set_page_num(page_num)
            victim.set_ref_bit(False)


def print_cache(lru: LRU):
    if lru.page_list is None:
        print("Cache is empty")
        return
    pages = []
    current = lru.page_list
    while True:
        pages.append(f"[{current.get_page_num()}|{int(current.get_ref_bit())}]")
        current = current.get_next_page()
        if current == lru.page_list:
            break
    print(" -> ".join(pages))


def test_lru():
    lru = LRU(3)
    sequence = [1, 2, 3, 2, 4, 1, 5, 6]
    for num in sequence:
        print(f"\nInserting page {num}")
        lru.add_page(num)
        print_cache(lru)


test_lru()
