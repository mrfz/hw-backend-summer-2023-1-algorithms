from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        output = []
        nodes = [self._root]
        while len(nodes) > 0:
          current_node = nodes.pop(0)
          if current_node not in output: output.append(current_node)
          out_sibs = current_node.outbound
         # out_sibs.reverse()
          for node in out_sibs:
            if node  not in output: nodes.insert(out_sibs.index(node), node)
            
      
        return output

    def bfs(self) -> list[Node]:
        output = []
        nodes = [self._root]
        while len(nodes) > 0:
          current_node = nodes.pop(0)
         # nodes.extend(current_node.outbound)
          if current_node not in output: output.append(current_node)
          out_sibs = current_node.outbound
          for node in  out_sibs:
            if node  not in output: nodes.append(node)
        
        return output
  
