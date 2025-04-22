
import unittest
from ProgrammeFiles.Graphs import Graph
class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_edge("B", "D")
        self.graph.add_edge("C", "E")

    def test_add_vertex(self):
        self.graph.add_vertex("F")
        self.assertIn("F", self.graph.adjacencyList)
        self.assertEqual(self.graph.adjacencyList["F"], [])

    def test_add_edge(self):
        self.assertIn("B", self.graph.adjacencyList["A"])
        self.assertIn("A", self.graph.adjacencyList["B"])
        self.assertIn("C", self.graph.adjacencyList["A"])

    def test_remove_edge(self):
        self.graph.remove_edge("A", "B")
        self.assertNotIn("B", self.graph.adjacencyList["A"])
        self.assertNotIn("A", self.graph.adjacencyList["B"])

    def test_remove_vertex(self):
        self.graph.remove_vertex("B")
        self.assertNotIn("B", self.graph.adjacencyList)
        self.assertNotIn("B", self.graph.adjacencyList["A"])
        self.assertNotIn("B", self.graph.adjacencyList["D"])

    def test_bfs(self):
        result = self.graph.bfs("A")
        # BFS could vary in ordering slightly if implemented differently, but from this graph it should be:
        self.assertEqual(result, ["A", "B", "C", "D", "E"])

    def test_dfs(self):
        result = self.graph.dfs("A")
        # DFS result can vary based on recursive call order but from this graph:
        self.assertEqual(result, ["A", "B", "D", "C", "E"])

    def test_display(self):
        # Just testing it doesn't raise any exception
        try:
            self.graph.display()
        except Exception as e:
            self.fail(f"display() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
