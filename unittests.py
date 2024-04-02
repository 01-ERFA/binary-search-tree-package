from src.bst import BinarySearchTree as Tree
import unittest

class TestTree(unittest.TestCase):
    default_values1 = [12, 34, 45, 16, 35, 57]
    default_values2 = [2, 12, 4, 34, 8, 45, 1, 16, 9, 35, 3, 57]

    def test_001_init(self):
        tree = Tree(int)
        self.assertEqual(tree.length, 0)
        self.assertEqual(len(tree), 0)

        self.assertEqual(tree.height, 0)
        
        self.assertEqual(tree.is_empty, True)
        self.assertEqual(bool(tree), False)

        self.assertEqual(tree.max_value, None)
        self.assertEqual(tree.min_value, None)

    def test_002_init_with_dict(self):
        tree = Tree(dict, lambda x : x.get('custom', None)).insert(*[ dict({'custom': val }) for val in self.default_values1])

        self.assertEqual(tree.length, len(self.default_values1))

        self.assertEqual(tree.height != 0, True)
        self.assertEqual(tree.is_empty, False)
        self.assertEqual(bool(tree), True)

        self.assertEqual(tree.max_value, {'custom': max(self.default_values1)})
        self.assertEqual(tree.min_value, {'custom': min(self.default_values1)})

    def test_003_deepcopy_tree_and_clear(self):
        tree1 = Tree(int).insert(*self.default_values1)
        tree2 = tree1.copy()

        tree1.clear()

        self.assertEqual(tree1.height, 0)
        self.assertEqual(len(tree1), 0)
        self.assertEqual(tree1.is_empty, True)

        self.assertEqual(tree2.height != 0, True)
        self.assertEqual(len(tree2), len(self.default_values1))
        self.assertEqual(tree2.is_empty, False)

    def test_004_iter_empty_tree(self):
        tree = Tree(int)

        self.assertEqual(list(tree), [])
        self.assertEqual(tree.length, 0)

    def test_005_contains(self):
        tree1 = Tree(int).insert(*self.default_values1)
        tree2 = Tree(int).insert(*self.default_values2)

        self.assertEqual(tree1 in tree1, True)
        self.assertEqual(tree2 in tree2, True)

        self.assertEqual(tree1 in tree2, True)
        self.assertEqual(tree2 in tree1, False)

        self.assertEqual(all(val in tree1 for val in self.default_values1), True)
        self.assertEqual(all(val in tree2 for val in self.default_values2), True)

    def test_006_unique_elements(self):
        tree = Tree(int).insert(*self.default_values2).insert(*self.default_values1).insert(*self.default_values2)

        self.assertEqual(len(tree), len(self.default_values2))
    
    def test_007_get_item(self):
        tree = Tree(int).insert(*self.default_values1)

        c = []
        for n in range(len(tree)):
            self.assertEqual(tree[n] in self.default_values1 and tree[n] not in c, True)
            c.append(tree[n])

    def test_008_min_max_one_element(self):
        tree = Tree(int).insert(3)

        self.assertEqual(tree.min_value, 3)
        self.assertEqual(tree.max_value, 3)
    
    def test_009a_pop_one_element(self):
        tree = Tree(int).insert(30)

        self.assertEqual(tree.pop(), 30)
        self.assertEqual(tree.length, 0)

    def test_009b_pop_elements(self):
        tree = Tree(int).insert(*self.default_values1)

        self.assertEqual(tree.pop(), max(self.default_values1))
        self.assertEqual(tree.length, len(self.default_values1) -1)
        
    def test_009c_pop_tree_empty(self):
        tree = Tree(int)

        self.assertEqual(tree.pop(), None)
        self.assertEqual(tree.length, 0)

    def test_010a_popleft_one_element(self):
        tree = Tree(int).insert(30)

        self.assertEqual(tree.popleft(), 30)
        self.assertEqual(tree.length, 0)

    def test_010b_popleft_elements(self):
        tree = Tree(int).insert(*self.default_values1)

        self.assertEqual(tree.popleft(), min(self.default_values1))
        self.assertEqual(tree.length, len(self.default_values1) -1)
        
    def test_010c_popleft_tree_empty(self):
        tree = Tree(int)

        self.assertEqual(tree.popleft(), None)
        self.assertEqual(tree.length, 0)

    def test_011a_remove_item(self):
        tree = Tree(int).insert(3)

        tree.remove(3)
        self.assertEqual(tree.length, 0)
        self.assertEqual(tree.is_empty, True)

    def test_011b_remove_item_from_tree_empty(self):
        tree = Tree(int)

        tree.remove(*self.default_values1)
        self.assertEqual(tree.length, 0)
        self.assertEqual(tree.is_empty, True)
    
    def test_011c_remove_items(self):
        tree = Tree(int).insert(*self.default_values2)

        tree.remove(*self.default_values1)
        self.assertEqual(tree.length, len(self.default_values2) - len(self.default_values1))
        self.assertEqual(tree.is_empty, False)

    def test_011d_remove_item_from_reference(self):
        tree = Tree(dict, lambda x : x.get('custom', None)).insert(*[ dict({'custom': val }) for val in self.default_values2])

        tree.remove(*self.default_values1)
        self.assertEqual(tree.length, len(self.default_values2) - len(self.default_values1))
        self.assertEqual(tree.is_empty, False)

    def test_012_clear(self):
        tree = Tree(int).insert(*self.default_values1)
        
        self.assertEqual(tree.length != 0, True)
        tree.clear()
        self.assertEqual(tree.length != 0, False)

    def test_013a_difference(self):
        tree1 = Tree(int).insert(*self.default_values1)
        tree2 = Tree(int).insert(*self.default_values2)

        difference = tree1.copy().remove(*tree2)

        self.assertEqual(difference in tree1, True)
        self.assertEqual(difference.length, 0)
        self.assertEqual(tree1.length, len(self.default_values1))
        self.assertEqual(difference.is_empty, True)

        difference = tree2.copy().remove(*tree1)

        self.assertEqual(difference in tree2, True)
        self.assertEqual(difference.length, len(self.default_values2) - len(self.default_values1))
        self.assertEqual(tree2.length, len(self.default_values2))
        self.assertEqual(difference.is_empty, False)

    def test_013b_difference(self):
        tree1 = Tree(int).insert(*self.default_values1)
        tree2 = Tree(int).insert(*self.default_values2)

        difference = tree1 - tree2

        self.assertEqual(difference in tree1, True)
        self.assertEqual(difference.length, 0)
        self.assertEqual(tree1.length, len(self.default_values1))
        self.assertEqual(difference.is_empty, True)

        difference = tree2 - tree1

        self.assertEqual(difference in tree2, True)
        self.assertEqual(difference.length, len(self.default_values2) - len(self.default_values1))
        self.assertEqual(tree2.length, len(self.default_values2))
        self.assertEqual(difference.is_empty, False)

    def test_013c_difference(self):
        tree = Tree(int).insert(10)

        self.assertEqual(tree.length, 1)
        tree = tree - 10
        self.assertEqual(tree.length, 0)

        tree = tree - 11
        self.assertEqual(tree.length, 0)

        tree.insert(*self.default_values1)

        self.assertEqual(tree.length, len(self.default_values1))

        tree = tree - self.default_values1[0]
        self.assertEqual(tree.length, len(self.default_values1) -1)

    
    def test_014a_union(self):
        tree1 = Tree(int).insert(*self.default_values1)
        tree2 = Tree(int).insert(*self.default_values2)

        union = tree2.copy().insert(*tree1)

        self.assertEqual(tree1 in tree2, True)
        self.assertEqual(union == tree2, True)
        self.assertEqual(union in tree2, True)

        union = tree1.copy().insert(*tree2)

        self.assertEqual(tree1 in tree2, True)
        self.assertEqual(union == tree2, True)
        self.assertEqual(union in tree2, True)

    def test_014b_union(self):
        tree1 = Tree(int).insert(*self.default_values1)
        tree2 = Tree(int).insert(*self.default_values2)

        union = tree2 + tree1

        self.assertEqual(tree1 in tree2, True)
        self.assertEqual(union == tree2, True)
        self.assertEqual(union in tree2, True)

        union = tree1 + tree2

        self.assertEqual(tree1 in tree2, True)
        self.assertEqual(union == tree2, True)
        self.assertEqual(union in tree2, True)

    def test_014c_union(self):
        tree = Tree(int)

        self.assertEqual(tree.length, 0)
        tree = tree + 10
        self.assertEqual(tree.length, 1)

        tree = tree + 11
        self.assertEqual(tree.length, 2)

    def test_015_intersection(self):
        tree1 = Tree(int).insert(*self.default_values1)
        tree2 = Tree(int).insert(*self.default_values2)

        intersection = ((tree1 + tree2) - (tree1 - tree2)) - (tree2 - tree1)

        self.assertEqual(tree1 in tree2, True)
        self.assertEqual(intersection == tree1, True)

    

    def test_016_eq(self):
        tree1 = Tree(int).insert(*self.default_values2)
        tree2 = Tree(int).insert(*self.default_values2)

        self.assertEqual(tree1 == tree2, True)
        self.assertEqual(tree1 != tree2, False)

        self.assertEqual(tree1 == (tree2.insert(19999)), False)
        self.assertEqual(tree1 != tree2.insert(19999), True)

    def test_017_iter(self):
        tree = Tree(int).insert(*self.default_values2)

        c = []
        for n in tree:
            self.assertEqual(n in self.default_values2 and n not in c, True)
            c.append(n)


    def test_018_height_stabilize(self):
        import math
        tree = Tree(int).insert(*self.default_values2).stabilize()

        self.assertEqual(tree.height <= math.ceil(math.log2(tree.length +1)), True)

        tree = Tree(int).stabilize()
        self.assertEqual(tree.height <= math.ceil(math.log2(tree.length +1)), True)

        tree.insert(3).stabilize()
        self.assertEqual(tree.height <= math.ceil(math.log2(tree.length +1)), True)

        tree.insert(*[n for n in range(2000)]).stabilize()
        self.assertEqual(tree.height <= math.ceil(math.log2(tree.length +1)), True)

    def test_019_exists(self):
        tree = Tree(int).insert(*self.default_values2).stabilize()

        self.assertEqual(tree.exists(*self.default_values1), True)
        self.assertEqual(tree.exists(*self.default_values2), True)


        self.assertEqual(tree.exists(19999), False)
        self.assertEqual(tree.exists(19999, *self.default_values1), False)

    def test_020_is_compatible(self):
        tree = Tree(int).insert(*self.default_values1).stabilize()

        self.assertEqual(tree.is_compatible(*self.default_values1), True)
        self.assertEqual(tree.is_compatible(*self.default_values2), True)

        self.assertEqual(tree.is_compatible("false"), False)
        self.assertEqual(tree.is_compatible("false", False), False)
        self.assertEqual(tree.is_compatible(1, 2, 3, 4, 5, "false", False), False)

    def test_021a_search(self):
        tree = Tree(int).insert(*self.default_values1).stabilize()

        self.assertEqual(tree.search(12), True)  
        self.assertEqual(tree.search(20000), False)

    def test_021b_search(self):
        tree = Tree(dict, lambda x: x.get('custom', None))

        tree.insert({'custom': 10},{'custom': 15}, {'custom': 20}, {'custom': 35}, {'custom': 0}).stabilize()

        self.assertEqual(tree.length, 5)
        self.assertEqual(tree.is_empty, False)

        self.assertEqual(tree.search(10), {'custom': 10})  
        self.assertEqual(tree.search(20), {'custom': 20})  

        self.assertEqual(tree.search(30), None)  
        self.assertEqual(tree.search(-1), None)  

    def test_021c_search(self):
        class MyClass1:
            def __init__(self, attribute):
                self.attribute = attribute
        class MyClass2:
            def __init__(self, attribute):
                self.__attribute = attribute

            @property
            def attribute(self):
                return self.__attribute

        tree1 = Tree(MyClass1, 'attribute')
        tree2 = Tree(MyClass2, 'attribute')

        obj11 = MyClass1(10)
        obj12 = MyClass1(20)
        obj13 = MyClass1(30)

        obj21 = MyClass2(10)
        obj22 = MyClass2(20)
        obj23 = MyClass2(30)

        tree1.insert(obj11, obj12, obj13).stabilize()
        tree2.insert(obj21, obj22, obj23).stabilize()

        self.assertEqual(tree1.search(10), obj11) 
        self.assertEqual(tree1.search(20), obj12) 
        self.assertEqual(tree1.search(30), obj13) 
        self.assertEqual(tree1.search(40), None)  

        self.assertEqual(tree2.search(10), obj21) 
        self.assertEqual(tree2.search(20), obj22) 
        self.assertEqual(tree2.search(30), obj23) 
        self.assertEqual(tree2.search(40), None)  

    def test_022_inorder(self):

        tree = Tree(int).insert(*self.default_values1).stabilize()

        self.assertEqual(tree.inorder(), sorted(self.default_values1))
        
        tree.insert(*self.default_values2)
        self.assertEqual(tree.inorder(), sorted(self.default_values2))

    def test_023_preorder(self):
        """
              35
            /    \
          16      57
         /  \    /
        12  34  45

        [35, 16, 12, 34, 57, 45]
        """
        tree = Tree(int).insert(*self.default_values1).stabilize()

        self.assertEqual(tree.preorder(), [35, 16, 12, 34, 57, 45])

    def test_024_postorder(self):
        """
              35
            /    \
          16      57
         /  \    /
        12  34  45

        [12, 34, 16, 45, 57, 35]
        """

        tree = Tree(int).insert(*self.default_values1).stabilize()
        self.assertEqual(tree.postorder(), [12, 34, 16, 45, 57, 35])

    def test_025_levelorder(self):
        """
              35
            /    \
          16      57
         /  \    /
        12  34  45

        [35, 16, 57, 12, 34, 45]
        """
        tree = Tree(int).insert(*self.default_values1).stabilize()
        self.assertEqual(tree.levelorder(), [35, 16, 57, 12, 34, 45])

    def test_026_spiralorder(self):
        """
              35
            /    \
          16      57
         /  \    /
        12  34  45

        [35, 16, 57, 45, 34, 12]
        """
        tree = Tree(int).insert(*self.default_values1).stabilize()
        self.assertEqual(tree.spiralorder(), [35, 16, 57, 45, 34, 12])


if __name__ == '__main__':
    unittest.main()