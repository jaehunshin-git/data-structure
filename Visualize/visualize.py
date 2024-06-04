import matplotlib.pyplot as plt
import networkx as nx
import subprocess


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


visualize_heap(minHeap.heap)
