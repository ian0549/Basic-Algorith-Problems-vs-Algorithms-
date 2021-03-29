
from collections import defaultdict


class RouteTrieNode:

    def __init__(self, handler=None):
        self.handler = handler
        self.children = defaultdict(RouteTrie)

    def insert(self, path, handler):
        self.children[path] = RouteTrie(handler)

    def __repr__(self):
        return str(self.children)


class RouteTrie:
    def __init__(self, root_handler = None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, paths, handlers):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for path in paths:
            if path not in current_node.children:
                current_node.children[path] = RouteTrieNode(None)
            current_node = current_node.children[path]

        current_node.handler = handlers

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(paths) == 0:
            return self.root.handler

        current_node = self.root
        for path in paths:
            if path not in current_node.children:
                return None
            current_node = current_node.children[path]

        return current_node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        self.route = RouteTrie(handler)
        self.route.root.handler = handler

    def add_handler(self, paths,handler):
     
        path = self.split_path(paths)
        self.route.insert(path,handler)


    def lookup(self, paths):

        path = self.split_path(paths)
        return  self.route.find(path)

    def split_path(self, paths):
        if paths == "/":
            return []
        path_list = paths.split('/')
        
        path_list.remove('')
        return path_list



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


router2 = Router("root handler") 
router2.add_handler("/foo/bar/hello", "hello handler")
router2.add_handler("/foo/bar/udacity", "udacity handler")
router2.add_handler("/foo/bar/hello/world", "world handler")
print("********** Test 2 ***********")
print(router2.lookup("/"))
print(router2.lookup("/foo/bar/udacity"))
print(router2.lookup("/foo/bar/hello"))
print(router2.lookup("/foo/bar/udacity"))
print(router2.lookup("/foo/bar/hello/world"))
print(router2.lookup("/foo/bar"))
print(router2.lookup("/foo/ba"))


router3 = Router("root handler") 
router3.add_handler("/about/pets/four legs", "four legs handler")
router3.add_handler("/about/pets/four legs/dogs/white dogs/bichon frise", "bichon frise handler")
print("********** Test 3 ***********")
print(router3.lookup("/"))
print(router3.lookup("/about/pets/four legs/dogs/white dogs/bichon frise"))
print(router3.lookup("/about/pets/four legs"))
print(router3.lookup("/about"))

"""
root handler
None
about handler
None
None
********** Test 2 ***********
root handler
udacity handler
hello handler
udacity handler
world handler
None
None
********** Test 3 ***********
root handler
bichon frise handler
four legs handler
None

"""