#You run a small laundry service. After washing and drying, you end up with a pile of single socks. Each sock is tagged with a size number (e.g., 6, 8, 10, etc.). You want to sort the socks from smallest to largest by size before pairing them.
#You decide to use a very simple sorting method — Bubble Sort — to arrange the socks.

"""
Given the following sock sizes in a random pile:

sock_sizes = [10, 6, 8, 7, 9, 6, 11]


Use Bubble Sort to sort the sock sizes in ascending order.

"""

class BubbleSort:

    def socks_pile(self, sock_sizes):
        self.sock_sizes = sock_sizes

        size = len(sock_sizes)

        for i in range(size):
            swapped = True
            
            for j in range(size - 1 - i):
                if sock_sizes[j] > sock_sizes[j + 1]:
                    sock_sizes[j], sock_sizes[j + 1] = sock_sizes[j + 1], sock_sizes[j]
                    swapped = True
            
            if not swapped:
                break
        return sock_sizes

BB = BubbleSort()
print(BB.socks_pile([10, 6, 8, 7, 9, 6, 11]))
