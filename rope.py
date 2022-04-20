class RopeLeaf:
    # Note: depending on your implementation, you may want to to change this constructor
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    # how deep the tree is (I.e. the maximum depth of children)
    def depth(self):
        return 1

    # Whether the rope is balanced, i.e. whether any subtrees have branches
    # which differ by more than one in depth.
    def is_balanced(self):
        return True

    # Helper method which converts the rope into an associative array
    #
    # Only used for debugging, this has no functional purpose
    def to_dictionary(self):
        return {
            "text": self.text,
        }

    def size(self):
        return len(self.text)


class RopeBranch:
    # Note: depending on your implementation, you may want to to change this constructor
    def __init__(self, left, right):
        self.left = left
        self.right = right

        # Please note that this is defined differently from "weight" in the Wikipedia article.
        # You may wish to rewrite this property or create a different one.
        self.cachedSize = (left.size() if left else 0) + (right.size() if right else 0)

    # just prints the stored text
    # note that you may want to change this, depending on your implementation
    def __str__(self):
        leftText = str(self.left) if self.left else ""
        rightText = str(self.right) if self.right else ""
        return leftText + rightText

    # how deep the tree is (I.e. the maximum depth of children)
    def depth(self):
        return 1 + max(self.left_depth(), self.right_depth())

    # Whether the rope is balanced, i.e. whether any subtrees have branches
    # which differ by more than one in depth.
    def is_balanced(self):
        leftBalanced = self.left.is_balanced() if self.left else True
        rightBalanced = self.right.is_balanced() if self.right else True

        return (
            leftBalanced
            and rightBalanced
            and abs(self.left_depth() - self.right_depth()) < 2
        )

    def left_depth(self):
        if not self.left:
            return 0
        return self.left.depth()

    def right_depth(self):
        if not self.right:
            return 0
        return self.right.depth()

    # Please note that this is defined differently from "weight" in the Wikipedia article.
    # You may wish to rewrite this method or create a different one.
    def size(self):
        return self.cachedSize

    # Helper method which converts the rope into an associative array
    #
    # Only used for debugging, this has no functional purpose
    def to_dictionary(self):
        mapVersion = {"size": self.size()}
        if self.right:
            mapVersion["right"] = self.right.to_dictionary()
        if self.left:
            mapVersion["left"] = self.left.to_dictionary()
        return mapVersion


def create_rope_from_map(map):
    if map.get("text") is not None:
        return RopeLeaf(map.get("text"))

    left = None
    right = None
    if "left" in map:
        left = create_rope_from_map(map["left"])
    if "right" in map:
        right = create_rope_from_map(map["right"])
    return RopeBranch(left, right)


# Note: Depending on your implementation, you might want to
# change these to be instance methods on the rope
def split_at(rope, start, end):
    # TODO
    pass

def delete_range(rope, start, end):
    # TODO
    pass


def insert(rope, text, location):
    # TODO
    pass


def rebalance(rope):
    # TODO
    pass