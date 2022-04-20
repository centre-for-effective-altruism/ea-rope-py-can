from rope import delete_range, insert, create_rope_from_map, rebalance
import unittest


def create_leaf(text):
    return create_rope_from_map({"text": text})


# These tests are here as a starting point, they are not comprehensive
class Testing(unittest.TestCase):
    def test_rope_basics(self):
        self.assertEqual(str(create_leaf("test")), "test")
        self.assertEqual(create_leaf("test").size(), 4)
        branch = create_rope_from_map(
            {
                "left": {
                    "left": {"text": "t"},
                    "right": {"text": "e"},
                },
                "right": {"right": {"text": "st"}},
            }
        )
        self.assertEqual(str(branch), "test")
        self.assertEqual(branch.size(), 4)

    def test_deletion(self):
        self.assertEqual(str(delete_range(create_leaf("test"), 1, 3)), "tt")
        self.assertEqual(str(delete_range(create_leaf("test"), 2, 4)), "te")
        self.assertEqual(str(delete_range(create_leaf("test"), 0, 2)), "st")

    def test_insertion(self):
        self.assertEqual(str(insert(create_leaf("test"), "123", 2)), "te123st")
        self.assertEqual(str(insert(create_leaf("test"), "123", 4)), "test123")
        self.assertEqual(str(insert(create_leaf("test"), "123", 0)), "123test")

    def test_extra_credit_rebalancing(self):
        self.assertEqual(
            rebalance(
                create_rope_from_map(
                    {
                        "left": {"text": "a"},
                        "right": {
                            "left": {"text": "b"},
                            "right": {"left": {"text": "c"}, "right": {"text": "d"}},
                        },
                    }
                )
            ).to_dictionary(),
            {
                "size": 4,
                "left": {"size": 2, "left": {"text": "a"}, "right": {"text": "b"}},
                "right": {"size": 2, "left": {"text": "c"}, "right": {"text": "d"}},
            },
        )


if __name__ == "__main__":
    unittest.main()
