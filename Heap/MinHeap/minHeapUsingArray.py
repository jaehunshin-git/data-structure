import matplotlib.pyplot as plt
import networkx as nx
import subprocess

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

def visualize_heap(heap):
    G = nx.DiGraph()
    labels = {}
    
    for i in range(len(heap)):
        G.add_node(i)
        labels[i] = heap[i]
        
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(heap):
            G.add_edge(i, left)
        if right < len(heap):
            G.add_edge(i, right)
    
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color="skyblue", font_size=15, font_weight="bold", arrows=False)
    output_file = "/mnt/c/Users/JHSHIN/Desktop/UbuntuImgDir/heap_visualization.png"
    plt.savefig(output_file)  # Save the plot as a file
    plt.close()  # Close the figure to free memory

    # Open the saved image file using Windows Explorer
    windows_path = "C:\\Users\\JHSHIN\\Desktop\\UbuntuImgDir\\heap_visualization.png"
    subprocess.run(["explorer.exe", windows_path])

minHeap = MinHeap()

keySet = [48, 54, 40, 19, 62, 95, 94, 52, 36, 32]
for key in keySet:
    minHeap.insert(key)

visualize_heap(minHeap.heap)
